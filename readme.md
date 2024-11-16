# Maze Solver with BFS and DFS

This Python project implements **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** to solve a 2D maze. The solution includes real-time console animations to visualize the pathfinding process.

---

## Features

- **BFS Solver**: Guarantees the shortest path in an unweighted maze.
- **DFS Solver**: Explores deeply and finds a path (not necessarily the shortest).
- **Real-Time Animation**: Visualizes the traversal of the maze in the console.
- **Customizable**: Easily modify the maze, start, and end points.

---

## Example Maze

```plaintext
0 1 0 0
0 0 0 1
1 1 0 1
0 0 0 0
```

Where:

- `0` = Open path
- `1` = Wall
- Start = `(0, 0)`
- End = `(3, 3)`

---

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/maze-solver.git
   cd maze-solver
   ```

2. Run the program:

   ```bash
   python maze_solver.py
   ```

3. Watch the BFS and DFS animations in the console.

---

## Customize the Maze

Edit the `maze` variable in the script to define your own maze:

```python
maze = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 0, 0, 0]
]
```

---

## Dependencies

- Python 3.x
- Standard libraries: `os`, `time`, `collections`

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.
