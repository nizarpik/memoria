import flask
import json
from sentence_transformers import SentenceTransformer, util
#import openai
import os
import pinecone
import validators
from flask import render_template, request
#from openai.embeddings_utils import get_embedding
from helpers import get_matches, get_authors, fetch_abstract, error

app = flask.Flask(__name__)

#First, we load the papers dataset (with title and abstract information)
dataset_file = 'emnlp2016-2018.json'

if not os.path.exists(dataset_file):
  util.http_get("https://sbert.net/datasets/emnlp2016-2018.json", dataset_file)

with open(dataset_file) as fIn:
  papers = json.load(fIn)

#We then load the allenai-specter model with SentenceTransformers
model = SentenceTransformer('allenai-specter')

#To encode the papers, we must combine the title and the abstracts to a single string
paper_texts = [paper['title'] + '[SEP]' + paper['abstract'] for paper in papers]

#Compute embeddings for all papers
corpus_embeddings = model.encode(paper_texts, convert_to_tensor=True)

#We define a function, given title & abstract, searches our corpus for relevant (similar) papers
def search_papers(query):
  query_embedding = model.encode(query, convert_to_tensor=True)

  search_hits = util.semantic_search(query_embedding, corpus_embeddings)
  search_hits = search_hits[0]  #Get the hits for the first query

  print("Paper:", query)
  print("Most similar papers:")
  for hit in search_hits:
    related_paper = papers[hit['corpus_id']]
    print("{:.2f}\t{}\t{} {}".format(hit['score'], related_paper['title'], related_paper['venue'], related_paper['year']))
    
# use OpenAI API key
# openai.api_key = os.environ["OPENAI_API_KEY"]
# MODEL = "text-embedding-ada-002"

# connect to Pinecone
#pinecone.init(api_key=os.environ["568c7b26-a502-4420-a50f-144d71e37c3a"])
#index = pinecone.Index("searchthearxiv")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/search")
def search():
    query = request.args.get("query")
    K = 100 # number of matches to request from Pinecone
    
    # special logic for handling arxiv url queries
    # if validators.url(query):
    #    arxiv_id = query.split("/")[-1]
    #    matches = index.fetch([arxiv_id])["vectors"]
    #    if len(matches) == 0:
    #        abstract = fetch_abstract(query)
    #        embed = get_embedding(abstract, MODEL)
    #        return get_matches(index, K, vector=embed, exclude=arxiv_id)
    #    return get_matches(index, K, id=arxiv_id, exclude=arxiv_id)
    
    # reject natural language queries longer than 200 characters
    if len(query) > 200:
        return error("Sorry! The length of your query cannot exceed 200 characters.")
    
    # embed query using OpenAI API
    try:
        #embed = get_embedding(query, MODEL)
        embed = model.encode(query, convert_to_tensor=True)
    except Exception as e:
        print(f"Encountered error when fetching embedding from OpenAI: {e}", flush=True)
        return error("OpenAI not responding. Try again in a few minutes.")
    
    # once we have the query embedding, find closest matches in Pinecone
    try:
        return render_template("index.html")
        #return get_matches(index, K, vector=embed)
    except Exception as e:
        print(f"Encountered error when fetching matches from Pinecone: {e}", flush=True)
        return error("Pinecone not responding. Try again in a few minutes.")

@app.route("/robots.txt")
def robots():
    with open("static/robots.txt", "r") as f:
        content = f.read()
    return content
