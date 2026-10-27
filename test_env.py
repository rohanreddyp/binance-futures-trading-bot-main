from dotenv import load_dotenv
import os

load_dotenv()

print("API KEY:", os.getenv("API_KEY"))
print("API SECRET EXISTS:", os.getenv("API_SECRET") is not None)