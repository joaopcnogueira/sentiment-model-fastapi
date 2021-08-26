from .leia import SentimentIntensityAnalyzer

class SentimentScore:

    @staticmethod
    def get(text):
        analyzer = SentimentIntensityAnalyzer()

        polarity_score = analyzer.polarity_scores(text)['compound']

        if polarity_score >= 0.05:
            class_ = "success"
            sentiment = "positivo"
        elif polarity_score <= -0.05:
            class_ = "danger"
            sentiment = "negativo"
        else:
            class_ = "secondary"
            sentiment = "neutro"

        return {"score": polarity_score,
                "sentiment": sentiment,
                "class": class_}
