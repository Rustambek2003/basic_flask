from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    print('Hi')
    data = {
        'apple': 15,
        'banana': 2,
        'orange': 5,
        'grape': 10
    }
    return {'Ok':'Hello, World!'}

@app.route('/home')
def home():
    return 'Home Page!!'

# This will run the app on http://localhost:5000
if __name__ == '__main__':
    # Run the app in local network
    app.run(host='0.0.0.0', port=8080,debug=True)