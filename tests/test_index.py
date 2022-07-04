import unittest

from dbConnector import dbConnector
from parser import Document
from index import index


class TestIndex(unittest.TestCase):

    db = dbConnector()
    i = index()
    testContainer = db.create_container("testIndex")

    def test_unique_doc(self):
        testDoc = Document()
        testDoc.url = "test1.url"
        testDoc.content = "abc def ghi"
        result = dict()
        self.i.index_doc(self.testContainer, testDoc)
        testDocAdded = self.testContainer.query_items(
        query='SELECT testIndex.reverseIndex FROM testIndex WHERE testIndex.id = "abc"',
        enable_cross_partition_query=True)
        for doc in testDocAdded:
            result = doc.get("reverseIndex")
        self.assertEquals(result.get("test1.url"), 1)
    
    def test_duplicate_token(self):
        testDoc = Document()
        testDoc.url = "test1.url"
        testDoc.content = "abc abc def"
        result = dict()
        self.i.index_doc(self.testContainer, testDoc)
        testDocAdded = self.testContainer.query_items(
        query='SELECT testIndex.reverseIndex FROM testIndex WHERE testIndex.id = "abc"',
        enable_cross_partition_query=True)
        for doc in testDocAdded:
            result = doc.get("reverseIndex")
        self.assertEquals(result.get("test1.url"), 2)
    
    def test_multiple_url(self):
        testDoc = Document()
        testDoc.url = "test1.url"
        testDoc.content = "abc def ghi"
        testDoc2 = Document()
        testDoc2.url = "test2.url"
        testDoc2.content = "abc def ghi"
        result = dict()
        self.i.index_doc(self.testContainer, testDoc)
        self.i.index_doc(self.testContainer, testDoc2)
        testDocAdded = self.testContainer.query_items(
        query='SELECT testIndex.reverseIndex FROM testIndex WHERE testIndex.id = "abc"',
        enable_cross_partition_query=True)
        for doc in testDocAdded:
            result = doc.get("reverseIndex")  
        self.assertTrue("test1.url" in result and "test2.url" in result)
    
    def test_tokenize(self):
        testText = "abc def ghi"
        words = self.i.tokenize(testText)
        checkWords = ["abc", "def", "ghi"]
        self.assertEquals(words, checkWords)

    def test_lowercase_filter(self):
        testText = ["aBc", "DeF", "ghi"]
        words = self.i.lowercase_filter(testText)
        checkWords = ["abc", "def", "ghi"]
        self.assertEquals(words, checkWords)

    def test_stem_filter(self):
        testText = ["likes", "liked", "likely", "program", "programs", "programming"]
        words = self.i.stem_filter(testText)
        checkWords = ["like", "like", "like", "program","program","program"]
        self.assertEquals(words, checkWords)

    def test_punctuation_filter(self):
        testText = ["abc.", "def", "ghi."]
        words = self.i.punctuation_filter(testText)
        checkWords = ["abc", "def", "ghi"]
        self.assertEquals(words, checkWords)
    
    def test_stopword_filter(self):
        testText = ["abc", "def", "ghi"]
        stopwords = ["abc", "ghi"]
        words = self.i.stopword_filter(testText, stopwords)
        checkWords = ["def"]
        self.assertEquals(words, checkWords)

    def test_analyze(self):
        testText = ("LiKes \n liked. program ProGrams." )
        words = self.i.analyze(testText)
        checkWords = ["like", "like", "program", "program"]
        self.assertEquals(words, checkWords)

if __name__ == '__main__':
    unittest.main()
