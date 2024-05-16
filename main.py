import re

import nltk

from utils.settings import BASE_DIR, doc_paths
from utils.helpers import process_document

document_separator_regex = re.compile(r"\*{40}")
documents: list = []

for doc_path in doc_paths:
    with open(     
        file=BASE_DIR / 'dataset' / doc_path,
        mode='r',
        encoding='utf-8'
    ) as file:
        
        current_document_lines = []
        for line in file:
            # Check if the line is the separator between documents
            if document_separator_regex.match(line):
                # Process the completed document
                documents.append(process_document(current_document_lines))
                # Reset the current document lines
                current_document_lines = []
            else:
                current_document_lines.append(line)

    if current_document_lines:
        documents.append(process_document(current_document_lines))

for i in documents:
    print(i)
