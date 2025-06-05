import openai
from APIkey import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_parameters(keywords):
    prompt = (
        f"Given the keywords: {', '.join(keywords)}, "
        "analyze the overall mood and generate Spotify recommendation API parameters.\n"
        "Return only a JSON object including these keys: 'valence', 'energy', 'danceability', and 'acousticness'. "
        "Each value should be a float between 0.0 and 1.0.\n"
        "This JSON will be used directly as input for Spotify API, so be precise and concise.\n"
        "Example output: {\"valence\": 0.75, \"energy\": 0.65, \"danceability\": 0.7, \"acousticness\": 0.3}"
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return response['choices'][0]['message']['content']

def generate_query(keywords):
    prompt = (
        f"Create a natural and emotional English sentence for searching music on Spotify, based on the keywords: {', '.join(keywords)}.\n"
        "This sentence will be used as a direct query in the Spotify Search API.\n"
        "Keep it short, emotionally expressive, and suitable for searching songs.\n"
        "Example: 'A relaxing acoustic tune for a rainy evening'\n"
        "Output only the sentence, no explanation."
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response['choices'][0]['message']['content']
