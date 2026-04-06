import feedparser
import logging
from typing import List, Tuple

logger = logging.getLogger(__name__)

def fetch_rss_feed(feed_url: str) -> List[Tuple[str, str]]:
    """Fetch and parse the RSS feed."""
    try:
        feed = feedparser.parse(feed_url)
        if not feed.entries:
            logger.warning(f"No posts found in the feed: {feed_url}")
            return []
        return [(entry.title, entry.link) for entry in feed.entries]
    except Exception as e:
        logger.error(f"Failed to parse RSS feed {feed_url}: {e}")
        return []