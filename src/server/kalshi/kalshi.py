import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Access environment variables
KALSHI_API_KEY = os.getenv("KALSHI_API_KEY")

print(KALSHI_API_KEY)