from gtts import gTTS
import re
import os

class AudioGenerator:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        
    def clean_text(self, text):
        """Removes content inside square brackets and extra whitespace."""
        return re.sub(r'\[.*?\]', '', text).strip()
        
    def split_text(self, text, max_length=5000):
        """Splits text into smaller chunks for processing."""
        paragraphs = text.split("\n\n")
        chunks = []
        current_chunk = ""
        
        for paragraph in paragraphs:
            if len(current_chunk) + len(paragraph) + 2 <= max_length:
                current_chunk += paragraph + "\n\n"
            else:
                chunks.append(current_chunk.strip())
                current_chunk = paragraph + "\n\n"
                
        if current_chunk:
            chunks.append(current_chunk.strip())
            
        return chunks
        
    def generate_audio(self, script_text):
        cleaned_text = self.clean_text(script_text)
        chunks = self.split_text(cleaned_text)
        audio_files = []
        
        for i, chunk in enumerate(chunks):
            output_file = os.path.join(self.output_dir, f"news_audio_part_{i+1}.mp3")
            tts = gTTS(text=chunk, lang='en')
            tts.save(output_file)
            audio_files.append(output_file)
            
        return audio_files