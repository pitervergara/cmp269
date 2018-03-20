#!/bin/python
import re
import os
from datetime import datetime
from pprint import pprint
from solr import index_docs



def parse_doc(doc_as_string):
    # print(doc_as_string)

    doc_tpl = {
        'DOCNO': 'docno_s',
        'DOCID': 'docid_s',
        'DATE': 'date_dt',
        'CATEGORY': 'category_s',
        'TEXT': 'text_txt',
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
            value = match.group(1)
            value = value.replace("\n", "")

            if key == 'DATE':
                date_obj = datetime.strptime(value, '%y%m%d')
                solr_date_str = date_obj.strftime("%Y-%m-%dT%H:%m:%S")
                value = solr_date_str

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
            if (line) == '</DOC>\n':
                doc_as_string += line
                
                doc = parse_doc(doc_as_string)
                docs.append(doc)

                doc_as_string = ""
            else:
                doc_as_string += line

            line = file.readline()

    return docs


def main():
    BASE_PATH = './FSP95'

    files = os.listdir(BASE_PATH)

    for fpath in files:
        docs = parse_file(os.path.join(BASE_PATH, fpath))
        
        #pprint(docs)
        ret = index_docs(docs)
        print("Indexados %d docs do arquivo %s" % (len(docs), fpath))

main()