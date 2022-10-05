from matplotlib import pyplot

def mult_m(Mat1,Mat2):
    res=[]
    for i in range(len(Mat1)):
        columna=[]
        for j in range(len(Mat2[0])):
            val=0
            for k in range(len(Mat1[0])):
                val+=float(Mat1[i][k])*float(Mat2[k][j])
            columna.append(round(val,2))
        res.append(columna)
    return res
        
def Time_c(Grafo,Tick):
    cont=1
    last=Grafo
    while cont!=Tick:
        last=mult_m(Grafo,last)
        cont+=1
    return last

def states(grafo,state):
    res=[]
    for i in range(len(grafo)):
        for j in range(len(state[0])):
            val=0
            for k in range(len(grafo[0])):
                val+=grafo[i][k]*state[k][j]
        res.append(val)
    return res

def MC(Data1,Data2):
    res=[]
    for i in range(len(Data1)):
        columna=[]
        for j in range(len(Data2[0])):
            Rp=0
            Ip=0
            for k in range(len(Data1[0])):
                Rp+=Data1[i][k][0]*Data2[k][j][0]-Data1[i][k][1]*Data2[k][j][1]
                Ip+=Data1[i][k][0]*Data2[k][j][1]+Data2[k][j][0]*Data1[i][k][1]
            columna.append((round(Rp,4),round(Ip,4)))
        res.append(columna)
    return res

def probs(Matrix):
    res=[]
    for i in Matrix:
        Fila=[]
        for j in i:
            Fila.append(round((j[0]**2),4)+round((j[1]**2),4))
        res.append(Fila)
    return res

def grafics(resul,N_Nodes,Tiempo,Name):
    Names=[]
    for i in range(N_Nodes):
        Names.append(str(i))
    co=["blue","red","green","black","purple"]
    pyplot.title(f"Estado del sitema en el {Tiempo} clicks de tiempo: ")
    pyplot.bar(Names,height=resul,color=co,width=0.5)
    pyplot.xlabel("Vertices")
    pyplot.ylabel(Name)
    pyplot.show()

def Marble(Canicas,Grafo,Tiempo):
    State=[]
    for i in Canicas:
        State.append([i])
    Grafof=Time_c(Grafo,Tiempo)
    resul=states(Grafof,State)
    return resul

def MultR(State,Grafo):
    Statec=[]
    for i in State:
        Statec.append([i])
    grafof=Time_c(Grafo,2)
    resul=states(grafof,Statec)
    return resul

def MultRC(state,grafo):
    Statec=[]
    for i in state:
        Statec.append([i])
    Ttik=MC(grafo,grafo)
    Ttik=probs(Ttik)
    resul=states(Ttik,Statec)
    return resul


