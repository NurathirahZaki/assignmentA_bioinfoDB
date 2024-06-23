# NURATHIRAH BINTI MUHAMAD ZAKI
# A21EC3025
# Assignment A BioinfoDB

import json
from typing import List
from fastapi import FastAPI, HTTPException
#from pymongo import MongoClient


#load the JSON data from file
with open("biotech.expression_data.json") as f:
    gene_data = json.load(f)
    
'''
#Initialize MongoDB client
client = MongoClient('mongodb://localhost:27017/')
db = client.biodata
collection = db.sequence_data'''


app = FastAPI()

#endpoint to get gene by ID
@app.get("/gene/{gene_id}")
async def get_gene_by_id(gene_id: str):
    for gene in gene_data:
        if gene["Gene ID"] == gene_id:
            return gene
    raise HTTPException(status_code=404, detail="Gene not found")



#endpoint to get gene by name
@app.get("/gene/name/{gene_name}")
async def get_gene_by_name(gene_name: str):
    # Search for the gene with the specified name
    for gene in gene_data:
        if gene["Gene Name"] == gene_name:
            return gene
    # If the gene is not found, raise a 404 error
    raise HTTPException(status_code=404, detail="Gene not found")


#endpoint to get gene expression data by gene ID
@app.get("/gene/{gene_id}/expression")
async def get_gene_expression(gene_id: str):
    for gene in gene_data:
        if gene["Gene ID"] == gene_id:
            return gene["expression"]
    raise HTTPException(status_code=404, detail="Gene not found")


#ndpoint to get gene expression data by sample ID
@app.get("/gene/expression/{sample_id}")
async def get_expression_by_sample_id(sample_id: str):
    for gene in gene_data:
        for expr in gene["expression"]:
            if expr["Sample ID"] == sample_id:
                return expr
    raise HTTPException(status_code=404, detail="Sample ID not found")


#endpoint to get sample data by gene ID
@app.get("/gene/{gene_id}/sample")
async def get_gene_samples(gene_id: str):
    for gene in gene_data:
        if gene["Gene ID"] == gene_id:
            return gene["sample"]
    raise HTTPException(status_code=404, detail="Gene not found")


#endpoint to get all genes
@app.get("/genes")
async def get_all_genes():
    return gene_data

#server using Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
