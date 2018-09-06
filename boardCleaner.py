from search import ( # Bases para construcción de problemas
    Problem, Node, Graph, UndirectedGraph,
    SimpleProblemSolvingAgentProgram,
    GraphProblem
)

from search import ( # Algoritmos de búsqueda no informada
    tree_search, graph_search, best_first_graph_search,
    breadth_first_tree_search, breadth_first_search,
    depth_first_tree_search, depth_first_graph_search,
    depth_limited_search, iterative_deepening_search,
    uniform_cost_search,
    compare_searchers
)

from search import ( # Algoritmos de búsqueda informada (heurística)
    greedy_best_first_graph_search, astar_search
)

import pprint
import copy

pp = pprint.PrettyPrinter()

def check_if_valid(action, n):
    i, j = action 
    return i >= 0 and i <= n - 1 and j >= 0 and j <= n-1

def change_piece(item):
    return 'x' if item == 'o' else 'o'

def tuplify(mat):
    return tuple([tuple(x) for x in mat])

def new_state(state, action, n):
    new = list(list(x) for x in state)
    #extract coordinates
    i, j = action

    #check if valid move
    if check_if_valid(action, n):
        if i > 0: 
            new[i-1][j] = change_piece(new[i-1][j])
        if i < n-1:
            new[i+1][j] = change_piece(new[i+1][j])
        if j > 0:
            new[i][j-1] = change_piece(new[i][j-1])
        if j < n-1:
            new[i][j+1] = change_piece(new[i][j+1])
            
    else:
        return -1

    return tuplify(new)

class BoardCleaner(Problem):

    """Board cleaner problem
    state: nxn board with x representing occupied spaces
    and o empty ones."""
    def __init__(self, initial, goal, n):
        Problem.__init__(self, initial, goal)
        self.n = n

    def actions(self, state):
        return [(i, j) for i in range(self.n) for j in range(self.n)]

    def result(self, state, action):
        res = new_state(state, action, self.n)
        return res

    '''counts the numbers of tokens left on the board'''
    def h(self, node):
        count = 0
        for lst in node.state:
            count = count + lst.count('x')
        return count


def despliega_solucion(nodo_meta):
    """Despliega la secuencia de estados y acciones de una solución"""
    acciones = nodo_meta.solution()
    print(acciones)
    nodos = nodo_meta.path()
    print('SOLUCION:')
    print('Estado')
    pp.pprint(nodos[0].state)
    for na in range(len(acciones)):
        print(acciones[na])
        print('Estado')
        pp.pprint(nodos[na+1].state)
    print('FIN')
