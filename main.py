from config import Config
from news_scraper import NewsScraper
from script_generator import ScriptGenerator
from audio_generator import AudioGenerator
from video_generator import VideoGenerator
import logging

def main():
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    try:
        # Ensure output directory exists
        Config.ensure_output_dir()
        
        # Step 1: Scrape news
        logging.info("Starting news scraping...")
        scraper = NewsScraper(Config.NEWS_URLS)
        news_data = scraper.scrape_news(Config.MAX_NEWS_ITEMS)
        
        # Save raw news data
        news_output_file = os.path.join(Config.OUTPUT_DIR, "raw_news.json")
        with open(news_output_file, 'w', encoding='utf-8') as f:
            json.dump(news_data, f, indent=2)
        
        # Step 2: Generate script
        logging.info("Generating news script...")
        script_generator = ScriptGenerator(Config.OPENAI_API_KEY)
        script_text = script_generator.generate_script(news_data)
        
        # Save script
        script_output_file = os.path.join(Config.OUTPUT_DIR, "news_script.txt")
        with open(script_output_file, 'w', encoding='utf-8') as f:
            f.write(script_text)
        
        # Step 3: Generate audio
        logging.info("Generating audio files...")
        audio_generator = AudioGenerator(Config.OUTPUT_DIR)
        audio_files = audio_generator.generate_audio(script_text)
        
        # Step 4: Generate video
        logging.info("Generating lip-sync video...")
        video_generator = VideoGenerator(
            Config.WAV2LIP_MODEL_PATH,
            Config.FACE_DETECTOR_PATH,
            Config.OUTPUT_DIR
        )
        final_video = video_generator.generate_video(
            audio_files,
            Config.ANCHOR_VIDEO_PATH
        )
        
        logging.info("Process completed successfully!")
        logging.info(f"Final video saved to: {final_video}")
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    main()