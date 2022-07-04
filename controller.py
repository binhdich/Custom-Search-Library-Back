
from flask import Flask, jsonify, request, render_template
from dbConnector import dbConnector
from index import index
from search import search
from parser import parser
app = Flask(__name__)

@app.route('/')
def home():

    return render_template('search.html')

@app.route('/indexurl', methods=['POST'])
def index_url():
    flask_url = request.form['indexUrl']
    flask_url_name = request.form['indexName']
    db = dbConnector()
    i = index()
    container = db.create_container(flask_url_name)
    pars = parser()
    i.index_doc(container, pars.parse_urls(flask_url))
    return("successful")


@app.route('/search', methods=['GET','POST'] )
def search_index():
    flask_search = request.form['searchTerm']
    flask_search_idx = request.form['searchIndexName']
    db = dbConnector()
    s = search()
    container = db.create_container(flask_search_idx)
    print(s.searchKeyword(flask_search,container))
    return jsonify(s.searchKeyword(flask_search,container))
   
if __name__ == '__main__':
    app.run(debug=True, threaded=True)




