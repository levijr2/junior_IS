import numpy as np
from numpy.random import shuffle

# If the code is not Cython-compiled, we need to add some imports.
from cython import compiled

if not compiled:
    from mazelib.solve.MazeSolveAlgo import MazeSolveAlgo


class BreadthFirstSearchSolver(MazeSolveAlgo):
    
    def get_neighbors(self, cell):
        """Get the unblocked neighbors of a cell."""
        x, y = cell
        neighbors = []
        #print("cell is", cell)
        if self.grid[cell] == 1:
            print("we in a wall, chief")
        if not self.grid[x-1,y] and (x-1, y) != self.start:
            neighbors.append((x-1, y))
            #print("up",x-1, y)
            
        if not self.grid[x+1,y] and (x+1, y) != self.start:
            neighbors.append((x+1, y))
            #print("down",x+1, y)
            
        if not self.grid[x,y+1] and (x,y+1) != self.start:
            neighbors.append((x,y+1))
            #print("right",x, y+1)
            
        if not self.grid[x,y-1] and (x,y-1) != self.start:
            neighbors.append((x,y-1))
            #print("left",x, y-1)
            
        return neighbors



    def _solve(self):
        """BFS maze solving algorithm."""
        
        if self._on_edge(self.start):
            current_node = self._push_edge(self.start)
        
        
        
        
        frontier=[] #this will act as our queue, we will use pop(0) for our dequeue
        visited = []  # Set to keep track of visited cells
        parent={} #dictionary of (node : parent pairs)
        solution=[]
        if self._on_edge(current_node):
                current_node = self._push_edge(current_node)
                
    
        frontier.append(current_node)
        visited.append(current_node)
        
        
        #explores using BFS pattern
        while not self._within_one(current_node, self.end):
            current_node = frontier.pop(0)
            current_neighbors=self.get_neighbors(current_node)
            for each in current_neighbors:
                if each not in visited:
                    frontier.append(each)
                    visited.append(each)
                    parent[each]= current_node
        
        
        #adds path of curent node and all its perents to the solution
        solution.append(current_node)
        while not self._within_one(parent[current_node], self.start): 
            solution.append(parent[current_node])
            current_node= parent[current_node]

        solution.append(self._push_edge(self.start))
        
        
        print("BFS solver visited ",len(visited), " nodes")
        return [solution]
    