from flask import Flask, render_template, jsonify
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
        value = spiral.position(int(x),int(y))
        
        r = {'position':value,
             'prime':spiral.tempprime(value)}
        
        return jsonify(results=r) 



api.add_resource(SpiralClient, '/api/<string:zoom>/<string:x>/<string:y>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
