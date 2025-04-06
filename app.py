from flask import Flask, render_template, request
from src.document_processor import extract_text_from_pdfs
from src.query_engine import QueryEngine

app = Flask(__name__)
qe = QueryEngine()

@app.before_first_request
def load_knowledge_base():
    docs = extract_text_from_pdfs('pdfs')
    qe.build_knowledge_base(docs)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ""
    if request.method == 'POST':
        question = request.form['question']
        results = qe.query(question)
        response = "<br>".join(results)
    return render_template('index.html', response=response)
