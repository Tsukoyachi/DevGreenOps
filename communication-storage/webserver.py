from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def handle_request():
    # payload size
    content_length = request.content_length
    # header size
    headers = dict(request.headers)
    headers_size = sum(len(key) + len(value) for key, value in headers.items())
    # total size
    total_content_length = content_length + headers_size
    
    if total_content_length is None:
        return 'No content received', 400
    return f"Size of incoming request: {total_content_length} bytes", 200

if __name__ == '__main__':
    # Start the server on port 5000
    app.run(host='0.0.0.0', port=5000)
