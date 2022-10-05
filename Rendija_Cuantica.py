import Cuantico
import math
##Experimento de las múltiples rendijas cuántico.
def Create_GC(N_Nodes,Slits):
    Grafo=[]
    for i in range(N_Nodes):
        Fila=[]
        for j in range(N_Nodes):
            if i == 0:
                k=(0,0)
                Fila.append(k)
            elif i<=Slits:
                if j==0:
                    k=(round((1/math.sqrt(Slits)),4),0)
                else:
                    k=(0,0)
                Fila.append(k)
            else:
                if j>0 and j<=Slits:
                    print("Con que probabilidad da el foton en el objetivo ",i-Slits," desde la rendija ",j,)
                    Rp=float(input("Parte real de la probabilidad: "))
                    Ip=float(input("Parte imaginaria de la probabilidad: "))
                    prob=(Rp,Ip)
                    Fila.append(prob)    
                elif j==i:
                    Fila.append((1,0))
                else:
                    Fila.append((0,0))
        Grafo.append(Fila)
    return Grafo
def MultRCE():
    Slits=int(input("Dame el numero de rendijas que quieres usar: "))
    Targets=int(input("Dame el numero de objetivos que quieres usar: "))
    N_Nodes=Slits+Targets+1
    State=[[1]]
    for i in range(N_Nodes-1):
        State.append([0])
    grafo=Create_GC(N_Nodes,Slits)
    print("\nEl estado del sitema al inicio es:\n")
    print(State)
    print("\nEl estado del grafo con numeros complejos es: \n")
    for i in grafo:
        print(i)
    print("\nEl estado del grafo en probabilidad es: \n")
    for i in Cuantico.probs(grafo):
        print(i)
    print("\nEl estado del grafo despues de 2 time clicks es: \n")
    Ttik=Cuantico.MC(grafo,grafo)
    for i in Ttik:
        print(i)
    print("\nEl estado del grafo en probabilidad en 2 time clicks es:\n ")
    for i in Cuantico.probs(Ttik):
        print(i)
    print("\nEl estado del sistema despues de 2 time cliks es:\n ")
    resul=Cuantico.states(Cuantico.probs(Ttik),State)
    print(resul)
    for i in range(len(resul)):
        resul[i]=resul[i]*100
    Cuantico.grafics(resul,N_Nodes,2,"Porcentaje(%)")
MultRCE()