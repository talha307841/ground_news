import cv2
import numpy as np
import torch
import subprocess
import os
from tqdm import tqdm
import shutil
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

class VideoGenerator:
    def __init__(self, wav2lip_path, face_detector_path, output_dir):
        self.wav2lip_path = wav2lip_path
        self.face_detector_path = face_detector_path
        self.output_dir = output_dir
        self.temp_dir = os.path.join(output_dir, 'temp')
        
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
    
    def prepare_audio(self, audio_files):
        """Combine multiple audio files into a single file."""
        combined_audio = os.path.join(self.temp_dir, 'combined_audio.wav')
        
        # Use FFmpeg to concatenate audio files
        audio_list = os.path.join(self.temp_dir, 'audio_list.txt')
        with open(audio_list, 'w') as f:
            for audio_file in audio_files:
                f.write(f"file '{audio_file}'\n")
        
        subprocess.run([
            'ffmpeg', '-f', 'concat', '-safe', '0',
            '-i', audio_list, '-c', 'copy',
            combined_audio
        ])
        
        return combined_audio
    
    def prepare_video(self, anchor_video, duration):
        """Prepare anchor video to match audio duration."""
        video = VideoFileClip(anchor_video)
        
        # Loop video if needed to match audio duration
        if video.duration < duration:
            num_loops = int(np.ceil(duration / video.duration))
            video = concatenate_videoclips([video] * num_loops)
        
        # Trim to match audio duration
        video = video.subclip(0, duration)
        
        temp_video = os.path.join(self.temp_dir, 'temp_anchor.mp4')
        video.write_videofile(temp_video)
        
        return temp_video
    
    def generate_lip_sync_video(self, anchor_video, audio_path):
        """Generate lip-synced video using Wav2Lip."""
        output_path = os.path.join(self.output_dir, 'final_news_video.mp4')
        
        # Run Wav2Lip
        subprocess.run([
            'python', 'inference.py',
            '--checkpoint_path', self.wav2lip_path,
            '--face', anchor_video,
            '--audio', audio_path,
            '--outfile', output_path,
            '--face_det_batch_size', '4',
            '--wav2lip_batch_size', '8',
            '--resize_factor', '2',
            '--face_detector', self.face_detector_path,
            '--no_smooth'  # Optional: remove if you want motion smoothing
        ])
        
        return output_path
    
    def cleanup(self):
        """Remove temporary files and directory."""
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    def generate_video(self, audio_files, anchor_video):
        try:
            # Step 1: Combine audio files
            combined_audio = self.prepare_audio(audio_files)
            
            # Get audio duration
            audio_clip = AudioFileClip(combined_audio)
            audio_duration = audio_clip.duration
            audio_clip.close()
            
            # Step 2: Prepare anchor video
            prepared_video = self.prepare_video(anchor_video, audio_duration)
            
            # Step 3: Generate lip-sync video
            final_video = self.generate_lip_sync_video(prepared_video, combined_audio)
            
            # Cleanup
            self.cleanup()
            
            return final_video
            
        except Exception as e:
            logging.error(f"Error in video generation: {e}")
            self.cleanup()
            raise