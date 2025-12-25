

#--------------------------------------------------------------------------

#Part 1: Install Required Libraries
# pip install langchain
# pip install langchain-text-splitters
# pip install pdfplumber
# pip install sentence_transformers
# pip install fastapi uvicorn
# pip install pydantic
# pip install openai
# ip install google-generativeai
  
# from fastapi import FastAPI, HTTPException, UploadFile, File, Path
# from pydantic import BaseModel
# import pdfplumber
# import numpy as np
# from starlette.formparsers import MultiPartParser
# MultiPartParser.max_memory_size = 1024 * 1024 * 2
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from sentence_transformers import SentenceTransformer
# import google.generativeai as genai
# import re


# # Configure Google Generative AI
# genai.configure(api_key="AIzaSyDgGxBUYF3fVXAIpSe72_bephqLQjlX560")
# model = genai.GenerativeModel("gemini-2.5-flash")
# embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# app = FastAPI(title="Chat with CV")


# class PathRequest(BaseModel):
#     path: str 
    
# class QueryRequest(BaseModel):
#     query: str

# chunks = [] 
# cv_embeddings = []    


# def similarity(a, b):
#     norm_a = np.linalg.norm(a)
#     norm_b = np.linalg.norm(b)
#     if norm_a == 0 or norm_b == 0:
#         return 0.0
#     return np.dot(a, b) / (norm_a * norm_b)
# def sanitize_cv_text(cv_text):
#     cv_text = re.sub(r'\n+', '\n', cv_text)
#     cv_text = re.sub(r'\s+', ' ', cv_text)
#    #cv_text = re.sub(r'[\w\.-]+@[\w\.-]+\.\w+', '[EMAIL]', cv_text)
#    #cv_text = re.sub(r'\+?\d[\d\s\-]{8,}\d', '[PHONE]', cv_text)
#     return cv_text.strip()
# def extract_text_from_pdf(file_path):
#     cv_pages = []
#     with pdfplumber.open(file_path) as pdf:
#         for page in pdf.pages:
#             text = page.extract_text()
#             if text:
#                 cv_pages.append(text)
#     if not cv_pages:
#         raise ValueError("PDF is empty or text could not be extracted")
#     cv_text = "\n".join(cv_pages)
#     return sanitize_cv_text(cv_text)


# @app.post("/upload")
# async def upload_cv(file: UploadFile = File(...)):
#     global chunks, cv_embeddings
  
#     if not file.filename.endswith(".pdf"):
#         raise HTTPException(status_code=400, detail="Only PDF files are supported")
#     temp_path = f"/tmp/{file.filename}"
#     with open(temp_path, "wb") as f:
#         content = await file.read()
#         f.write(content)
#     cv_text = extract_text_from_pdf(temp_path)
#     splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=30)
#     chunks = splitter.split_text(cv_text)
#     cv_embeddings = embed_model.encode(chunks)
#     return {"message": f"CV uploaded, sanitized, split into {len(chunks)} chunks, embeddings ready."}
# @app.post("/ask")
# async def ask_question(request: QueryRequest
#                        ):
#     global chunks, cv_embeddings
    
#     if request.query is None or request.query.strip() == "":
#         raise HTTPException(status_code=400, detail="Query cannot be empty")
    
#     query_embedding = embed_model.encode(request.query)
    

#     similarities = [similarity(query_embedding, emb) for emb in cv_embeddings]
    

#     indexed_similarities = sorted(enumerate(similarities), key=lambda x: x[1], reverse=True)
#     top_indices = [i for i, _ in indexed_similarities[:6]]
    
#     relevant_chunks = [chunks[i] for i in top_indices]
#     context = "\n\n".join(relevant_chunks)
    
#     prompt = f"""
# You are an expert HR assistant and Tech Lead. Don't answer questions outside the CV. No hallucination.Ansers should be concise and to the point.and if  some query is out of scope call I don't know. also calculate yeras and exprience ob base of provided data

