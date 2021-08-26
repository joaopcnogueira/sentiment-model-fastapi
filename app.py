import gradio as gr
from vader import SentimentScore


# def get_polarity_score(text):
#     analyzer = SentimentIntensityAnalyzer()
#     polarity_score = analyzer.polarity_scores(text)['compound']
#     return polarity_score

interface = gr.Interface(
    fn=SentimentScore.get, 
    inputs=gr.inputs.Textbox(lines=2, placeholder="Escreva aqui..."), 
    outputs=["number"],
    title="Análise de Sentimentos",
    article="""<div>
    <p>Digite o texto na caixa <b>TEXT</b> e clique no botão <b>Submit</b>. </p>
    <p>Na caixa <b>OUTPUT</b> irá aparecer o score de sentimento associado ao texto, que pode variar de <b>-1</b> (<i>sentimento negativo</i>)
    até <b>1</b> (<i>sentimento positivo</i>). <b>0</b> significa <i>sentimento neutro</i>.</p>
    </div>"""
)
interface.launch(share=True)
