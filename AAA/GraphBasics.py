from UndirectedGraph import Graph
if __name__=='__main__':
         g = Graph()
         g.addEdge('A', 'B', 5)
         g.addEdge('A', 'C', 6)
         g.addEdge('A', 'D', 4)
         g.addEdge('B', 'C', 1)
         g.addEdge('B', 'D', 2)
         g.addEdge('C', 'D', 2)
         g.addEdge('C', 'E', 5)
         g.addEdge('C', 'F', 3)
         g.addEdge('D', 'F', 4)

         Graph = g.addEdge('E', 'F', 4)
         print(Graph)

         # TODO-1: Graph.items():
         print('Graph.items()')
         for u,edges in Graph.items():
             for v,w in edges:
                 print([u,v,w],end=',')   # Printing them as lists
         print('/n')
         print('Graph.values()')
         # # TODO-2: Graph.values():
         for edges in Graph.values():
             print(edges,end=',')
         print('/n')
         print('Graph.keys()')
         for keys in Graph.keys():
             print(keys,end=':')