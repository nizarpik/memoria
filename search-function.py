import pickle
import io
import torch
from sentence_transformers import SentenceTransformer, util
import json
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

#print(len(papers), "papers loaded")

#We then load the allenai-specter model with SentenceTransformers
model = SentenceTransformer('allenai-specter')

#We define a function, given title & abstract, searches our corpus for relevant (similar) papers
def search_papers(title, abstract):
  query_embedding = model.encode(title+'[SEP]'+abstract, convert_to_tensor=True)

  search_hits = util.semantic_search(query_embedding, corpus_embeddings)
  search_hits = search_hits[0]  #Get the hits for the first query

  print("Paper:", title)
  print("Most similar papers:")
  for hit in search_hits:
    related_paper = papers[hit['corpus_id']]
    #print(related_paper)
    print("{:.2f}\t{}\t{} {}".format(hit['score'], related_paper['dc.title'], related_paper['dc.contributor.author'], related_paper['dc.date.issued']))

# This paper was the EMNLP 2019 Best Paper
search_papers(title='Desarrollo de software y medioambiente', abstract='')