import unittest

def ProgamiNGDrill_3_1_1(VectorIni,MatrizDir,clicks):
    VectorIni=transpuestaVector(VectorIni)
    if(len(MatrizDir[0])!=len(VectorIni)):
        return "entrada error"        
    else:
        for i in range(clicks):
            VectorIni=multiplicacionDeMatrices(MatrizDir,VectorIni)

        return (VectorIni)

#m=[[(1/2**0.5,0),(1/2**0.5,0),(0,0)],[(0,-1/2**0.5),(0,1/2**0.5),(0,0)],[(0,0),(0,0),(0,0)]]
#v=[(1/3**0.5,0),(0,2/15**0.5),((2/5)**0.5,0)]
def ProgamiNGDrill_3_3_1(VectorIni,MatrizDir,clicks):
    VectorIni=transpuestaVector(VectorIni)
    if(len(MatrizDir[0])!=len(VectorIni)):
        return "entrada error"        
    else:
        for i in range(clicks):
            VectorIni=multiplicacionDeMatricesComplejas(MatrizDir,VectorIni)

        return (VectorIni)


#numRendijas entero --> cantidad de rendijas
#numBlancos entero --> cantidad de blancos por rendija
#numCompartidas entero --> cantidad de blancos compartidos con la siguiente rendija
#rendijas3_2_2(2,3,1,[1,0,0,0,0,0,0,0],1)
def rendijas3_2_2(numRendijas,numBlancos,numCompartidas,vectorInic,clicks):
    
    if(numRendijas==1):
        n=2+numBlancos
    else:
        n=(1+numRendijas)+(2*(numBlancos-numCompartidas)+numCompartidas)+((numRendijas-2)*(numBlancos-numCompartidas))

    if(len(vectorInic)!=n):
        return "las entradas no coinciden"
    else:
        m=[]
        for i in range(8):
            m.append([0]*n)
        for i in range(n):
            for j in range(n):
                if(i==0):
                    if(j>0 and j<=numRendijas):
                        m[j][i]=(1/numRendijas)
                elif(i>0 and i<=numRendijas):
                    if(i==1):
                        if(j>numRendijas+((i-1)*numBlancos) and j<=numRendijas+(i*numBlancos)):
                          m[j][i]+=(1/numBlancos)                        
                    elif(j>numRendijas+((i-1)*numBlancos)-numCompartidas and j<=numRendijas+(i*numBlancos)-numCompartidas):
                          m[j][i]+=(1/numBlancos)
                else:
                    if(i==j):
                        m[j][i]=1

        print()
        print ("la matriz es : ")
        print()
        print (bonita(m))        
        print("el vector resultante es :")
        print()
        m2=multiplicacionDeMatrices(m,m)
        return (ProgamiNGDrill_3_1_1(vectorInic,m2,clicks))

#----------------------------------------Complementarios----------------------------------------

def multiplicacionDeMatricesComplejas(m1,m2):
    matriz=[]
    for i in range(len(m1)):
        vector=[]        
        for j in range(len(m2[i])):
            suma=(0,0)
            for k in range (len(m2)):                
                if(len(m1[i])!=len(m2)):
                    return "mala entrada"
                else:
                    suma=sumas(suma,producto(m1[i][k],m2[k][j]))
            vector.append(suma)
        matriz.append(vector)

    return matriz

def sumas(c1,c2):
    preal=c1[0]+c2[0]
    pimaginaria=c1[1]+c2[1]
    return (preal,pimaginaria)

def bonita(mi):
    for i in range(len(mi)):
        for j in range(len(mi[i])):
            print(("%.2f" % mi[i][j]), end= " ") 
        print()

def bonitaCompleja(mi):
    for i in range(len(mi)):
        for j in range(len(mi[i])):
            if((mi[i][j][1])>0):
                print(str(mi[i][j][0])+"+"+str(mi[i][j][1])+"i", end= " ")
            elif((mi[i][j][1])==0):
                print(str(mi[i][j][0]), end= " ")
            else:
                print(str(mi[i][j][0])+str(mi[i][j][1])+"i", end= " ")
        print()



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

def producto(c1,c2):
    pr=(c1[0]*c2[0])-(c1[1]*c2[1])
    pi=(c1[0]*c2[1])+(c2[0]*c1[1])
    return (pr,pi)


#----------------------------------------Pruebas----------------------------------------

class TestUM(unittest.TestCase):
    #suma
    def test_caso_ProgamiNGDrill_3_1_1(self):
        V=[6,2,1,5,3,10]
        m1=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,1],[0,0,0,1,0,0],[0,0,1,0,0,0],[1,0,0,0,1,0]]
        self.assertEqual([[0], [0], [12], [5], [1], [9]],ProgamiNGDrill_3_1_1(V,m1,1))
    def test_caso_ProgamiNGDrill_3_2_1(self):
        V=[1/6,1/6,2/3]
        m1=[[0,1/6,5/6],[1/3,1/2,1/6],[2/3,1/3,0]]
        self.assertEqual([[0.5833333333333334], [0.25], [0.16666666666666666]] ,ProgamiNGDrill_3_1_1(V,m1,1))
    def test_caso_ProgamiNGDrill_3_2_2(self):
        self.assertEqual([[0.0], [0.0], [0.0], [0.16666666666666666], [0.16666666666666666], [0.3333333333333333], [0.16666666666666666], [0.16666666666666666]] ,rendijas3_2_2(2,3,1,[1,0,0,0,0,0,0,0],1))

    def test_caso_ProgamiNGDrill_3_3_1(self):
        m=[[(1/2**0.5,0),(1/2**0.5,0),(0,0)],[(0,-1/2**0.5),(0,1/2**0.5),(0,0)],[(0,0),(0,0),(0,0)]]
        v=[(1/3**0.5,0),(0,2/15**0.5),((2/5)**0.5,0)]
        self.assertEqual([[(0.408248290463863, 0.36514837167011066)], [(-0.36514837167011066, -0.408248290463863)], [(0.0, 0.0)]] ,ProgamiNGDrill_3_3_1(v,m,1))


if __name__ =='__main__':
    unittest.main()


