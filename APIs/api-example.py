from flask import Flask, request

# create the flask routing object
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """

    To url's with the following extension, '/', they are only allowed to
    accept GET requests.

    Whenever a GET request is sent here, 'Hello World' is returned.

    :return:
    """
    return '''Hello World'''


@app.route('/post-example', methods=['POST'])
def post_example():
    """

    To url's with the following extension, '/post-example', they are only
    allowed to accept POST requests.

    Whenever a POST request is sent here, it checks to make sure that info
    was properly sent from the client and if so it will return that info,
    otherwise, it will return a message saying that the POST request failed.

    :return:
    """

    response = request.json

    if response is not None:
        return response

    return "Failed Post Request"


if __name__ == '__main__':
    """

    This function routes to the specified IP and port number:

    IP: 0.0.0.0
    port: 8080

    Note: Port 5000 is the default for Flask Apps.

    """
    app.run(debug=True, host='0.0.0.0', port='8080')
