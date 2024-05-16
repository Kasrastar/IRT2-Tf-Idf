from copy import copy

from utils.documents import Document


def process_document(document_lines: list[str]):
    try:
        return copy(Document(document_lines))
    except IndexError:
        print(document_lines)
        raise 
    except ValueError:
        print(document_lines)
        raise

