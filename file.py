import pickle
import numpy as np
import matplotlib.pyplot as plt

# Load data from exercise.pickle
with open('exercise.pickle', 'rb') as file:
    data = pickle.load(file)

geneList = data['geneList']
expListIDs = data['expListIDs']
exprMat = data['exprMat']

# Function to find the gene with maximum expression for each condition
def find_max_expr_genes(exprMat, geneList):
    max_expr_genes = []
    for i in range(exprMat.shape[1]):
        max_expr_gene_index = np.argmax(exprMat[:, i])
        max_expr_gene = geneList[max_expr_gene_index]
        max_expr_genes.append(max_expr_gene)
    return max_expr_genes

max_expr_genes = find_max_expr_genes(exprMat, geneList)

# Output the list of genes with maximum expression
for i, condition in enumerate(expListIDs):
    print(f"Condition '{condition}': {max_expr_genes[i]}")

# Function to plot expression values of a specific gene as a histogram
def plot_gene_expression(gene_name, exprMat, geneList):
    gene_index = geneList.index(gene_name)
    expression_values = exprMat[gene_index, :]
    
    plt.figure(figsize=(8, 6))
    plt.hist(expression_values, bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Expression Histogram for Gene {gene_name}')
    plt.xlabel('Expression Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

# Example usage: Plot expression histogram for a specific gene
# Replace 'YourGeneName' with the gene you want to plot
plot_gene_expression('YourGeneName', exprMat, geneList)
