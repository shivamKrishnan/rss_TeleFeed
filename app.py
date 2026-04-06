from flask import Flask, render_template, request, redirect, url_for
from bot.database import init_db, get_seen_posts, save_seen_posts
from bot.rss_fetcher import fetch_rss_feed
from bot.telegram_bot import send_telegram_message
from config import DEFAULT_RSS_FEEDS
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Initialize the database
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_feed = request.form.get("rss_feed")
        if new_feed:
            DEFAULT_RSS_FEEDS.append(new_feed)
    return render_template("index.html", feeds=DEFAULT_RSS_FEEDS)

@app.route("/remove_feed/<int:index>", methods=["GET"])
def remove_feed(index):
    if 0 <= index < len(DEFAULT_RSS_FEEDS):
        DEFAULT_RSS_FEEDS.pop(index)
    return redirect(url_for("index"))

@app.route("/check_feeds", methods=["GET"])
def check_feeds():
    new_posts = []
    for feed_url in DEFAULT_RSS_FEEDS:
        seen_posts = get_seen_posts(feed_url)
        posts = fetch_rss_feed(feed_url)
        for title, link in posts:
            if link not in seen_posts:
                new_posts.append((title, link, feed_url))

    if new_posts:
        for title, link, feed_url in new_posts:
            send_telegram_message(f"🎉 New Post Alert!\n\n{title}\n{link}")
        save_seen_posts([(post[1], post[2]) for post in new_posts])
        return "New posts found and sent to Telegram!"
    else:
        send_telegram_message("No new posts found.")
        return "No new posts found."

if __name__ == "__main__":
    app.run(debug=True)