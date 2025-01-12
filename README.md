# AI News Video Generator

An automated pipeline that generates news videos by scraping current news, creating scripts using GPT, converting text to speech, and generating lip-synced news anchor videos.

## 🌟 Features

- Scrapes latest news from major news websites
- Generates professional news scripts using GPT-4
- Converts scripts to natural-sounding speech
- Creates lip-synced news anchor videos
- Fully automated end-to-end pipeline

## 🛠️ Technologies Used

- Python 3.8+
- OpenAI GPT-4
- Beautiful Soup 4
- gTTS (Google Text-to-Speech)
- Wav2Lip
- OpenCV
- PyTorch
- FFmpeg

## 📋 Prerequisites

- Python 3.8 or higher
- FFmpeg installed on your system
- OpenAI API key
- NVIDIA GPU (recommended for video generation)
- Wav2Lip models and dependencies

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-news-video-generator.git
cd ai-news-video-generator
```

2. Create and activate a virtual environment:
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Set up Wav2Lip:
```bash
git clone https://github.com/Rudrabha/Wav2Lip.git
cd Wav2Lip

# Download pre-trained models
mkdir checkpoints
wget "https://github.com/Rudrabha/Wav2Lip/raw/master/checkpoints/wav2lip.pth" -O checkpoints/wav2lip.pth
wget "https://github.com/Rudrabha/Wav2Lip/raw/master/checkpoints/face_detection.pth" -O checkpoints/face_detection.pth
```

5. Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_api_key_here
```

6. Prepare the project structure:
```
project/
├── assets/
│   └── anchor.mp4          # Your news anchor video
├── checkpoints/
│   ├── wav2lip.pth
│   └── face_detection.pth
├── output/                 # Generated files will be saved here
└── ...
```

## 🎯 Usage

1. Place your news anchor video in the `assets` folder as `anchor.mp4`

2. Run the main script:
```bash
python main.py
```

The script will:
- Scrape the latest news
- Generate a news script using GPT
- Create audio files from the script
- Generate a lip-synced video with the news anchor

3. Find the output files in the `output` directory:
- `raw_news.json`: Scraped news data
- `news_script.txt`: Generated script
- `news_audio_part_*.mp3`: Generated audio segments
- `final_news_video.mp4`: Final news video

## 📁 Project Structure

```
project/
├── config.py              # Configuration settings
├── news_scraper.py        # News scraping functionality
├── script_generator.py    # GPT script generation
├── audio_generator.py     # Audio generation using gTTS
├── video_generator.py     # Video generation with Wav2Lip
└── main.py               # Main execution file
```

## ⚙️ Configuration

Edit `config.py` to customize:
- News sources
- Maximum number of news items
- Model paths
- Output directories
- Other settings

## 🔧 Troubleshooting

1. **FFmpeg Issues**
   - Windows: Install using `choco install ffmpeg`
   - macOS: Install using `brew install ffmpeg`
   - Linux: Install using `sudo apt-get install ffmpeg`

2. **CUDA/GPU Issues**
   - Ensure NVIDIA drivers are installed
   - Install CUDA-compatible PyTorch version
   - Uncomment GPU-specific requirements in requirements.txt

3. **System Dependencies (Linux)**
```bash
sudo apt-get update
sudo apt-get install python3-dev
sudo apt-get install portaudio19-dev
sudo apt-get install python3-opencv
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- [Wav2Lip](https://github.com/Rudrabha/Wav2Lip) for the lip-sync technology
- OpenAI for GPT API
- News sources used in the project

## ⚠️ Disclaimer

This project is for educational purposes only. Ensure you have the right to use any news content and follow the terms of service of all APIs and services used.

## 📧 Contact

Your Name - your.email@example.com

Project Link: [https://github.com/yourusername/ai-news-video-generator](https://github.com/yourusername/ai-news-video-generator)