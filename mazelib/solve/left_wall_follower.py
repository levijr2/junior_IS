from random import choice

# If the code is not Cython-compiled, we need to add some imports.
from cython import compiled

if not compiled:
    from mazelib.solve.MazeSolveAlgo import MazeSolveAlgo


class left_wall_follower(MazeSolveAlgo):
    """
    1. follow the left wall untill the end
    """
    def find_direction(self,down1,over1,down2,over2):
        
        if down2 < down1 :
            return 'North'
        elif down2 > down1:
            return 'South'
        elif over2 > over1:
            return 'East'
        elif over2 < over1:
            return 'West'
        else:
            return 'Same coordinates'
        
    def go_left(self,orientation,place):
        
        if orientation == 'North':
            return (place[0] ,place[1]-1)
        
        elif orientation == 'South':
            return (place[0] ,place[1]+1)
        
        elif orientation == 'East':
            return (place[0]-1 ,place[1])
        
        elif orientation == 'West':
            return (place[0]+1 ,place[1])
        
    def go_right(self,orientation,place):
        
        if orientation == 'North':
            return (place[0] ,place[1]+1)
        
        elif orientation == 'South':
            return (place[0] ,place[1]-1)
        
        elif orientation == 'East':
            return (place[0]+1 ,place[1])
        
        elif orientation == 'West':
            return (place[0]-1 ,place[1])
        
    def go_straight(self,orientation,place):
        
        if orientation == 'North':
            return (place[0]-1,place[1])
        
        elif orientation == 'South':
            return (place[0]+1 ,place[1])
        
        elif orientation == 'East':
            return (place[0],place[1]+1)
        
        elif orientation == 'West':
            return (place[0] ,place[1]-1)
        
    def go_straight(self,orientation,place):
        
        if orientation == 'North':
            return (place[0]-1,place[1])
        
        elif orientation == 'South':
            return (place[0]+1 ,place[1])
        
        elif orientation == 'East':
            return (place[0],place[1]+1)
        
        elif orientation == 'West':
            return (place[0] ,place[1]-1)     
        
    def go_back(self,orientation,place):
        
        if orientation == 'North':
            return (place[0]+1,place[1])
        
        elif orientation == 'South':
            return (place[0]-1 ,place[1])
        
        elif orientation == 'East':
            return (place[0],place[1]-1)
        
        elif orientation == 'West':
            return (place[0] ,place[1]+1)     
        
    def _solve(self):
        solution = []

        # a first move has to be made
        current = self.start
        solution.append(current)
        if self._on_edge(self.start):
            current = self._push_edge(self.start)
        solution.append(current)
        
        
        orientation= self.find_direction(solution[-2][0],solution[-2][1],current[0],current[1])
        #print(self.go_back(orientation, current))
        
        # follow the left wall until you hit the end
        Node_count=0
        
        while not self._within_one(solution[-1], self.end):
            if(self.grid[solution[-1]]):
                return solution
            
            orientation= self.find_direction(solution[-2][0],solution[-2][1],solution[-1][0],solution[-1][1])
            
            if not self.grid[self.go_left(orientation,solution[-1])]:
                current=self.go_left(orientation,solution[-1])
                solution.append(current)
                Node_count= Node_count + 1
                
            elif not self.grid[self.go_straight(orientation,solution[-1])]:
                current=self.go_straight(orientation,solution[-1])
                solution.append(current)
                Node_count= Node_count + 1

                
            elif not self.grid[self.go_right(orientation,solution[-1])]:
                current=self.go_right(orientation,solution[-1])
                solution.append(current)
                Node_count= Node_count + 1
                
            elif not self.grid[self.go_back(orientation,solution[-1])]:
                current=self.go_back(orientation,solution[-1])
                solution.append(current)
                Node_count= Node_count + 1

        
        print(print("Left_wall_follower solver visited ",Node_count, " nodes"))
        return [solution]