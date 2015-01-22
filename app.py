from flask import Flask
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)

class SpiralClient(restful.Resource):
    def get(self, x, y):
        return {'x':x,'y':y}
        
api.add_resource(SpiralClient, '/<string:x>/<string:y>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')