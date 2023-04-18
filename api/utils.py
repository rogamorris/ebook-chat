import os
from ebooklib import epub

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def validate_epub(file_path):
    try:
        epub.read_epub(file_path)
        return True
    except:
        return False

def file_size(file, max_size):
    return os.fstat(file.fileno()).st_size <= max_size
