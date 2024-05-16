class Document:    
    def __init__(self, document_lines: list[str]) -> None:
        self.id = document_lines[0].strip().split()[1]
        self.title = self.create_title(document_lines[1:])
        content_start_pos: int = self.find_index(document_lines) 
        self.content = self.create_content(document_lines[content_start_pos+1:])

    def create_title(self, document_lines: list[str]):
        title: str = ''
        for line in document_lines:
            if line == '\n':
                break
            title += line.strip() + ' '
        return title
    
    def create_content(self, document_lines: list[str]):
        content: str = ''
        for line in document_lines:
            content += line.strip()
        return content

    def find_index(self, document_lines: list[str]):
        i = 0
        for line in document_lines:
            if line.strip() ==  '\n':
                return i
            i+=1
        return i

    def __str__(self) -> str:
        return f'{self.id} {self.title} {self.content}'