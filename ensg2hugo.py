#!/usr/bin/python
import sys
import fileinput
import re
import numpy as np
import pandas as pd

eth={}
for each_line_of_text in fileinput.input("/home/jupyter-aomidsal/data/Homo_sapiens.GRCh37.75.gtf"):
    gene=re.findall(r'^.*?\t.*?\t(gene)\t', each_line_of_text, re.I)
    gene_id=re.findall(r'gene_id "(ENSG\d*?)"', each_line_of_text, re.I)
    gene_name=re.findall(r'gene_name "(.*?)"', each_line_of_text, re.I)
    homo_sapiens_split= re.split('\t', each_line_of_text)
    if gene:
        if gene_id:
            if gene_name:
                eth[gene_id[0]] = gene_name[0]
                
if sys.argv[1][:2] == '-f':
    columnnumber = sys.argv[1][2]
    data = sys.argv[2]
    column = int(columnnumber) - 1
else:
    column = 1
    data = sys.argv[1]               

data = pd.read_csv(data)
data.iloc[:, column]=data.iloc[:, column].astype(str).str.replace(r'(\.\d*)', '')
data.iloc[:, column]=data.iloc[:, column].str.strip('"')
data.iloc[:, column]=data.iloc[:, column].replace(eth)
print(data)
