from collections import deque
import os
import time


maze = [
    [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 0],
]

start = (0, 0)  # Starting position (row, column)
end = (9, 9)  # Ending position (row, column)


def is_valid_move(maze, visited, x, y):
    rows, cols = len(maze), len(maze[0])
    return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0 and not visited[x][y]


def print_maze(maze, current=None, path=None):
    maze_copy = [row[:] for row in maze]
    if path:
        for x, y in path:
            maze_copy[x][y] = "*"
    if current:
        x, y = current
        maze_copy[x][y] = "O"  # Highlight current position
    os.system("cls" if os.name == "nt" else "clear")
    for row in maze_copy:
        print(" ".join(str(cell) for cell in row))
    print("\n")


def animate_maze_walk(maze, start, end, path, delay=0.3):
    for pos in path:
        print_maze(maze, current=pos, path=path[: path.index(pos)])
        time.sleep(delay)
    print_maze(maze, current=None, path=path)  # Final path
    print("Path traversal complete!")


def reconstruct_path(parents: dict, start, end):
    """Reconstruct the path from start to end using the parents dictionary."""
    path = []
    current = end
    while current != start:
        path.append(current)
        current = parents[current]
    path.append(start)
    return path[::-1]


def bfs_maze_solver(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque([start])
    parents = {start: None}
    visited[start[0]][start[1]] = True
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return reconstruct_path(parents, start, end)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if all(
                [0 <= nx < rows, 0 <= ny < cols, maze[nx][ny] == 0, not visited[nx][ny]]
            ):
                visited[nx][ny] = True
                queue.append((nx, ny))
                parents[(nx, ny)] = (x, y)
    return None  # No path found


def bfs_maze_solver(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque([start])
    parents = {start: None}
    visited[start[0]][start[1]] = True

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    while queue:
        x, y = queue.popleft()

        if (x, y) == end:
            return reconstruct_path(parents, start, end)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid_move(maze, visited, nx, ny):
                visited[nx][ny] = True
                queue.append((nx, ny))
                parents[(nx, ny)] = (x, y)

    return None  # No path found


def dfs_maze_solver(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    stack = [start]
    parents = {start: None}
    visited[start[0]][start[1]] = True

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    while stack:
        x, y = stack.pop()

        if (x, y) == end:
            return reconstruct_path(parents, start, end)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid_move(maze, visited, nx, ny):
                visited[nx][ny] = True
                stack.append((nx, ny))
                parents[(nx, ny)] = (x, y)

    return None  # No path found


if __name__ == "__main__":
    # Real-time BFS animation, dfs_maze_solver
    solver = bfs_maze_solver
    # solver = dfs_maze_solver
    bfs_path = solver(maze, start, end)
    if bfs_path:
        print("Animating BFS Path:\n")
        animate_maze_walk(maze, start, end, bfs_path, delay=1.0)
    else:
        print("No path found using BFS.")
