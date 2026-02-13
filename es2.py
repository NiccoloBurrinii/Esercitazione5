class Matrice():
    def __init__(self, righe, colonne, valore=0):
        self.righe = righe
        self.colonne = colonne
        self.valori = [[valore for _ in range(colonne)] for _ in range(righe)]


    def __getitem__ (self, index):
        return self.valori[index]
    
    def __setitem__ (self, index, value):
        self.valori[index] = value

    def __str__(self):
        return "\n".join(["\t".join(map(str, riga)) for riga in self.valori])
    
    def __len__(self):
        return self.righe * self.colonne
    
    def dimensioni(self):
        return (self.righe, self.colonne)
    
    def trasposta(self):
        trasposta = Matrice(self.colonne, self.righe)
        for i in range(self.righe):
            for j in range(self.colonne):
                trasposta[j][i] = self.valori[i][j]
        return trasposta
    

mat = Matrice(3, 3)

# Imposta valori
mat[0][0] = 1
mat[0][1] = 2
mat[0][2] = 3
mat[1] = [4, 5, 6]
mat[2] = [7, 8, 9]

print(mat)
print(f"Elemento [1][1]: {mat[1][1]}")  # 5
print(f"Dimensioni: {mat.dimensioni()}")  # (3, 3)

# Trasposta
mat_t = mat.trasposta()
print("Trasposta:")
print(mat_t)