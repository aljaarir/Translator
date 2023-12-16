# Text Translator Web App

This is a simple web application that allows users to translate text using the Microsoft Translator API.

## Features

- Translate text to different languages.
- Easy-to-use web interface.
- Powered by Azure , Microsoft Translator API.

## Technologies Used

- Python
- Flask (Web Framework)
- Microsoft Translator API
- HTML, CSS (for frontend)

## Setup

1. Clone the repository: `git clone https://github.com/aljaarir/Translator.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables:
   - Create a `.env` file in the project root.
   - Add the following content and replace with your API key and endpoint:
     ```
     KEY=your_translation_api_key
     ENDPOINT=your_translation_api_endpoint
     LOCATION=your_translation_api_region
     ```
4. Run the application: `python app.py`
5. Open your browser and navigate to http://localhost:5000 to use the app.

