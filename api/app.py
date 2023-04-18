from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

api = Api(app)

class Upload(Resource):
    def post(self):
        if 'file' not in request.files:
            return {'error': 'No file provided'}, 400

        file = request.files['file']
        filename = secure_filename(file.filename)

        if not filename.lower().endswith('.epub'):
            return {'error': 'Invalid file format. Only EPUB files are accepted.'}, 400

        file.save(os.path.join('uploads', filename))
        return {'message': 'File uploaded successfully'}, 200

api.add_resource(Upload, '/upload')

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True, host='0.0.0.0', port=5000)

