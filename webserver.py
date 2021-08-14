from flask import Flask
import requests
from flask.ctx import has_app_context
from flask.signals import request_finished


app = Flask(__name__)

import markdown
@app.route("/")
def index():
    """Some Documentation"""

    # Open the ReadMe File
    #with open(os.path.dirname(app.root_path) + '/README.md', 'r' ) as markdown_file:
    with open('/home/pi/Desktop/API_Project/README-2.md', 'r' ) as markdown_file:
        content = markdown_file.read()

        return markdown.markdown(content)

@app.route("/on")
def on():
    with open('text.txt', 'w') as f:
        f.write("1")
        f.close()
    return "ON"


@app.route("/off")
def off():
    with open('text.txt', 'w') as f:
        f.write("0")
        f.close()
    return "OFF"

@app.route('/api/rgb', methods=['GET'])
def api_rgb():
    if 'rgb' in requests.args:
        id = int(requests.args['rgb'])
        print(id)
        return "hello"
    else:
        return "Error: No id field provided. Please specify an rgb."
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 402, debug = True)


