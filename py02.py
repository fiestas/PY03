def jersey_inicializacion(cantidad_polos,cantidad_camisas,cantidad_cuellos):

    peso_polo_jersey=float(input("ingrese peso por polo en kgs de jersey :"))
    peso_camisa_jersey_=float(input("ingrese peso por camisa en kgs de jersey :"))
    peso_cuello_jersey=float(input("ingrese peso por cuello en kgs de jersey :"))

    a=[]
    a.append(cantidad_polos*peso_polo_jersey)
    a.append(cantidad_camisas*peso_camisa_jersey_)
    a.append(cantidad_cuellos*peso_cuello_jersey)
    return a

def calculo_tiempos_jersey(kg_prenda):
    kg_h_tejido=1  # velocidad de tejido en kg/h
    kg_h_tenido = 10 # velocidad de tenido en kg/h
    kg_h_acabado = 20 # velocidad de acabado en kg/h
    kg_h_confeccion_polos = 0.2 # velocidad de confeccion de polos en kg/h
  #  kg_h_confeccion_camisas = 0.5 # velocidad de confeccion de camisas en kg/h
  #  kg_h_confeccion_cuellos = 0.05 # velocidad de confeccion de cuellos en kg/h

    return kg_prenda/kg_h_tejido + kg_prenda/kg_h_tenido+kg_prenda/kg_h_acabado + kg_prenda/kg_h_confeccion_polos

def calculo_materia_prima_de_jersey(KgTela):
    return KgTela/0.7

def calculo_ganancia_jersey(MateriaPrima,cantidad_polos,cantidad_camisas,cantidad_cuellos):
    # ganancia = ventas - costo de materia prima
    precio_polo=int(input("precio por polo de jersey: "))
    precio_camisa = int(input("precio por camisa de jersey: "))
    precio_cuello = int(input("precio por cuello de jersey: "))
    return precio_polo*cantidad_polos+precio_camisa*cantidad_camisas+precio_cuello*cantidad_cuellos-MateriaPrima*10 # 10 soles por kg hilo


def main():
    # crear una lista con elementos en kgs.
    cantidad_polos = float(input("ingrese cantidad de polos de jersery:"))
    cantidad_camisas = float(input("ingrese cantidad de camisas de jersey:"))
    cantidad_cuellos = float(input("ingrese cantidad de cuellos de jersey:"))
    jersey=jersey_inicializacion(cantidad_polos,cantidad_camisas,cantidad_cuellos)
    print(jersey)

    # calcular el tiempo total de proceso en horas
    TiempoTotal=calculo_tiempos_jersey(jersey[0])
    print("Tiempo total de proceso de jersey: %f"%(TiempoTotal))

    # calcular total en kgs de tela (suma de los elementos de una lista)
    KgTela=jersey[0]+jersey[1]+jersey[2]
    MateriaPrima=calculo_materia_prima_de_jersey(KgTela)
    print("Total materia prima en kgs de jersey: %f"%(MateriaPrima))

    ganancia=calculo_ganancia_jersey(MateriaPrima, cantidad_polos,cantidad_camisas,cantidad_cuellos)
    print("total ganancia de jersey: %f"%(ganancia))

if (__name__== "__main__"):
    main()



def pique_inicializacion(cantidad_polos,cantidad_camisas,cantidad_cuellos):

    peso_polo_pique=float(input("ingrese peso por polo en kgs:"))
    peso_camisa_pique=float(input("ingrese peso por camisa en kgs:"))
    peso_cuello_pique=float(input("ingrese peso por cuello en kgs:"))

    a=[]
    a.append(cantidad_polos*peso_polo_pique)
    a.append(cantidad_camisas*peso_camisa_pique)
    a.append(cantidad_cuellos*peso_cuello_pique)
    return a

def calculo_tiempos_pique(kg_prenda):
    kg_h_tejido=0.4  # velocidad de tejido en kg/h
    kg_h_tenido = 70 # velocidad de tenido en kg/h
    kg_h_acabado = 150 # velocidad de acabado en kg/h
    kg_h_confeccion_polos = 0.2 # velocidad de confeccion de polos en kg/h
    kg_h_confeccion_camisas = 0.5 # velocidad de confeccion de camisas en kg/h
    kg_h_confeccion_cuellos = 0.05 # velocidad de confeccion de cuellos en kg/h

    return kg_prenda/kg_h_tejido + kg_prenda/kg_h_tenido+kg_prenda/kg_h_acabado + kg_prenda/kg_h_confeccion_polos

def calculo_materia_prima_de_pique(KgTela):
    return KgTela/0.5

