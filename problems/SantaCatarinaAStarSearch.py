from search.utils.Node import Node
from search.utils.Adjacent import Adjacent



class SantaCatarinaMap:
    joinville = Node("Joinville", 146)
    barraVelha = Node("Barra Velha", 108)
    picarras = Node("Piçarras", 94)
    penha = Node("Penha", 92)
    navegantes = Node("Navegantes", 78)
    itajai = Node("Itajaí", 77)
    balnearioCamboriu = Node("Balneário Camboriú", 68)
    itapema = Node("Itapema", 56)
    portoBelo = Node("Porto Belo", 49)
    govCelsoRamos = Node("Governador Celso Ramos", 31)
    saoJose = Node("São José", 6)
    ranchoQueimado = Node("Rancho Queimado", 46)
    novaTrento = Node("Nova Trento", 51)
    brusque = Node("Brusque", 66)
    blumenau = Node("Blumenau", 91)
    jaraguaDoSul = Node("Jaraguá do Sul", 132)
    florianopolis = Node("Florianópolis", 0)

    joinville.addAdjacent(Adjacent(jaraguaDoSul, 53))
    joinville.addAdjacent(Adjacent(barraVelha, 57))

    barraVelha.addAdjacent(Adjacent(joinville, 57))
    barraVelha.addAdjacent(Adjacent(jaraguaDoSul, 62))
    barraVelha.addAdjacent(Adjacent(picarras, 18))

    picarras.addAdjacent(Adjacent(barraVelha, 18))
    picarras.addAdjacent(Adjacent(penha, 4))

    penha.addAdjacent(Adjacent(picarras, 4))
    penha.addAdjacent(Adjacent(navegantes, 22))

    navegantes.addAdjacent(Adjacent(penha, 22))
    navegantes.addAdjacent(Adjacent(blumenau, 58))
    navegantes.addAdjacent(Adjacent(itajai, 5))

    itajai.addAdjacent(Adjacent(navegantes, 5))
    itajai.addAdjacent(Adjacent(brusque, 35))
    itajai.addAdjacent(Adjacent(balnearioCamboriu, 17))

    balnearioCamboriu.addAdjacent(Adjacent(itajai, 17))
    balnearioCamboriu.addAdjacent(Adjacent(itapema, 16))

    itapema.addAdjacent(Adjacent(balnearioCamboriu, 16))
    itapema.addAdjacent(Adjacent(portoBelo, 23))

    portoBelo.addAdjacent(Adjacent(itapema, 12))
    portoBelo.addAdjacent(Adjacent(govCelsoRamos, 43))

    govCelsoRamos.addAdjacent(Adjacent(portoBelo, 43))
    govCelsoRamos.addAdjacent(Adjacent(saoJose, 43))

    saoJose.addAdjacent(Adjacent(govCelsoRamos, 43))
    saoJose.addAdjacent(Adjacent(florianopolis, 11))
    saoJose.addAdjacent(Adjacent(ranchoQueimado, 55))

    ranchoQueimado.addAdjacent(Adjacent(saoJose, 55))
    ranchoQueimado.addAdjacent(Adjacent(novaTrento, 87))

    novaTrento.addAdjacent(Adjacent(ranchoQueimado, 87))
    novaTrento.addAdjacent(Adjacent(brusque, 38))

    brusque.addAdjacent(Adjacent(novaTrento, 38))
    brusque.addAdjacent(Adjacent(itajai, 35))
    brusque.addAdjacent(Adjacent(blumenau, 41))

    blumenau.addAdjacent(Adjacent(brusque, 41))
    blumenau.addAdjacent(Adjacent(navegantes, 58))
    blumenau.addAdjacent(Adjacent(jaraguaDoSul, 64))

    jaraguaDoSul.addAdjacent(Adjacent(joinville, 53))
    jaraguaDoSul.addAdjacent(Adjacent(barraVelha, 62))
    jaraguaDoSul.addAdjacent(Adjacent(blumenau, 64))
