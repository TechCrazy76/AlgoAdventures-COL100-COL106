from maze import *
from exception import *
from stack import *
class PacMan:
    def __init__(self, grid : Maze) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        self.navigator_maze = grid.grid_representation
    def find_path(self, start, end):
        # IMPLEMENT FUNCTION HERE
        start_blocked = self.navigator_maze[start[0]][start[1]] == 1
        end_blocked = self.navigator_maze[end[0]][end[1]] == 1
        if start_blocked or end_blocked:
            raise PathNotFoundException

        stack = Stack() # Initialize stack for DFS with the start cell and an empty path
        stack.push((start, []))  # Store the cell and the path to reach it

        visited = set() # Track visited cells
        visited.add(start)

        while not stack.is_empty():
            current, path = stack.pop()
            new_path = path + [current]  # Extend the path to include the current cell
            if current == end: # To check if we've reached the end
                return new_path

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # Exploring neighbors (up, down, left, right)
                nx, ny = current[0] + dx, current[1] + dy
                if (0 <= nx < len(self.navigator_maze) and
                    0 <= ny < len(self.navigator_maze[0]) and
                    self.navigator_maze[nx][ny] == 0 and
                    (nx, ny) not in visited):
                    stack.push(((nx, ny), new_path))
                    visited.add((nx, ny))

        raise PathNotFoundException  # If we exhaust all possibilities and don't find the end