from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'Mi primera aplicacion con flask'


@app.route('/postjson', methods=['POST'])
def postJsonHandler():
    #print('Getting RAW data')
    # print(request.get_data())
    #print('Validate JSON Format')
    # print(request.get_json)
    content = request.get_json()
    print(content)
    return 'JSON POSTEADO'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
