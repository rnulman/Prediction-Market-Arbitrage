import os
from dotenv import load_dotenv
from cryptography.hazmat.primitives import serialization
from clients import KalshiHttpClient, Environment

# Load .env file
load_dotenv()

# Load environment variables
KEYID = os.getenv("KALSHI_API_KEY")
KEYFILE = os.getenv('KALSHI_KEY_PATH')
env = Environment.DEMO  # toggle environment here

# Load private key
try:
    with open(KEYFILE, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None  # Provide password if necessary
        )
except FileNotFoundError:
    raise FileNotFoundError(f"Private key file not found at {KEYFILE}")
except Exception as e:
    raise Exception(f"Error loading private key: {str(e)}")

# Initialize the HTTP client
client = KalshiHttpClient(
    key_id=KEYID,
    private_key=private_key,
    environment=env
)

# **1. Get Account Balance**
try:
    balance = client.get_balance()
    print("Account Balance:", balance)
except Exception as e:
    print("Error fetching balance:", e)

# **2. Get Exchange Status**
try:
    status = client.get_exchange_status()
    print("Exchange Status:", status)
except Exception as e:
    print("Error fetching exchange status:", e)

# **3. Get Available Markets**
try:
    markets = client.get(client.markets_url)
    print("Available Markets:", markets)
except Exception as e:
    print("Error fetching markets:", e)
