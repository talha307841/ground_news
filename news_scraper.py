import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import logging

class NewsScraper:
    def __init__(self, urls):
        self.urls = urls
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        
    def fetch_article_content(self, article_url):
        try:
            response = requests.get(article_url, headers=self.headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            
            article_text = ' '.join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])
            return article_text or "Content not found."
            
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching article: {e}")
            return f"Error fetching article: {e}"

    def scrape_news(self, max_items=30):
        data = []
        
        for url in self.urls:
            try:
                logging.info(f"Scraping: {url}")
                response = requests.get(url, headers=self.headers)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.text, 'html.parser')
                articles = soup.find_all('a', href=True)
                
                for article in articles:
                    if len(data) >= max_items:
                        return data
                        
                    headline = article.get_text(strip=True)
                    article_url = article['href']
                    
                    if not headline or not article_url.startswith(('http', '/')):
                        continue
                        
                    article_url = urljoin(url, article_url)
                    article_text = self.fetch_article_content(article_url)
                    data.append({
                        'headline': headline,
                        'url': article_url,
                        'content': article_text
                    })
                    
            except Exception as e:
                logging.error(f"Error scraping {url}: {e}")
                
        return data[:max_items]