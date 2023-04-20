import streamlit as st
import praw

from dotenv import load_dotenv

load_dotenv()

def setup_reddit():
    reddit = praw.Reddit(
        client_id=st.secrets['REDDIT_CLIENT_ID'],
        client_secret=st.secrets['REDDIT_SECRET_KEY'],
        user_agent=st.secrets['REDDIT_USER_AGENT'],
        username=st.secrets['REDDIT_USERNAME'],
        password=st.secrets['REDDIT_PASSWORD']
    )
    return reddit

def fetch_comments(url):
    all_comments = ""
    reddit = setup_reddit()
    submission = reddit.submission(url=url)
    submission.comments.replace_more(limit=100)

    for top_level_comment in submission.comments.list():
        all_comments = all_comments + top_level_comment.body+"\n"
    return all_comments