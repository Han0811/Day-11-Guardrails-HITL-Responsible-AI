"""
Lab 11 — Configuration & API Key Setup
"""
import os
from dotenv import load_dotenv

# Tải các biến từ file .env
load_dotenv()

def setup_api_key():
    """Load OpenAI API key from environment."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        api_key = input("Enter OpenAI API Key: ")
        os.environ["OPENAI_API_KEY"] = api_key
    else:
        # Đảm bảo OpenAI library nhận được key
        os.environ["OPENAI_API_KEY"] = api_key
    print("API keys configured.")


# Allowed banking topics (used by topic_filter)
# Đã mở rộng cho cả Arena Lập trình
ALLOWED_TOPICS = [
    "banking", "account", "transaction", "transfer",
    "loan", "interest", "savings", "credit",
    "deposit", "withdrawal", "balance", "payment",
    "tai khoan", "giao dich", "tiet kiem", "lai suat",
    "chuyen tien", "the tin dung", "so du", "vay",
    "ngan hang", "atm",
    "python", "variable", "loop", "coding", "programming", "list", "tuple", "code", "lập trình", "biến", "vòng lặp"
]

# Blocked topics (immediate reject)
BLOCKED_TOPICS = [
    "hack", "exploit", "weapon", "drug", "illegal",
    "violence", "gambling", "bomb", "kill", "steal",
]
