import Cuantico
##Experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas.
def Create_G(N_Nodes,Slits):
    Grafo=[]
    for i in range(N_Nodes):
        Fila=[]
        for j in range(N_Nodes):
            if i == 0:
                j="0.00"
                Fila.append(j)
            elif i<=Slits:
                if j==0:
                    j=round((1/Slits),2)
                else:
                    j="0.00"
                Fila.append(j)
            else:
                if j>0 and j<=Slits:
                    print("Con que probabilidad da el foton en el objetivo ",i-Slits," desde la rendija ",j,"(Numeros decimales.)")
                    prob=float(input())
                    Fila.append(round(prob,2))    
                elif j==i:
                    Fila.append("1.00")
                else:
                    Fila.append("0.00")
        Grafo.append(Fila)
    return Grafo

def MultRE():
    Slits=int(input("Dame el numero de rendijas que quieres usar: "))
    Targets=int(input("Dame el numero de objetivos que quieres usar: "))
    N_Nodes=Slits+Targets+1
    State=[[1]]
    for i in range(N_Nodes-1):
        State.append([0])
    grafo=Create_G(N_Nodes,Slits)
    print("\nEl estado del grafo inicial es:\n")
    for i in grafo:
        print(*i)
    data=int(input("\nDame el numero de clicks de tiempo en el cual quieres evaluar el estado del sistema:"))
    grafof=Cuantico.Time_c(grafo,data)
    print(f"\nEl grafo a los {data} clicks de tiempo es:\n")
    for i in grafof:
        print(*i)
    print("\nEl estado del sistema al inicio es :\n")
    print(State)
    print("\nEl estado final del sistema es: \n")
    resul=Cuantico.states(grafof,State)
    print(resul)
    Cuantico.grafics(resul,N_Nodes,data,"Probabilidades")
MultRE()