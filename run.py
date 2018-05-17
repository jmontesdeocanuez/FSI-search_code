# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)


#print search.breadth_first_graph_search(ab).path()
#print search.depth_first_graph_search(ab).path()

#print search.iterative_deepening_search(ab).path()
#print search.depth_limited_search(ab).path()


print "La ruta mas corta es:"

# Result:
print "[<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418"
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
print "Con el algoritmo de ramificacion y salto se obtiene la siguiente ruta:"
print search.ramification_graph_search(ab).path()
print "Con el algoritmo de ramificacion y salto con subestimacion se obtiene la siguiente ruta"
print search.astar_search(ab).path()

