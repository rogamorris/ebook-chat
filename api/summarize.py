import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text, max_tokens=100):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes text."},
            {"role": "user", "content": f"Please provide a detailed but concise summary of the following text:\n\n{text}. Ignore any HTML, code, SVGs, and images."}
        ],
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.5,
    )

    summary = response.choices[0].message["content"].strip()
    return summary