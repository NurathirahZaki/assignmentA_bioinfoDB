README file- Assignment A Bioinformatics Database

Name: Nurathirah Binti Muhamad Zaki
Matrix no: A21EC3025



DELIVERABLES:

1. Design of the MongoDB structure JSON format


2. biotech.expression_data.json
 
- export from result of MongoDB database
- Database name: "biotech"
- Collection name: "expression_data"



3. Python implementation in .ipynb file

- using pandas
- import csv file for "Gene_Information.csv" , "Expression_Data.csv",  "Sample_Information.csv".
- use library from pymongo import MongoCLient to create database name and the collection in MongoDB.
- structure the data into the collection.



4. Python implement of FastAPI in .py file

- GET /genes for retrieve all gene data available in JSON structure.
- GET /gene/{gene_id} for retrieve gene data by Gene ID.
- GET /gene/name/{gene_name} for retrieve gene data by Gene Name.
- GET /gene/{gene_id}/expression for retrieve expression data associated with a gene by Gene ID.
- GET /gene/expression/{sample_id} for retrieve expression data associated with a specific sample ID.
- GET /gene/{gene_id}/sample for retrieve sample data associated with a gene by Gene ID.


