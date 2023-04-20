# Reddit Threads Summarizer

Please find my Streamlit app hosted [here](https://iprinka-comments-summary-ml-project-app-xobtj4.streamlit.app/)
<br/>
Please note that if you face an error, the Open AI API credits on my account might have expired :D

## Project Summary

The goal of this model is to provide a summary of comment threads for any given Reddit article/submission link.

## Approach

* In this project, I will be using [Reddit API](https://www.reddit.com/dev/api) to fetch all comment threads for any given Reddit article/submission.
* I used [Streamlit](https://streamlit.io/) to build this application. It takes a Reddit article url as input. Using the Reddit API, I fetch all the comment threads under that article and provide it to the Tokenizer to break the text into chunks.
* Then I provide each chunk as an input to the [Completions API](https://platform.openai.com/docs/guides/completion/introduction) with the prompt - `Provide a summary of the comments below.`followed by the chunk of comments. The model then returns a brief summary of how people are reacting to that video.

## How to use

1. Create a virtual environment (python3 -m venv venv && source venv/bin/activate)

2. Download all the dependencies by running `make requirements` in your terminal

3. Create a project on Reddit Developers platform. Follow this article [here.](https://towardsdatascience.com/how-to-use-the-reddit-api-in-python-5e05ddfd1e5c)

4. Create a .streamlit folder at the source level and add a secrets.toml file to it.

5. Ensure your Reddit API keys are set in the secrets.toml file (check the secrets.toml.example file for reference). Please find the details to generate the API key in the article mentioned above.

6. Ensure your OpenAI API key is set as an environment variable in the secrets.toml file (check the secrets.toml.example file for reference).

7. Run the [streamlit](https://streamlit.io/) app by running `make run`

8. Open the app in your browser at `http://localhost:8501`

## Example

![alt text](https://github.com/iPrinka/qa-summarizer/blob/main/assets/reddit-summarizer.png?raw=true)
