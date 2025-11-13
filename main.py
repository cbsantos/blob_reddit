"""
blob_reddit – Personal Reddit Automation Script

This is a small, non-commercial script that connects to the Reddit Data API
(using PRAW) in order to:

- post from my own account into a small number of subreddits where I already
  participate; and
- retrieve basic engagement information (scores, comments) and mentions/replies
  related to my own submissions.

All usage is low-volume and in compliance with Reddit’s Responsible Builder
Policy, Developer Terms, Data API Terms, and Content Policy.

Real credentials are kept locally in config.ini (which is NOT committed to the
repository).
"""

import configparser
import pathlib
from typing import Optional

import praw


CONFIG_PATH = pathlib.Path(__file__).parent / "config.ini"


def load_config(path: pathlib.Path = CONFIG_PATH) -> configparser.ConfigParser:
    """
    Load local configuration file (not committed to the repo).
    """
    config = configparser.ConfigParser()
    if not path.exists():
        raise FileNotFoundError(
            f"Config file '{path}' not found. "
            "Create it based on 'config.example.ini'."
        )
    config.read(path)
    return config


def get_reddit_instance(config: Optional[configparser.ConfigParser] = None) -> praw.Reddit:
    """
    Create an authenticated Reddit instance using PRAW.

    This function uses only locally stored credentials and is intended for
    low-volume, personal use, in compliance with Reddit policies.
    """
    if config is None:
        config = load_config()

    cfg = config["reddit"]

    reddit = praw.Reddit(
        client_id=cfg["client_id"],
        client_secret=cfg["client_secret"],
        username=cfg["username"],
        password=cfg["password"],
        user_agent=cfg["user_agent"],
    )

    return reddit


def main() -> None:
    """
    Placeholder entry point.

    For now, this function just tests the connection and prints the current
    authenticated user. The actual logic will perform simple, personal account
    automation such as:

    - creating a text post in one of my allowed subreddits; and
    - reading basic engagement / mentions related to my posts.
    """
    try:
        reddit = get_reddit_instance()
        me = reddit.user.me()
        print(f"Authenticated as: {me}")
        print(
            "This is a placeholder. Actual posting and data retrieval logic "
            "will remain low-volume and aligned with Reddit’s policies."
        )
    except FileNotFoundError as e:
        print(e)
        print("Please create 'config.ini' based on 'config.example.ini'.")
    except Exception as e:
        print("Error while connecting to Reddit:", e)


if __name__ == "__main__":
    main()
