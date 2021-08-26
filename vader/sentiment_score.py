from .leia import SentimentIntensityAnalyzer

class SentimentScore:

    @staticmethod
    def get(text):
        analyzer = SentimentIntensityAnalyzer()
        polarity_score = analyzer.polarity_scores(text)['compound']
        return polarity_score
