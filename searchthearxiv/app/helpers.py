import json
from paper import Paper
from requests_html import HTMLSession
from collections import defaultdict
import sys

import pickle
import io
import torch
from sentence_transformers import util
import os

class CPU_Unpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == 'torch.storage' and name == '_load_from_bytes':
            return lambda b: torch.load(io.BytesIO(b), map_location='cpu')
        else:
            return super().find_class(module, name)

with open('doc_embedding_allenai_specter.pickle', 'rb') as f:
    corpus_embeddings = CPU_Unpickler(f).load()

#First, we load the papers dataset (with title and abstract information)
dataset_file = 'documents-trial.json'

with open('documents-trial.json', encoding="utf8") as f:
    papers = json.load(f)

def fetch_abstract(url):
    session = HTMLSession()
    r = session.get(url)
    content = r.html.find("#content-inner", first=True)
    abstract = content.find(".abstract", first=True).text
    return abstract

def avg_score(papers):
    avg_score = sum([p.score for p in papers]) / len(papers)
    return round(avg_score, 2)

def get_matches(embed):
    search_hits = util.semantic_search(embed, corpus_embeddings)
    search_hits = search_hits[0]  #Get the hits for the first query
    formatted_papers = []
    for hit in search_hits:
        related_paper = papers[hit['corpus_id']]
        abstract = related_paper.get('dc.description.abstract', '') if 'dc.description.abstract' in related_paper else 'DOCUMENTO SIN ABSTRACT'
        if isinstance(abstract, list):
            abstract = abstract[0] if abstract else ""
        formatted_paper = {
            "id": hit['corpus_id'],
            "score": "{:.2f}".format(hit['score']),
            "title": related_paper['dc.title'],
            "authors": related_paper['dc.contributor.author'],
            "abstract": abstract,
            "year": 'none',
            "month": 'none',
            "authors_parsed": 'none'
        }
        formatted_papers.append(formatted_paper)
    result = {"papers": formatted_papers}
    return json.dumps(result, indent=4)
    

def get_authors(papers):
    authors = defaultdict(list)
    for paper in papers:
        for author in paper.authors_parsed:
            authors[author].append(paper)
    authors = [{"author": author,
                "papers": [paper.__dict__ for paper in papers],
                "avg_score": avg_score(papers)}
                for author, papers in authors.items()]
    authors = sorted(authors, key=lambda e: e["avg_score"], reverse=True)
    authors = sorted(authors, key=lambda e: len(e["papers"]), reverse=True)
    return authors[:10]

def error(msg):
    return json.dumps({"error": msg})