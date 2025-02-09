from google import genai
from dotenv import load_dotenv


env = load_dotenv('.env')
client = genai.Client(api_key=env['API_KEY'])

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works",
)

print(response.text)