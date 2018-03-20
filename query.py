#!/bin/python
import re
import os
from datetime import datetime
from pprint import pprint
from solr import query_docs



def parse_doc(doc_as_string):
    # print(doc_as_string)

    doc_tpl = {
        'num': 'num',
        'PT-title': 'title',
        'PT-desc': 'desc',
        'PT-narr': 'narr',
    }

    doc = {}

    for key in doc_tpl.keys():
        # generates something like:
        # str_pattern = ".*\<DOCID\>(.*)\<\/DOCID\>.*"
        str_pattern = ".*\<%s\>(.*)\<\/%s\>.*" % (key, key)

        # compiles pattern, capture match, updates doc
        re_pattern = re.compile(str_pattern, re.DOTALL)
        match = re_pattern.match(doc_as_string)
        
        if match:
            value = match.group(1).strip()
            solr_key = doc_tpl[key]
            doc.update({solr_key: value})

    # ensures we have all keys..
    for key in doc_tpl.values():
        assert(doc[key] is not None)

    return doc


def parse_file(fpath):
    '''Lê um arquivo linha a linha e separa os DOC dentro dele'''

    docs = []
    
    with open(fpath, encoding="iso-8859-1") as file:
        doc_as_string = ""

        line = file.readline()
        while (line):
            if (line) == '</top>\n':
                doc_as_string += line
                
                doc = parse_doc(doc_as_string)
                docs.append(doc)

                doc_as_string = ""
            else:
                doc_as_string += line

            line = file.readline()

    return docs


def main():

    queries = parse_file('Consultas.txt')
        
    # pprint(queries)
    # ret = index_docs(docs)
    # print("Indexados %d docs do arquivo %s" % (len(docs), fpath))

    for query in queries:
        terms = query["title"]
        result = query_docs(terms)
        # pprint(dir(result))
        print("Encontrados %d resultados para a busca '%s'" % (len(result.docs), terms))
        [ print(d["docno_s"]) for d in result.docs ]
        result = None

main()