from flask import Flask, request, render_template
import json
from vision import detect

app = Flask(__name__)

@app.route('/')
def index():
    data={"sonic1":0.00,"sonic2":1.00}
    return render_template('index.html', data=data)

@app.route('/test')
def test():
    return {"test":"hello world"}
@app.route('/upload', methods=['POST'])
def upload():
    #print entire request
    print(request)
    file = request.data
    with open('file.jpg','wb') as f:
        f.write(file)
    detect('file.jpg')
    
    return 'File uploaded successfully', 200

@app.route('/distance', methods=['GET'])
def distance():
    data = request.args
    #print sonic1 & sonic2 from payload
    payload = json.loads(data['payload'])
    print('\n\tSonic 1',payload['sonic1'])
    print('\tSonic 2',payload['sonic2'])
    return "200"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)