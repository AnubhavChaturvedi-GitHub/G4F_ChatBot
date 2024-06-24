from flask import Flask, render_template, request, jsonify
from g4f.client import Client

def res(text):
    client = Client()
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": text}]
    )
    return (response.choices[0].message.content)

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        user_input = request.json['user-message']
        response = res(user_input)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
