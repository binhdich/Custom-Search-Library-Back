import unittest
from parser import Document

from dbConnector import dbConnector
from index import index
from search import search

class TestSearch(unittest.TestCase):
    db = dbConnector()
    i = index()
    s = search()

    testContainer = db.create_container("testSearchIndex")

    testDoc1 = Document()
    testDoc1.url = "test1.url"
    testDoc1.content = "a b c"

    testDoc2 = Document()
    testDoc2.url = "test2.url"
    testDoc2.content = "b b c"
    
    testDoc3 = Document()
    testDoc3.url = "test3.url"
    testDoc3.content = "c"

    def test_single_search(self):

        self.i.index_doc(self.testContainer, self.testDoc1)
        self.i.index_doc(self.testContainer, self.testDoc2)
        self.i.index_doc(self.testContainer, self.testDoc3)

        result = self.s.searchKeyword("a", self.testContainer)
        self.assertEquals(result, [("test1.url", 1)])

    def test_ranked_search(self):

        self.i.index_doc(self.testContainer, self.testDoc1)
        self.i.index_doc(self.testContainer, self.testDoc2)
        self.i.index_doc(self.testContainer, self.testDoc3)

        result = self.s.searchKeyword("a b c", self.testContainer)
        self.assertEquals(result, [('test3.url', 1), ('test1.url', 3), ('test2.url', 3)])

if __name__ == '__main__':
    unittest.main()

