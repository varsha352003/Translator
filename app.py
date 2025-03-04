from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    # Get the input text and target language from the form
    text_to_translate = request.form.get('text')
    target_language = request.form.get('language')
    
    # Perform the translation
    try:
        translated_text = GoogleTranslator(target=target_language).translate(text_to_translate)
        return render_template('index.html', translated_text=translated_text, original_text=text_to_translate)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run()
