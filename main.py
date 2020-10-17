from search.AStar import AStar
from problems.SantaCatarinaAStarSearch import SantaCatarinaMap

mapa = SantaCatarinaMap()

astar = AStar(mapa.florianopolis)
astar.search(mapa.joinville)