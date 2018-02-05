#DFs to visit all nodes even if graph is disconnected
class Digraph(object):
    def __init__(self):
        self.edges = {}
    def addNode(self,node):
        if node in self.edges :
            print("Node Already there")
        else:
            self.edges[node] = []
    def addEdge(self,src,dest):
            self.edges[src].append(dest)
    def layout(self):
        print(self.edges)
    def childrenOf(self,node):
        return self.edges[node]

def buildCityGraph(graphType):
    g = graphType()
    for name in ('1','2','3','5','4'): #Create 7 nodes
        g.addNode(name)
    
    g.addEdge('1','3')
    g.addEdge('3','4')
    g.addEdge('2','3')
    g.addEdge('2','5')
    g.addEdge('5','4')
   
    return g

graph = buildCityGraph(Digraph)

def DFS(graph):
	for node in graph.edges:
		if node not in visited:
			children_visitor(node,graph)
			stack.append(node)
			
def children_visitor(v,graph):
	global visited,stack
	visited = visited + [v]
	for child in graph.childrenOf(v):
		if child not in visited: #if child doesnt have a parent
				children_visitor(child,graph)
				stack.append(child)
				

visited = []
disjoint = 0 
stack = []

DFS(graph)
print(stack)





#Without us
