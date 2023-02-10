from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    r=request.args
    name=r['name']
    data = {
        'apple': 15,
        'banana': 2,
        'orange': 5,
        'grape': 10
    }
    return {name:data.get(name,'Not Found')}

@app.route('/home')
def home():
    return 'Home Page!!'

@app.route('/sum')
def get_sum():
    a = request.args.get("a",0)
    b = request.args.get("b",0)
    return a + b

# This will run the app on http://localhost:5000
if __name__ == '__main__':
    # Run the app in local network
    app.run()
# get remote 