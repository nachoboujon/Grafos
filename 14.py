import networkx as nx

def crearGrafoHabitaciones():
    grafo = nx.Graph()

    habitaciones = [
        "cocina", "comedor", "cochera", "quincho", "baño1", "baño2",
        "habitacion1", "habitacion2", "salaDeEstar", "terraza", "patio"
    ]
    for habitacion in habitaciones:
        grafo.add_node(habitacion)

    conexiones = [
        ("cocina", "comedor", 5), ("cocina", "cochera", 7), ("cocina", "quincho", 9),
        ("comedor", "baño1", 6), ("comedor", "baño2", 8), ("cochera", "habitacion1", 4),
        ("cochera", "terraza", 10), ("quincho", "patio", 3), ("quincho", "terraza", 12),
        ("baño1", "habitacion2", 14), ("baño1", "salaDeEstar", 11),
        ("baño2", "habitacion1", 13), ("baño2", "salaDeEstar", 15),
        ("habitacion1", "patio", 8), ("habitacion2", "salaDeEstar", 7),
        ("salaDeEstar", "terraza", 9), ("terraza", "patio", 5)
    ]
    for u, v, peso in conexiones:
        grafo.add_edge(u, v, weight=peso)

    return grafo

def calcularArbolExpansionMinima(grafo):
    return nx.minimum_spanning_tree(grafo)

grafoHabitaciones = crearGrafoHabitaciones()
arbolMinimoHabitaciones = calcularArbolExpansionMinima(grafoHabitaciones)

print("Árbol de Expansión Mínima de las Habitaciones:")
for u, v, datos in arbolMinimoHabitaciones.edges(data=True):
    print(f"{u} - {v}: {datos['weight']} metros")
