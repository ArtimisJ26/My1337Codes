class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # convert edgelist to adjacency list
        graph = self.buildGraph(edges)
        print(graph)
        # Initialize count
        count = 0
        # Initialized visited set
        visited = set()
        # Iterate over each node
        for node in graph:
            # explore the full  connection to know which of the nodes are connected here
            print(node)
            if self.explore(graph,node,visited):
                count += 1
        
        # check if n > len(graph) if yes then add those as individual nodes
        if n > len(graph):
            count += n-len(graph)
        # return count
        return count
    
    def buildGraph(self, edges):
        graph = {}

        for edge in edges:
            a,b = edge
            if a not in graph: graph[a] = []
            if b not in graph: graph[b] = []
            graph[a].append(b)
            graph[b].append(a)

        return graph

    def explore(self, graph, node, visited):
        if node in visited: return False
        visited.add(node)

        for neighbor in graph[node]:
            self.explore(graph,neighbor,visited)

        return True
