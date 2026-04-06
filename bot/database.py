import sqlite3
from typing import Set, List, Tuple

def init_db():
    """Initialize the SQLite database."""
    with sqlite3.connect("rss_bot.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS seen_posts (
                post_id TEXT PRIMARY KEY,
                feed_url TEXT NOT NULL
            )
        ''')
        conn.commit()

def get_seen_posts(feed_url: str) -> Set[str]:
    """Retrieve previously seen post IDs for a specific feed."""
    with sqlite3.connect("rss_bot.db") as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT post_id FROM seen_posts WHERE feed_url = ?', (feed_url,))
        return {row[0] for row in cursor.fetchall()}

def save_seen_posts(posts: List[Tuple[str, str]]) -> None:
    """Save seen post IDs to the database."""
    with sqlite3.connect("rss_bot.db") as conn:
        cursor = conn.cursor()
        cursor.executemany(
            'INSERT OR IGNORE INTO seen_posts (post_id, feed_url) VALUES (?, ?)',
            posts
        )
        conn.commit()