# Context:
# {context}

# Question:
# {request.query}
# """

#     response = model.generate_content(prompt)
#     answer_text = response.text.strip()
#     return {"answer": answer_text}
#--------------------------------------------------------------------------

#Part 1: Install Required Libraries
#  pip install langchain
#  pip install langchain-text-splitters
#  pip install pdfplumber
#  pip install sentence_transformers
#  pip install fastapi uvicorn
#  pip install pydantic
#  pip install openai
#  pip install google-generativeai
#  pip install python-dateutil dateparser pymupdf4llm
  
# from fastapi import FastAPI, HTTPException, UploadFile, File
# from pydantic import BaseModel
# from pathlib import Path as PathLib
# import pdfplumber
# import numpy as np
# from starlette.formparsers import MultiPartParser
# #MultiPartParser.max_memory_size = 1024 * 1024 * 2
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from sentence_transformers import SentenceTransformer
# import google.generativeai as genai
# import re
# import pymupdf4llm
# from datetime import datetime
# import dateparser
# # Configure Google Generative AI
# genai.configure(api_key="AIzaSyDgGxBUYF3fVXAIpSe72_bephqLQjlX560")
# model = genai.GenerativeModel("gemini-2.5-flash")
# embed_model = SentenceTransformer("all-MiniLM-L6-v2")
# app = FastAPI(title="Chat with CV")
# class PathRequest(BaseModel):
#     path: str    
# class QueryRequest(BaseModel):
#     query: str
# chunks = [] 
# cv_embeddings = []    
# def similarity(a, b):
#     norm_a = np.linalg.norm(a)
#     norm_b = np.linalg.norm(b)
#     if norm_a == 0 or norm_b == 0:
#         return 0.0
#     return np.dot(a, b) / (norm_a * norm_b)
# def extract_text_from_pdf(file_path):
#     cv_text = pymupdf4llm.to_markdown(file_path)
#     return clean_text(cv_text)
# def clean_text(text: str) -> str:
#     lines = text.split("\n")
#     cleaned = []
#     for line in lines:
#         line = line.strip()
#         if not line:
#             continue
#         if line.lower().startswith("page "):
#             continue
#         cleaned.append(line)
#     return "\n".join(cleaned)
# def chunk_by_sections(text: str):
#     chunks = []
#     current_chunk = []
#     for line in text.split("\n"):
#         if line.startswith("## "):
#             if current_chunk:
#                 chunks.append("\n".join(current_chunk))
#                 current_chunk = []
#         current_chunk.append(line)
#     if current_chunk:
#         chunks.append("\n".join(current_chunk))
#     return chunks
# @app.post("/upload")
# async def upload_cv(file: UploadFile = File(...)):
#     global chunks, cv_embeddings
#     if not file.filename.endswith(".pdf"):
#         raise HTTPException(status_code=400, detail="Only PDF files are supported")
#     temp_path = f"/tmp/{file.filename}"
#     with open(temp_path, "wb") as f:
#         content = await file.read()
#         f.write(content)
#     cv_text = extract_text_from_pdf(temp_path)
#     cv_text = clean_text(cv_text)
#     splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=30)
#     chunks = splitter.split_text(cv_text)
#     chunks = chunk_by_sections(cv_text)
#     cv_embeddings = embed_model.encode(chunks)
# @app.post("/ask")
# async def ask_question(request: QueryRequest):
#     global chunks, cv_embeddings
#     query_embedding = embed_model.encode(request.query) 
#     similarities = [similarity(query_embedding, emb) for emb in cv_embeddings]
#     indexed_similarities = sorted(enumerate(similarities), key=lambda x: x[1], reverse=True)
#     top_indices = [i for i, _ in indexed_similarities[:3]] 
#     relevant_chunks = [chunks[i] for i in top_indices]
#     context = "\n\n".join(relevant_chunks)
#     prompt = f"""
# You are an expert HR assistant and Tech Lead. Don't answer questions outside the CV. No hallucination.
# Answers should be concise and to the point. If some query is out of scope say "not mentioned in CV".

