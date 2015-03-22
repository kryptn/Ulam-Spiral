from flask import Flask, render_template, send_from_directory, Response
from flask.ext import restful
from spiral import Spiral
import json

app = Flask(__name__)
api = restful.Api(app)
spiral = Spiral()

@app.route('/')
def index():
    return render_template('base.html')


class SpiralClient(restful.Resource):

    def get(self, zoom, x, y):
        #import pdb; pdb.set_trace()
        value = spiral.position(int(x),int(y))
        
        if zoom == "position":
            data = value
        else:
            if spiral.tempprime(value):
                data = 'black'
            else:
                data = 'white'
        
        r = Response(response=json.dumps({'data':data}), status=200, mimetype="application/json")
        return r 



api.add_resource(SpiralClient, '/api/<string:zoom>/<string:x>/<string:y>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
