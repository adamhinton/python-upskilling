# Here I will implement the graph data structure.

from typing import Tuple, List, Dict
type Route = Tuple[str, str]
type Routes = List[Route]

class Graph:
    def __init__(self, edges: Routes): # ["Mumbai", "Paris"]
        self.edges = edges
        self.graph_dict = {} # starting point: List of places it flies to
        for start, end in self.edges: # end is destination, start is departure location
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else: # destination not in dict
                self.graph_dict[start] = [end]

        print("\n Graph dict", self.graph_dict, "\n \n")

    def get_paths(self, start, end, path=[]):
        """
        Take in the starting location and returns all the possible paths to the end destination.

        Path starts as empty array and is built recurisively.
        """
        
        path = path + [start]

        # Recursive: Always start with simplest case
        if start == end:
            return [path]
        
        if start not in self.graph_dict: # No flights at all from departure point
            return []
        
        paths = [] # all possible paths

        for node in self.graph_dict[start]: # for each destination that this arrival point flies to
            if node not in path: # making sure we haven't already visited this destination
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths
    
    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]
        
        if start not in self.graph_dict: # Doesn't fly to any destination
            return None
        
        if start == end:
            return path
        
        shortest_path = None # We don't know at the beginning what the shortest path is
        
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if shortest_path is None or len(sp) < len(shortest_path):
                    shortest_path = sp

        return shortest_path

                
        
        # Would you not just call get_paths here and return the shortest array out of the answers?
    
        
    




if __name__ == "__main__":
    routes: Routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(routes)

    start = "Paris"
    end = "New York"
    print(f"\n Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start, end))


