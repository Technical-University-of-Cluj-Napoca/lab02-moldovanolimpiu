import sys
from collections import deque

def read_maze(filename: str) -> list[list[str]]:
    """Reads a maze from a file and returns it as a list of lists (i.e. a matrix).

    Args:
        filename (str): The name of the file containing the maze.
    Returns:
        list: A 2D list (matrix) representing the maze.
    """
    with open(filename, "r") as f:
        matr = f.read()
    matres = matr.split('\n')
    return matres


def find_start_and_target(maze: list[list[str]]) -> tuple[int, int]:
    """Finds the coordinates of start ('S') and target ('T') in the maze, i.e. the row and the column
    where they appear.

    Args:
        maze (list[list[str]): A 2D list (matrix) representing the maze.
    Returns:
        tuple[int, int]: A tuple containing the coordinates of the start and target positions.
        Each position is represented as a tuple (row, column).
    """
    start = None
    target = None
    for r, row in enumerate(maze):
        for c, value in enumerate(row):
            if maze[r][c] == 'S':
                start = (r, c)
            if maze[r][c] == 'T':
                target = (r,c)
    return start, target



def get_neighbors(maze: list[list[str]], position: tuple[int, int]) -> list[tuple[int, int]]:
    """Given a position in the maze, returns a list of valid neighboring positions: (up, down, left, right)
    where the player can be moved to. A neighbor is considered valid if (1) it is within the bounds of the maze
    and (2) not a wall ('#').

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        position (tuple[int, int]): The current position in the maze as (row, column).
    Returns:
        list[tuple[int, int]]: A list of valid neighboring positions.
    """
    # construct the direction array: list[tuple[int, int]] (up, down, left, right)
    # test the position in each direction
   
    #print(maze[position[0]][position[1]])
    tlist = []
    rows = len(maze[0])
    cols = len(maze)
    directions = [(-1, 0), (1, 0), (0, -1), (0,1)]
    for x in directions:
        newp = (position[0] + x[0], position[1] + x[1])
        if(0 <newp[0] < cols -1) and (0 < newp[1] < cols-1) and maze[newp[0]][newp[1]]!= '#':
            tlist.append(newp)
    return tlist
    

    



def bfs(maze: list[list[str]], start: tuple[int, int], target: tuple[int, int]) -> list[tuple[int, int]]:
    """Performs a breadth-first search (BFS) to find the shortest path from start to target in the maze.

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        start (tuple[int, int]): The starting position in the maze as (row, column).
        target (tuple[int, int]): The target position in the maze as (row, column).
    Returns:
        list[tuple[int, int]]: A list of positions representing the shortest path from start to target,
        including both start and target. If no path exists, returns an empty list.
    """
    # from collections you can import deque for using a queue.
    queu = deque([(start,[start])])
    vis = {start}

    while queu:
        curr_node,path = queu.popleft()
        if curr_node == target:
            return path
        for neighbor in get_neighbors(maze,curr_node):
            if neighbor not in vis:
                vis.add(neighbor)
                new_path = path + [neighbor]
                queu.append((neighbor,new_path))
    return None




def dfs(maze: list[list[str]], start: tuple[int, int], target: tuple[int, int]) -> list[tuple[int, int]]:
    """Performs a depth-first search (DFS) to find the shortest path from start to target in the maze.

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        start (tuple[int, int]): The starting position in the maze as (row, column).
        target (tuple[int, int]): The target position in the maze as (row, column).
    Returns:
        list[tuple[int, int]]: A list of positions representing the shortest path from start to target,
        including both start and target. If no path exists, returns an empty list.
    """
    # you can use a list as a stack in Python.
    stack = [(start,[start])]

    vis = {start}
    while start:
        curr_node, path = stack.pop()

        if curr_node == target:
            return path
        for neighbor in get_neighbors(maze,curr_node):
            if neighbor not in vis:
                vis.add(neighbor)
                new_path = path + [neighbor]
                stack.append((neighbor,new_path))
    return None



def print_maze_with_path(maze: list[list[str]], path: list[tuple[int, int]]) -> None:
    """Prints the maze to the console, marking the path with '.' characters.

    Args:
        maze (list[list[str]]): A 2D list of lists (matrix) representing the maze.
        path (list[tuple[int, int]]): A list of positions representing the path to be marked.
    Returns:
        None
    """
    # # ANSI escape code for red
    RED = "\033[91m"
    RESET = "\033[0m"
    # encode a character with red color: RED + char + RESET

    maze_copy = [list(row) for row in maze]

    for r,c in path:
        if maze_copy[r][c] not in ('S','T'):
            maze_copy[r][c] = f"{RED}x{RESET}"

    for row in maze_copy:
        print(''.join(row))

if __name__ == "__main__":
    # Example usage: py maze_search.py dfs/bfs maze.txt
    if len(sys.argv) != 3:
        print("Not enough arguments")
        exit()
    mat = read_maze(sys.argv[2])
    mat.pop()
    start, target = find_start_and_target(mat)
    #print(mat)
    if sys.argv[1] == "bfs" :
        path = bfs(mat,start,target)
    elif sys.argv[1] == "dfs" :
        path = dfs(mat,start,target)

    if path == None:
        print("No path found kek")
    else:
        print_maze_with_path(mat,path)
    