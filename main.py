from boardCleaner import *
import copy

n = 5
goal = [['o' for i in range(n)] for j in range(n)]
initial = copy.deepcopy(goal)

'''initial[0][1] = 'x'
initial[1][0] = 'x'
initial[1][2] = 'x'
initial[2][1] = 'x'

initial[4][3] = 'x'
initial[3][2] = 'x'
initial[3][4] = 'x'
initial[2][3] = 'x'
'''

initial[0][0] = 'x'
initial[1][1] = 'x'
initial[1][4] = 'x'
initial[2][3] = 'x'
initial[3][1] = 'x'
initial[3][4] = 'x'
initial[4][0] = 'x'


bc = BoardCleaner(tuplify(initial), tuplify(goal), n)

print("Solución del Problema 1 a*")
meta6 = astar_search(bc)
if meta6:
    despliega_solucion(meta6)
else:
    print("Falla: no se encontró una solución")


print("Solución del Problema 1 mediante búsqueda primero en anchura arbol")
meta1 = breadth_first_tree_search(bc)
if meta1:
    despliega_solucion(meta1)
else:
    print("Falla: no se encontró una solución")

print("Solución del Problema 1 mediante búsqueda primero en anchura")
meta4 = breadth_first_search(bc)
if meta4:
    despliega_solucion(meta4)
else:
    print("Falla: no se encontró una solución")

print("Solución del Problema 1 mediante uniform cost searh")
meta3 = uniform_cost_search(bc)
if meta3:
    despliega_solucion(meta3)
else:
    print("Falla: no se encontró una solución")

print("Solución del Problema 1 mediante uniform cost searh")
meta3 = uniform_cost_search(bc)
if meta3:
    despliega_solucion(meta3)
else:
    print("Falla: no se encontró una solución")

print("Solución del Problema 1 depth_limited_search")
meta5 = depth_limited_search(bc, 20)
if meta5:
    despliega_solucion(meta5)
else:
    print("Falla: no se encontró una solución")

'''
print("Solución del Problema 1 mediante búsqueda primero en altura graph")
meta3 = depth_first_graph_search(bc)
if meta3:
    despliega_solucion(meta3)
else:
    print("Falla: no se encontró una solución")

print("Solución del Problema 1 mediante búsqueda primero en altura arbol")
meta2 = depth_first_tree_search(bc)
if meta2:
	print('a')
	despliega_solucion(meta2)
else:
    print("Falla: no se encontró una solución")'''

'''con 11'''
n = 11
goal = [['o' for i in range(n)] for j in range(n)]
initial = copy.deepcopy(goal)

initial[0][6] = 'x'

initial[1][0] = 'x'
initial[1][5] = 'x'
initial[1][7] = 'x'
initial[1][8] = 'x'

initial[2][1] = 'x'
initial[2][5] = 'x'
initial[2][6] = 'x'
initial[2][7] = 'x'
initial[2][9] = 'x'

initial[3][0] = 'x'
initial[3][4] = 'x'
initial[3][6] = 'x'
initial[3][8] = 'x'

initial[4][8] = 'x'

initial[5][4] = 'x'
initial[5][6] = 'x'
initial[5][7] = 'x'
initial[5][9] = 'x'

initial[6][5] = 'x'
initial[6][8] = 'x'

initial[7][2] = 'x'
initial[7][5] = 'x'
initial[7][7] = 'x'

initial[8][1] = 'x'
initial[8][3] = 'x'
initial[8][4] = 'x'
initial[8][8] = 'x'
initial[8][10] = 'x'

initial[9][2] = 'x'
initial[9][5] = 'x'
initial[9][7] = 'x'
initial[9][9] = 'x'

initial[10][10] = 'x'


bc = BoardCleaner(tuplify(initial), tuplify(goal), n)

print("Solución del Problema 1 a*")
meta6 = astar_search(bc)
if meta6:
    despliega_solucion(meta6)
else:
    print("Falla: no se encontró una solución")

n = 11
goal = [['o' for i in range(n)] for j in range(n)]
initial = copy.deepcopy(goal)

initial[0][1] = 'x'
initial[0][3] = 'x'
initial[0][7] = 'x'

initial[1][2] = 'x'
initial[1][4] = 'x'
initial[1][6] = 'x'
initial[1][8] = 'x'
initial[1][10] = 'x'


initial[2][1] = 'x'
initial[2][2] = 'x'
initial[2][3] = 'x'
initial[2][4] = 'x'
initial[2][7] = 'x'
initial[2][9] = 'x'

initial[3][0] = 'x'
initial[3][1] = 'x'
initial[3][2] = 'x'
initial[3][5] = 'x'
initial[3][6] = 'x'
initial[3][8] = 'x'
initial[3][10] = 'x'

initial[4][1] = 'x'
initial[4][2] = 'x'
initial[4][4] = 'x'
initial[4][5] = 'x'
initial[4][9] = 'x'

initial[5][6] = 'x'

initial[6][7] = 'x'
initial[6][9] = 'x'

initial[7][8] = 'x'
initial[7][10] = 'x'

initial[8][9] = 'x'

initial[9][9] = 'x'

initial[10][8] = 'x'
initial[10][10] = 'x'


bc = BoardCleaner(tuplify(initial), tuplify(goal), n)

print("Solución del Problema 1 a*")
meta6 = astar_search(bc)
if meta6:
    despliega_solucion(meta6)
else:
    print("Falla: no se encontró una solución")

