from flask import Flask
from flask.ext import restful
from spiral import Spiral

app = Flask(__name__)
api = restful.Api(app)
spiral = Spiral()

@app.route('/')
def index():
    return "Hihi"

class SpiralClient(restful.Resource):
    def get(self, x, y):
        pos = spiral.position(int(x),int(y))
        return {'x':x,'y':y,'n':pos}
        
api.add_resource(SpiralClient, '/api/<string:x>/<string:y>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')