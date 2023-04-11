from mazelib import Maze
from mazelib.generate.Kruskal import Kruskal

from mazelib.solve.Tremaux import Tremaux

from mazelib.solve.new_solver import new_solver

from mazelib.solve.ShortestPath import ShortestPath

import matplotlib.pyplot as plt

def toHTML(grid, start, end, cell_size=10):
    row_max = grid.shape[0]
    col_max = grid.shape[1]

    html = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"' + \
           '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">' + \
           '<html xmlns="http://www.w3.org/1999/xhtml"><head>' + \
           '<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />' + \
           '<style type="text/css" media="screen">' + \
           '#maze {width: ' + str(cell_size * col_max) + 'px;height: ' + \
           str(cell_size * row_max) + 'px;border: 3px solid grey;}' + \
           'div.maze_row div{width: ' + str(cell_size) + 'px;height: ' + str(cell_size) + 'px;}' + \
           'div.maze_row div.bl{background-color: black;}' + \
           'div.maze_row div.wh{background-color: white;}' + \
           'div.maze_row div.rd{background-color: red;}' + \
           'div.maze_row div.gr{background-color: green;}' + \
           'div.maze_row div{float: left;}' + \
           'div.maze_row:after{content: ".";height: 0;visibility: hidden;display: block;clear: both;}' + \
           '</style></head><body>' + \
           '<div id="maze">'

    for row in range(row_max):
        html += '<div class="maze_row">'
        for col in range(col_max):
            if (row, col) == start:
                html += '<div class="gr"></div>'
            elif (row, col) == end:
                html += '<div class="rd"></div>'
            elif grid[row][col]:
                html += '<div class="bl"></div>'
            else:
                html += '<div class="wh"></div>'
        html += '</div>'
    html += '</div></body></html>'

    return html



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


size =50


m = Maze()
m.generator = Kruskal(size,size)
m.generate()
#print(m)

m.solver = new_solver()
m.generate_entrances()
m.solve()
#print(m)
print(m.solutions)


showPNG(m)


m.solver = Tremaux()
m.solve()
#print(len(m.solutions))
showPNG(m)



m.solver = ShortestPath()
m.solve()
showPNG(m)