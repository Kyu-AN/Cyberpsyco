import re

def clean_keywords(keywords):
    cleaned = []

    for kw in keywords:

        kw = kw.lower()
        kw = re.sub(r"[^a-z0-9\s]", "", kw)
        kw = kw.strip()


        if len(kw) < 2:
            continue

        cleaned.append(kw)

    cleaned = list(dict.fromkeys(cleaned))

    return cleaned