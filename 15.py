def crearGrafoMaravillas():
    grafo = nx.Graph()

    maravillas = [
        ("Gran Muralla China", "China", "arquitectónica"),
        ("Petra", "Jordania", "arquitectónica"),
        ("Cristo Redentor", "Brasil", "arquitectónica"),
        ("Machu Picchu", "Perú", "arquitectónica"),
        ("Chichén Itzá", "México", "arquitectónica"),
        ("Coliseo", "Italia", "arquitectónica"),
        ("Taj Mahal", "India", "arquitectónica"),
        ("Amazonas", "Brasil/Perú/Colombia", "natural"),
        ("Bahía de Ha-Long", "Vietnam", "natural"),
        ("Cataratas del Iguazú", "Argentina/Brasil", "natural"),
        ("Jeju", "Corea del Sur", "natural"),
        ("Komodo", "Indonesia", "natural"),
        ("Río Subterráneo de Puerto Princesa", "Filipinas", "natural"),
        ("Montaña de la Mesa", "Sudáfrica", "natural")
    ]
    for nombre, pais, tipo in maravillas:
        grafo.add_node(nombre, pais=pais, tipo=tipo)

    conexiones = [
        ("Gran Muralla China", "Petra", 4000), ("Gran Muralla China", "Cristo Redentor", 17000),
        ("Gran Muralla China", "Machu Picchu", 18000), ("Gran Muralla China", "Chichén Itzá", 19000),
        ("Petra", "Coliseo", 3000), ("Petra", "Taj Mahal", 4000),
        ("Cristo Redentor", "Machu Picchu", 2500), ("Cristo Redentor", "Coliseo", 9000),
        ("Machu Picchu", "Chichén Itzá", 4000), ("Amazonas", "Cataratas del Iguazú", 4000),
        ("Bahía de Ha-Long", "Jeju", 3000), ("Jeju", "Komodo", 1500),
        ("Komodo", "Río Subterráneo de Puerto Princesa", 2500), ("Montaña de la Mesa", "Bahía de Ha-Long", 15000)
    ]
    for u, v, peso in conexiones:
        grafo.add_edge(u, v, weight=peso)

    return grafo

grafoMaravillas = crearGrafoMaravillas()

print("\nGrafo de las Maravillas del Mundo:")
for nodo in grafoMaravillas.nodes(data=True):
    print(nodo)
