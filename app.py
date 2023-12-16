# Importing the required libraries
import requests
import os
import uuid
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# code
@app.route('/', methods=['POST'])
def index_post():
    # Read the values from the form
    original_text = request.form.get('text')
    target_language = request.form.get('language')

    # Check if required form fields are present
    if not original_text or not target_language:
        error_message = "Error: Missing form fields"
        print(error_message)
        return render_template(
            'results.html',
            translated_text=error_message,
            original_text=original_text,
            target_language=target_language
        )

    # Load the values from .env
    key = os.environ.get('KEY')
    endpoint = os.environ.get('ENDPOINT')
    location = os.environ.get('LOCATION')

    # Check if environment variables are set
    if not key or not endpoint or not location:
        error_message = "Error: Missing environment variables"
        print(error_message)
        return render_template(
            'results.html',
            translated_text=error_message,
            original_text=original_text,
            target_language=target_language
        )

    # Indicate that we want to translate and the API version (3.0) and the target language
    path = '/translate?api-version=3.0'
    # Add the target language parameter
    target_language_parameter = '&to=' + target_language
    # Create the full URL
    constructed_url = endpoint + path + target_language_parameter

    # Set up the header information, which includes our subscription key
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # Create the body of the request with the text to be translated
    body = [{'text': original_text}]

    # Make the call using post
    translator_request = requests.post(constructed_url, headers=headers, json=body)

    # Check if the request was successful
    if translator_request.status_code != 200:
        error_message = f"Error: Translation request failed with status code {translator_request.status_code}"
        print(error_message)
        return render_template(
            'results.html',
            translated_text=error_message,
            original_text=original_text,
            target_language=target_language
        )

    # Retrieve the JSON response
    translator_response = translator_request.json()

    # Retrieve the translation
    translated_text = translator_response[0]['translations'][0]['text']

    # Call render template, passing the translated text,
    # original text, and target language to the template
    return render_template(
        'results.html',
        translated_text=translated_text,
        original_text=original_text,
        target_language=target_language
    )

if __name__ == '__main__':
    app.run(debug=True)
