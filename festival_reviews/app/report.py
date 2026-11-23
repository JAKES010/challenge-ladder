def count_sentiments(reviews):
    counts = {
        "positive": 0,
        "negative": 0,
        "neutral": 0,
        "mixed": 0
    }

    for review in reviews:
        sentiment = review["sentiment"]

        if sentiment in counts:
            counts[sentiment] += 1

    return counts