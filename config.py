import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    NEWS_URLS = [
        "https://www.bbc.com/news",
        "https://edition.cnn.com/world",
        "https://www.nytimes.com/section/world",
        "https://www.reuters.com/news/archive/worldNews",
    ]
    MAX_NEWS_ITEMS = 30
    OUTPUT_DIR = "output"
    WAV2LIP_MODEL_PATH = "checkpoints/wav2lip.pth"  # Path to Wav2Lip model
    FACE_DETECTOR_PATH = "checkpoints/face_detection.pth"  # Path to face detection model
    ANCHOR_VIDEO_PATH = "assets/anchor.mp4"  # Path to news anchor video
    
    @classmethod
    def ensure_output_dir(cls):
        if not os.path.exists(cls.OUTPUT_DIR):
            os.makedirs(cls.OUTPUT_DIR)