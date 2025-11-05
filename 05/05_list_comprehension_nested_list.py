#matrix = []
#for i in range(100):
#    row = []
#    for j in range(5):
#        row.append(j)
#    matrix.append(row)

#print(matrix)


matrix = [[j for j in range(5)] for i in range(5)]
print(matrix)

flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix)
