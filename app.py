from language import transalation_lang
from flask import Flask, request, jsonify
from langdetect import detect

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def post():
    posted_data = request.get_json()
    text = posted_data['text']
    output_language = posted_data['output_language']
    translation = transalation_lang(output_language,text)
    input_lang = detect(text)
    return jsonify({
        "text" : translation,
        "input_language":input_lang,
        "output_language":output_language
    })
# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"



if __name__ == '__main__':
    app.run(threaded=True, port=5000)
