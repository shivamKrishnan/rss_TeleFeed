import requests
import logging
from config import BOT_TOKEN, CHAT_ID

logger = logging.getLogger(__name__)
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def send_telegram_message(message: str) -> None:
    """Send a message to Telegram."""
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        response = requests.post(TELEGRAM_URL, data=payload)
        response.raise_for_status()
        logger.info("Message sent to Telegram successfully.")
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to send message to Telegram: {e}")