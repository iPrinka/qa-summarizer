import transformers
import streamlit as st
from comments import fetch_comments
from utils import text_to_chunks, summarize_chunk

st.title("Reddit Threads Summarizer")

st.write(
    "Use this tool to generate summaries from Reddit threads."
    "The Tool uses OpenAI's APIs to generate the summaries."
)
st.write(
    "The app is currently a POC. It extracts comments from the given reddit article, "
    "chunks the text, summarizes it and then returns the same."
)

st.write()

left, right = st.columns(2)
form = left.form("template_form")

url_input = form.text_input(
    "Enter Reddit article/submission link",
    placeholder="",
    value="",
)

submit = form.form_submit_button("Get Summary")

with st.container():
    if submit and url_input:
        with st.spinner("Fetching Summary..."):
            text = fetch_comments(url_input)
            tokenizer = transformers.GPT2TokenizerFast.from_pretrained("gpt2")
            chunks = text_to_chunks(text, tokenizer)

            summaries = ""
            for chunk in chunks:
                summary = summarize_chunk(chunk)
                summaries = summaries + summary

            final_summary = summarize_chunk(summaries)

            with right:
                right.write(f"{final_summary}")