from mazelib import Maze
from mazelib.generate.Kruskal import Kruskal

from mazelib.generate.BinaryTree import BinaryTree

from mazelib.solve.Tremaux import Tremaux

from mazelib.solve.left_wall_follower import left_wall_follower

from mazelib.solve.Bfs_solver import BreadthFirstSearchSolver

from mazelib.solve.Dfs_solver import DepthFirstSearchSolver

import matplotlib.pyplot as plt


def showPNG(m):
    plt.figure(figsize=(10, 5))
    solution= m.solutions[0]
    
    for i in solution:
        plt.plot(i[1],i[0],'r+')
    plt.imshow(m.grid, cmap=plt.cm.binary, interpolation='nearest')
    plt.plot(m.start[1],m.start[0],"go")
    plt.plot(m.end[1],m.end[0],"ro")
    plt.xticks([]), plt.yticks([])
    plt.show()


size =20


m = Maze()
m.generator = Kruskal(size,size)
m.generate()
m.generate_entrances()




m.solver = left_wall_follower()
m.solve()
showPNG(m)




m.solver = Tremaux()
m.solve()
showPNG(m)



m.solver = BreadthFirstSearchSolver()
m.solve()
showPNG(m)


m.solver = DepthFirstSearchSolver()
m.solve()
showPNG(m)
