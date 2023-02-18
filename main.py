import numpy as np


class Movement():
    pos: any
    direction: str  # "up" | "down" | "left" | "right"
    parent: any
    isRoot: bool

    def __init__(self, pos, direction, parent, root=False):
        self.pos = pos
        self.direction = direction
        self.parent = parent
        self.isRoot = root


def moveToCoord(pos, move):
    match move:
        case "up":
            return (pos[0]+1, pos[1])
        case "down":
            return (pos[0]-1, pos[1])
        case "left":
            return (pos[0], pos[1]-1)
        case "right":
            return (pos[0], pos[1]+1)


def isValid(maze, pos):
    a, b = pos
    return (maze[a][b] == " ") or (maze[a][b] == "F")


def findStart(maze):
    a = np.argwhere(np.array(maze) == "$")[0]
    return (a[0], a[1])


def isFound(maze, pos):
    a, b = pos
    return maze[a][b] == "F"


def block(maze, pos):
    a, b = pos
    maze[a][b] = "@"
    return maze


def whileAway(maze):
    start = findStart(maze)
    queue = [
        Movement(start, "", None, True)
    ]
    tail = None
    while (len(queue) > 0):
        nxt = queue.pop()
        for each in ["up", "down", "left", "right"]:
            newPos = moveToCoord(nxt.pos, each)
            if isValid(maze, newPos):
                queue.insert(0, Movement(newPos, each, nxt))
                if isFound(maze, newPos):
                    tail = queue[0]
                    return tail
                maze = block(maze, newPos)
    return tail


def main(maze):
    tail = whileAway(maze)

    if tail == None:
        print("No Path!")
    else:
        path = []
        while not tail.isRoot:
            path.insert(0, tail.direction)
            tail = tail.parent
        print("Path: ", end="")
        print(", ".join(path))
    return maze


if __name__ == "__main__":
    maze = [['+', '-', '+', '-', '+', '-', '+'],
            ['|', ' ', ' ', ' ', ' ', ' ', '|'],
            ['+', ' ', '+', '-', '+', ' ', '+'],
            ['|', ' ', ' ', 'F', '|', ' ', '|'],
            ['+', '-', '+', '-', '+', ' ', '+'],
            ['|', '$', ' ', ' ', ' ', ' ', '|'],
            ['+', '-', '+', '-', '+', '-', '+']]
    
    # print maze
    # print("\n".join([
    #     "".join(each)
    #     for each in maze
    # ]))

    maze = main(maze)

    # print maze (to see path)
    # print("\n".join([
    #     "".join(each)
    #     for each in maze
    # ]))
