from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import re
import string






class index:

    STOPWORDS = set(['\n'])
    PUNCTUATION = re.compile('[%s]' % re.escape(string.punctuation))
    ps = PorterStemmer()

    def tokenize(self, text):
        words = word_tokenize(text)
        return words

    def lowercase_filter(self, tokens):
        return [token.lower() for token in tokens]

    def stem_filter(self, tokens):
        return [self.ps.stem(token) for token in tokens]
    
    def punctuation_filter(self, tokens):
        return [self.PUNCTUATION.sub('', token) for token in tokens]

    def stopword_filter(self, tokens, stopwords):
        return [token for token in tokens if token not in stopwords]

    def analyze(self, text):
        tokens = self.tokenize(text)
        tokens = self.lowercase_filter(tokens)
        tokens = self.punctuation_filter(tokens)
        tokens = self.stopword_filter(tokens, self.STOPWORDS)
        tokens = self.stem_filter(tokens)
        return [token for token in tokens if token]

    def index_doc(self, container, document):

        tokensAddedLst = []
        reverseIndexDict = dict()

        tokensAdded = container.query_items(
        query='SELECT Index.id FROM Index',
        enable_cross_partition_query=True)

        for item in tokensAdded:
            tokensAddedLst.append(item['id'])
        tokensLst = self.analyze(document.content)
        tokensSet = set(tokensLst)

        for token in tokensSet:
            if token not in tokensAddedLst:
                reverseIndex = dict()
                reverseIndex[document.url] = tokensLst.count(token)    
                container.upsert_item({'id' : token,
                                        'url': 'test',
                                        'reverseIndex': reverseIndex})
            else:
                reverseIndex = container.query_items(
                        query='SELECT Index.reverseIndex FROM Index WHERE Index.id = @token',
                        parameters=[dict(name="@token", value= token )],
                        enable_cross_partition_query=True)

                for item in reverseIndex:
                    reverseIndexDict = item['reverseIndex']
                    print(reverseIndexDict)
                    reverseIndexDict[document.url] = tokensLst.count(token)
                    container.upsert_item({'id' : token,
                                        'url': 'test',
                                        'reverseIndex': reverseIndexDict})









