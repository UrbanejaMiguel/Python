def get_data():
    #En esta funcion en el futuro podriamos, por ejemplo, extraer un excel, un csv o consultar una bbdd.
    return [
          {'id': 1, 'name': 'Juan', 'age': 43, 'vigor': True},
        {'id': 2, 'name': 'María', 'age': 29, 'vigor': False},
        {'id': 3, 'name': 'Luis', 'age': 34, 'vigor': True},
        {'id': 4, 'name': 'Ana', 'age': 22, 'vigor': False},
        {'id': 5, 'name': 'Carlos', 'age': 55, 'vigor': True},
        {'id': 6, 'name': 'Marta', 'age': 31, 'vigor': False},
        {'id': 7, 'name': 'Pedro', 'age': 40, 'vigor': True},
        {'id': 8, 'name': 'Lucía', 'age': 27, 'vigor': False},
        {'id': 9, 'name': 'José', 'age': 60, 'vigor': True},
        {'id': 10, 'name': 'Elena', 'age': 45, 'vigor': False},
        {'id': 11, 'name': 'Miguel', 'age': 38, 'vigor': False},
        {'id': 12, 'name': 'Isabel', 'age': 52, 'vigor': False},
        {'id': 13, 'name': 'Andrés', 'age': 47, 'vigor': True},
        {'id': 14, 'name': 'Rosa', 'age': 58, 'vigor': False},
        {'id': 15, 'name': 'Javier', 'age': 33, 'vigor': True},
        {'id': 16, 'name': 'Sandra', 'age': 26, 'vigor': False},
        {'id': 17, 'name': 'Alberto', 'age': 49, 'vigor': True},
        {'id': 18, 'name': 'Paula', 'age': 30, 'vigor': False},
        {'id': 19, 'name': 'Fernando', 'age': 41, 'vigor': True},
        {'id': 20, 'name': 'Laura', 'age': 24, 'vigor': False}
    ]   

def get_caidas(pols):
    caidas=list(filter(lambda client: client["vigor"] == False,pols))
    return len(caidas)

def perc_g(pols):
    total = len(pols)
    caidas = get_caidas(pols)
    return (caidas/total*100)

def get_client_by_tramo(pols,tramo):
    client_by_tramo=[]
    max_age=max(client['age'] for client in pols)
    n_max=int(max_age/tramo)+1
    
    for i in range(n_max):
        a=list(filter(lambda client: tramo*i<=client["age"]<tramo*(i+1),pols))
        if a != []:
            client_by_tramo.append(a)
    return client_by_tramo
