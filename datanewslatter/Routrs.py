from ApiJasonN import Api
from flask import Flask
import json

app = Flask(__name__)

@app.route('/api')
def Homepage():
    return 'Api page'

@app.route('/api/ecnomy')
def economy():
    notice = Api(addrs='https://g1.globo.com/educacao/', classnamed='feed-media-wrapper', atribut='div')
    dicty = {
        'id': 'random',
        'notice': f'{notice}'
    }

    jsonfile= json.dumps(dicty, indent=2)
    return jsonfile

app.run()