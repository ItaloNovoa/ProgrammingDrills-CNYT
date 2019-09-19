def ProgamiNGDrill_3_1_1(VectorIni,MatrizDir,clicks):
    VectorIni=transpuestaVector(VectorIni)
    if(len(MatrizDir[0])!=len(VectorIni)):
        return "entrada error"        
    else:
        for i in range(clicks):
            VectorIni=multiplicacionDeMatrices(MatrizDir,VectorIni)

        return (VectorIni)


def multiplicacionDeMatrices(m1,m2):
    matriz=[]
    for i in range(len(m1)):
        vector=[]        
        for j in range(len(m2[i])):
            suma=0
            for k in range (len(m2)):                
                if(len(m1[i])!=len(m2)):
                    return "mala entrada 1"
                else:
                    suma+=m1[i][k]*m2[k][j]
            vector.append(suma)
        matriz.append(vector)
    return matriz
    
def transpuestaVector(v1):
    matriz=[]
    for i in range(len(v1)):
        vector=[v1[i]]
        matriz.append(vector)
    return matriz

