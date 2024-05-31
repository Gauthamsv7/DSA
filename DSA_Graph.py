#Graph Creation

def build_graph(edges):
    graph = {}
    for edge in edges:
        pointA,pointB = edge
        if pointA not in graph:
            graph[pointA] = []
        if pointB not in graph:
            graph[pointB] = []
        graph[pointA].append(pointB)
        graph[pointB].append(pointA)
        
    return graph

edges = [["i","j"],
         ["k","i"],
         ["m","k"],
         ["k","l"],
         ["o","n"]]

print(build_graph(edges))

#Graph Edges with user Input 

# def build_graph_1(edges_1):
#     graph = {}
#     for edge in edges_1:
#         pointA,pointB = edge
#         if pointA not in graph:
#             graph[pointA] = []
#         if pointB not in graph:
#             graph[pointB] = []
#         graph[pointA].append(pointB)
#         graph[pointB].append(pointA)
        
#     return graph
# n = 5
# edges_1 = [] 
# for i in range(5):
#     edges_1.append(input("Please enter the edges : ").split())
# print(edges_1)

# print(build_graph_1(edges_1))


#Finding all the routes in the cities and finding the shortest route

class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        for start,end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph Dict : ",self.graph_dict)

    def get_paths(self,start,end,path=[]):
        path = path + [start]
        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return "No path"
        
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                newpaths = self.get_paths(node,end,path)
                for p in newpaths:
                    paths.append(p)
        return paths
    
    def get_shortest_path(self,start,end,path=[]):
        path = path + [start]

        if start == end :
            return path
        
        if start not in self.graph_dict:
            return "No path"
        
        shortest_path_1 = None
        for node in self.graph_dict[start]:
            if node not in path:
                shortest_path = self.get_shortest_path(node,end,path)
                if shortest_path:
                    if shortest_path_1 is None or len(shortest_path) < len(shortest_path_1):
                        shortest_path_1 = shortest_path
        return shortest_path_1
    
    
if __name__ == "__main__":
    inter_routes = [
        ("Mumbai","Hyderabad"),
        ("Mumbai","Vizag"),
        ("Hyderabad","Vizag"),
        ("Hyderabad","Rajamundry"),
        ("Vizag","Rajamundry"),
        ("Rajamundry","Kakinada"),
    ]
    
route_graph = Graph(inter_routes)
start = "Mumbai"
end = "Kakinada"

#print(f"Paths b/w {start} and {end} : ",route_graph.get_paths(start,end))
print(f"Shortest Paths b/w {start} and {end} : ",route_graph.get_shortest_path(start,end))



