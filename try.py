def count_sentiments(reviews):
    count = {
        "positive": 0,
        "negative":0,
        "mixed":0,
        "neutral":0
    }
    for review in reviews:
        count[review["sentiment"]] += 1
    return count


print(count_sentiments(
[
  {"text": "The queue was terrible.", "sentiment": "negative"},
  {"text": "The app crashed right before I could finish my payment.", "sentiment": "negative"},
  {"text": "Customer support never replied to my emails.", "sentiment": "negative"},
  {"text": "Delivery arrived two days early and the packaging was spotless.", "sentiment": "positive"},
  {"text": "The new update makes navigating the menu effortless.", "sentiment": "positive"},
  {"text": "The food tasted amazing, though the service was painfully slow.", "sentiment": "mixed"}
]))