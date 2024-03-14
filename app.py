from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Use an environment variable for the OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.json
    text = data.get('text')
    
    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        response = openai.Completion.create(
          model="gpt-3.5-turbo",
          prompt=f"Summarize this for a helpdesk support context:\n{text}",
          temperature=0.5,
          max_tokens=150
        )

        summary = response.choices[0].text.strip()
        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
