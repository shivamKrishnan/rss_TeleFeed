Here you go—clean, copy-ready `README.md` Markdown:

````markdown
# RSS-to-Telegram Bot

A Python-based bot that fetches updates from RSS feeds and sends them as alerts to a Telegram chat. Built with Flask and SQLite for simplicity and reliability.

---

## 🌟 Features

- **RSS Feed Monitoring**: Fetches updates from multiple RSS feeds.
- **Telegram Alerts**: Sends new posts as messages to a Telegram chat.
- **Avoid Duplicates**: Tracks seen posts using SQLite to avoid sending duplicates.
- **Web Interface**: Simple UI to add, remove, and manage RSS feeds.
- **Automated Checks**: Runs on a schedule (e.g., every hour) to check for new posts.

---

## 📋 Prerequisites

- **Python 3.8+**
- **SQLite** (included with Python)
- **Telegram Bot Token** (Get it from [BotFather](https://t.me/BotFather))
- **Telegram Chat ID** (Get it using the instructions below)

---

## 🛠 Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/rss-telegram-bot.git
cd rss-telegram-bot
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the Bot

#### Add Telegram API Token and Chat ID

1. Open `config.py`.
2. Replace `your_bot_token_here` and `your_chat_id_here` with your actual Telegram bot token and chat ID.

```python
# config.py
BOT_TOKEN = "your_bot_token_here"
CHAT_ID = "your_chat_id_here"
```

#### How to Get a Telegram Bot Token and Chat ID

1. **Create a Telegram Bot**:

   * Open Telegram and search for **BotFather**.
   * Send `/newbot` and follow the instructions to create a new bot.
   * Copy the API token provided by BotFather.

2. **Get Your Chat ID**:

   * Send a message to your bot.
   * Visit:

     ```
     https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
     ```
   * Look for:

     ```json
     "chat":{"id":-XXXXXX}
     ```

     This is your chat ID.

---

## 🚀 Running the Bot

### 1. Start the Flask App

```bash
python app.py
```

### 2. Access the Web Interface

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 📱 Usage

### Web Interface

* **Add a Feed**: Enter the RSS feed URL and click "Add Feed".
* **Remove a Feed**: Click the "Remove" button next to the feed you want to remove.
* **Check for New Posts**: Click the "Check for New Posts" button to manually trigger a check.

### Scheduler

The bot automatically checks for new posts every hour.

To change the interval, modify:

```python
schedule.every(1).hour.do(check_feeds)
```

in `app.py`.

---

## 🗃 Database

The bot uses **SQLite** to track seen posts and avoid duplicates.

The database file:

```
rss_bot.db
```

will be created automatically in the project directory.

---

## 🌐 Deployment

### Running on a Server

You can deploy the bot to:

* **Heroku**
* **AWS Lambda**
* **Google Cloud Run**

### Using Cron (Linux/macOS)

```bash
crontab -e
```

Add:

```bash
0 * * * * cd /path/to/your/bot && /usr/bin/python3 /path/to/your/bot/app.py >> /path/to/your/bot/cron.log 2>&1
```

### Using Task Scheduler (Windows)

1. Open Task Scheduler
2. Create a new task
3. Set it to run:

```bash
python app.py
```

every hour.

---

## 🤝 Contributing

Contributions are welcome!
Fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.

