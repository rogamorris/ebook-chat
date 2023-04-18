from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, request
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import os
from utils import allowed_file, validate_epub, file_size
from epub_processing import process_epub

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

api = Api(app)

class Upload(Resource):
    @cross_origin()
    def post(self):
        if 'file' not in request.files:
            return {'error': 'No file provided'}, 400

        file = request.files['file']
        filename = secure_filename(file.filename)

        # Check if the file has the allowed format
        if not allowed_file(filename, {'epub'}):
            return {'error': 'Invalid file format. Only EPUB files are accepted.'}, 400

        # Check if the file size is within the limit
        max_size = 15 * 1024 * 1024  # 15 MB
        if not file_size(file, max_size):
            return {'error': 'File size exceeds the maximum limit of 15 MB.'}, 400

        file.save(os.path.join('uploads', filename))
        print("File saved:", filename)

       # Check if the file is a valid EPUB file
        if not validate_epub(os.path.join('uploads', filename)):
            os.remove(os.path.join('uploads', filename))
            return {'error': 'Invalid EPUB file. It may be unreadable due to DRM protection or missing/corrupt data.'}, 400

        try:
            summary = process_epub(os.path.join('uploads', filename))
            print("Summary:", summary)
        except Exception as e:
            print("Error processing EPUB:", e)
            return {'error': 'Failed to process the EPUB file.'}, 500

        return {'message': 'File uploaded and summarized successfully.', 'summary': summary}, 200


api.add_resource(Upload, '/upload')

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True, host='0.0.0.0', port=5000)