# CV Context:
# {context}

# Question:
# {request.query}
# """
#     response = model.generate_content(prompt)
#     answer_text = response.text.strip()
#     return {"answer": answer_text}
from fastapi import FastAPI, HTTPException, UploadFile, File, Depends
from pydantic import BaseModel
from typing import Optional
import numpy as np
import pymupdf4llm
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
import google.generativeai as genai
import os


app = FastAPI(
    title="Chat with CV API",
    description="Upload CV (PDF) and chat with it using Gemini + Embeddings",
    version="1.0.0"
)


chunks = []
cv_embeddings = []
GEMINI_API_KEY: Optional[str] = None

embed_model = SentenceTransformer("all-MiniLM-L6-v2")
model = None

class APIKeyRequest(BaseModel):
    api_key: str

class QueryRequest(BaseModel):
    query: str


def similarity(a, b):
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return float(np.dot(a, b) / (norm_a * norm_b))


def clean_text(text: str) -> str:
    lines = text.split("\n")
    cleaned = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.lower().startswith("page "):
            continue
        cleaned.append(line)
    return "\n".join(cleaned)


def extract_text_from_pdf(file_path: str) -> str:
    text = pymupdf4llm.to_markdown(file_path)
    return clean_text(text)


def require_api_key():
    if GEMINI_API_KEY is None:
        raise HTTPException(
            status_code=401,
            detail="API key not set. Please insert API key first."
        )

@app.get("/")
def frontend():
    return FileResponse("index.html")

@app.post("/set-api-key")
def set_api_key(request: APIKeyRequest):
    global GEMINI_API_KEY, model

    try:
        GEMINI_API_KEY = request.api_key
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-2.5-flash")

        return {"status": "success", "message": "API key configured successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/upload-cv")
async def upload_cv(file: UploadFile = File(...)):
    require_api_key()
    global chunks, cv_embeddings

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")

    try:
        temp_path = f"/tmp/{file.filename}"

        with open(temp_path, "wb") as f:
            content = await file.read()
            f.write(content)

        cv_text = extract_text_from_pdf(temp_path)

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=250,
            chunk_overlap=30
        )
        chunks = splitter.split_text(cv_text)

        if not chunks:
            raise HTTPException(status_code=400, detail="No readable text found in CV")

        cv_embeddings = embed_model.encode(chunks)

        return {
            "status": "success",
            "message": "CV uploaded and indexed successfully",
            "total_chunks": len(chunks)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ask")
def ask_question(request: QueryRequest):
    require_api_key()

    if len(chunks) == 0 or cv_embeddings is None or len(cv_embeddings) == 0:
        raise HTTPException(
            status_code=400,
            detail="No CV uploaded. Please upload CV first."
        )

    try:
        query_embedding = embed_model.encode(request.query)

        similarities = [
            similarity(query_embedding, emb)
            for emb in cv_embeddings
        ]

        top_indices = sorted(
            enumerate(similarities),
            key=lambda x: x[1],
            reverse=True
        )[:3]

        relevant_chunks = [chunks[i] for i, _ in top_indices]
        context = "\n\n".join(relevant_chunks)

        prompt = f"""
You are an expert HR assistant.
Only answer from the CV context.
If information is missing say: "Not mentioned in CV".

CV Context:
{context}

Question:
{request.query}
"""

        response = model.generate_content(prompt)

        return {
            "question": request.query,
            "answer": response.text.strip()
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
#Part 1: Install Required Libraries
# pip install langchain
# pip install langchain-text-splitters
# pip install pdfplumber
# pip install sentence_transformers
# pip install fastapi uvicorn
# pip install pydantic
# pip install openai
# ip install google-generativeai
  
