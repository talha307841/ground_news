import openai
import json

class ScriptGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key
        
    def generate_script(self, news_data):
        system_prompt = """You are an expert news video scriptwriter for a premier news channel. Your task is to:
        1. Create an engaging news script from the provided content
        2. Include natural transitions between stories
        3. Write in a clear, broadcast-friendly style
        4. Highlight key points while maintaining viewer interest
        5. Keep sentences concise and easy to follow
        6. Add appropriate tone markers and pauses [PAUSE] where needed
        
        Format the script with:
        - Clear segment breaks
        - Timing indicators
        - Camera direction notes [ZOOM] [PAN] etc.
        - Tone indicators [SERIOUS] [UPBEAT] where appropriate"""
        
        try:
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Create a news video script from this data:\n\n{json.dumps(news_data, indent=2)}"}
            ]
            
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages,
                max_tokens=2000,
                temperature=0.7
            )
            
            return response['choices'][0]['message']['content'].strip()
            
        except Exception as e:
            print(f"Error generating script: {e}")
            raise