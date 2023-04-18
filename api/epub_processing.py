from ebooklib import epub, ITEM_DOCUMENT
from summarize import summarize_text

def process_epub(file_path):
    book = epub.read_epub(file_path)
    content = ""

    for item in book.get_items():
        if item.get_type() == ITEM_DOCUMENT:
            content += item.get_content().decode('utf-8')

    summary = summarize_text(content)
    return summary
