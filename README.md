# blob_reddit – Personal Reddit Automation Script

This repository contains a small, non-commercial Python script that connects to
the Reddit Data API to automate **posting from my own account** and to retrieve
basic **engagement information** (comments, mentions, and inbox replies) about
my own submissions.

The project is designed for **low-volume, personal use only**, in a small number
of subreddits where I am already an active participant. It follows Reddit’s:

- Responsible Builder Policy  
- Developer Terms  
- Data API Terms  
- Reddit Content Policy  
- Bots and Automated Activity guidelines  

## Purpose

The script helps me:

1. Publish posts from my personal account into a few subreddits where I
   already post manually.
2. Retrieve basic metrics about my posts (score, number of comments) and
   read mentions/replies to my username from my inbox.

It is **not** a commercial product, and it is **not** used for:

- data resale or licensing  
- large-scale scraping  
- machine learning or model training  
- advertising or analytics pipelines  

All data stays under my personal control.

## How it works (high-level)

The script uses [PRAW](https://praw.readthedocs.io/) (Python Reddit API Wrapper)
to:

1. Authenticate with Reddit via OAuth using credentials stored locally in a
   configuration file (`config.ini`, which is **not** committed to this
   repository).
2. Provide simple functions to:
   - create a text post in a configured subreddit;
   - fetch basic engagement information (score, number of comments) for
     my recent submissions;  
   - read mentions and replies from my inbox.

Only content that is already visible to my account in the normal Reddit UI is
accessed.

## Installation (local use)

```bash
git clone https://github.com/cbsantos/blob_reddit.git
cd blob_reddit
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
