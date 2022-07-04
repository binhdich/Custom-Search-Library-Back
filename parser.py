from xml.dom.minidom import Document
from bs4 import BeautifulSoup
import requests


class parser:

    class Document:
        def __init__(self):
            self.url = str
            self.content = str

    def parse_urls(self, url):
        document = Document()  
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        document.url = url
        document.content = soup.text
        return document

    
