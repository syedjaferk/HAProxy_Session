from flask import Flask, send_from_directory
 
app = Flask(__name__)
 
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)