def calculo_ganancia_pique(MateriaPrima,cantidad_polos,cantidad_camisas,cantidad_cuellos):
    # ganancia = ventas - costo de materia prima
    precio_polo=int(input("precio por polo de pique: "))
    precio_camisa = int(input("precio por camisa de pique: "))
    precio_cuello = int(input("precio por cuello de pique: "))
    return precio_polo*cantidad_polos+precio_camisa*cantidad_camisas+precio_cuello*cantidad_cuellos-MateriaPrima*10 # 10 soles por kg hilo


def main():
    # crear una lista con elementos en kgs.
    cantidad_polos = float(input("ingrese cantidad de polos de pique:"))
    cantidad_camisas = float(input("ingrese cantidad de camisas de pique :"))
    cantidad_cuellos = float(input("ingrese cantidad de cuellos de pique:"))
    pique=pique_inicializacion(cantidad_polos,cantidad_camisas,cantidad_cuellos)
    print(pique)

    # calcular el tiempo total de proceso en horas
    TiempoTotal=calculo_tiempos_jersey(pique[0])
    print("Tiempo total de proceso de pique: %f"%(TiempoTotal))

    # calcular total en kgs de tela (suma de los elementos de una lista)
    KgTela=pique[0]+pique[1]+pique[2]
    MateriaPrima=calculo_materia_prima_de_jersey(KgTela)
    print("Total materia prima en kgs de pique: %f"%(MateriaPrima))

    ganancia=calculo_ganancia_jersey(MateriaPrima, cantidad_polos,cantidad_camisas,cantidad_cuellos)
    print("total ganancia: %f"%(ganancia))

if (__name__== "__main__"):
    main()



def franela_inicializacion(cantidad_polos,cantidad_camisas,cantidad_cuellos):

    peso_polo_franela=float(input("ingrese peso por polo en kgs:"))
    peso_camisa_franela=float(input("ingrese peso por camisa en kgs:"))
    peso_cuello_franela=float(input("ingrese peso por cuello en kgs:"))

    a=[]
    a.append(cantidad_polos*peso_polo_franela)
    a.append(cantidad_camisas*peso_camisa_franela)
    a.append(cantidad_cuellos*peso_cuello_franela)
    return a

def calculo_tiempos_franela(kg_prenda):
    kg_h_tejido=0.3  # velocidad de tejido en kg/h
    kg_h_tenido = 50 # velocidad de tenido en kg/h
    kg_h_acabado = 100 # velocidad de acabado en kg/h
    kg_h_confeccion_polos = 0.2 # velocidad de confeccion de polos en kg/h
    kg_h_confeccion_camisas = 0.5 # velocidad de confeccion de camisas en kg/h
    kg_h_confeccion_cuellos = 0.05 # velocidad de confeccion de cuellos en kg/h

    return kg_prenda/kg_h_tejido + kg_prenda/kg_h_tenido+kg_prenda/kg_h_acabado + kg_prenda/kg_h_confeccion_polos

def calculo_materia_prima_de_franela(KgTela):
    return KgTela/0.5

def calculo_ganancia_franela (MateriaPrima,cantidad_polos,cantidad_camisas,cantidad_cuellos):
    # ganancia = ventas - costo de materia prima
    precio_polo=int(input("precio por polo de franela: "))
    precio_camisa = int(input("precio por camisa de franela: "))
    precio_cuello = int(input("precio por cuello de franela: "))
    return precio_polo*cantidad_polos+precio_camisa*cantidad_camisas+precio_cuello*cantidad_cuellos-MateriaPrima*10 # 10 soles por kg hilo


def main():
    # crear una lista con elementos en kgs.
    cantidad_polos = float(input("ingrese cantidad de polos de franela:"))
    cantidad_camisas = float(input("ingrese cantidad de camisas de franela :"))
    cantidad_cuellos = float(input("ingrese cantidad de cuellos de franela:"))
    franela=franela_inicializacion(cantidad_polos,cantidad_camisas,cantidad_cuellos)
    print(franela)

    # calcular el tiempo total de proceso en horas
    TiempoTotal=calculo_tiempos_franela(franela[0])
    print("Tiempo total de proceso de franela: %f"%(TiempoTotal))

    # calcular total en kgs de tela (suma de los elementos de una lista)
    KgTela=franela[0]+franela[1]+franela[2]
    MateriaPrima=calculo_materia_prima_de_franela(KgTela)
    print("Total materia prima en kgs de franela: %f"%(MateriaPrima))

    ganancia=calculo_ganancia_franela(MateriaPrima, cantidad_polos,cantidad_camisas,cantidad_cuellos)
    print("total ganancia: %f"%(ganancia))

if (__name__== "__main__"):
    main()