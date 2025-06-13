from openai import OpenAI
from APIkey import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_query(keywords):
    prompt = (
        f"Using the keywords: {', '.join(keywords)}, "
        "generate a short, natural English search sentence that would return well-known or popular songs on Spotify. "
        "Avoid niche or obscure terms. Focus on mood, genre, or theme to guide the search.\n"
        "Only return the sentence, no explanations."
        )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content
