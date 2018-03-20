import pysolr
import logging




SOLR_URL = 'http://solr:8983/solr/cmp269'
si = pysolr.Solr(SOLR_URL)


def index_docs(docs):
    if not isinstance(docs, list):
        docs = [docs, ]
    
    ret = si.add(docs)

    return ret


def remove_docs(query):
    ret = si.delete(q=query)
    return ret


def query_docs(query):
    
    fq = [
        'text_txt:"%s"' % query
    ]
    
    ret = si.search(q="*:*", fq=fq)
    
    return ret
