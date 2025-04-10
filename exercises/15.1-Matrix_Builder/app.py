# Your code here
def matrix_builder(num):   
    matrix = []
    
    for i in range(num):
        fila = []
        for elem in range(num):
            fila.append(1)
        matrix.append(fila)

    return matrix
    
world_matrix = matrix_builder(10)
print(world_matrix)