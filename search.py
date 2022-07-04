from index import index

class search:

    
    
   
    index = index()

    def searchKeyword(self, searchTxt, container):
        keywords = []
        keywordLinks = dict()
        keywordDict = dict()
        searchTxtResults = dict()
        keywords = self.index.analyze(searchTxt)
        for keyword in keywords: 

            keywordResults = container.query_items(
            query='SELECT Index.reverseIndex FROM Index WHERE Index.id = @keyword',
                        parameters=[dict(name="@keyword", value= keyword )],
                        enable_cross_partition_query=True)
            for result in keywordResults:
                keywordLinks = result['reverseIndex']
                sortedResults = dict()
                sortedResults = sorted(keywordLinks.items(), key=lambda x: x[1])
                i = 1
                for k in sortedResults:
                    keywordDict[k[0]] = i
                    if sortedResults.index(k)+1 < len(sortedResults):
                        if(k[1] < sortedResults[sortedResults.index(k)+1][1]):
                            i += 1
                    if k[0] in searchTxtResults:
                        searchTxtResults[k[0]] = searchTxtResults.get(k[0]) + keywordDict.get(k[0])
                    else:
                        searchTxtResults[k[0]] = keywordDict.get(k[0])
        
        return sorted(searchTxtResults.items(), key=lambda y: y[1])