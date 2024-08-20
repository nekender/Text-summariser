from flask import Flask, request, jsonify
import nltk
import re
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

def summarize_text(article_text):
    parser = PlaintextParser.from_string(article_text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, 3)
    summary_text = " ".join(str(sentence) for sentence in summary)
    return summary_text

def summarize_large_text(article_text, chunk_size=5000):
    chunks = [article_text[i:i+chunk_size] for i in range(0, len(article_text), chunk_size)]
    summaries = []
    for chunk in chunks:
        summaries.append(summarize_text(chunk))
    return " ".join(summaries)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    article_text = data.get('text', '')
    if not article_text:
        return jsonify({'summary': 'No text provided.'})
    summary = summarize_large_text(article_text)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
