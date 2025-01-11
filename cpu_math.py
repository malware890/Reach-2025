def prime_check(start: int, end: int):
    for i in range(start, end + 1):
        p = True
        for j in range(2, int(i ** 0.5)):
            if not i % j:
                p = False
                break
        if p:
            yield i


def mat_mult(mat1: list[list], mat2: list[list]):
    if len(mat1[0]) != len(mat2) or not mat1 or not mat2:
        raise ValueError("Invalid Arguments")

    result = [[0 for _ in range(len(mat2[0]))] for __ in range(len(mat1))]

    for i in range(len(mat2[0])):
        for j in range(len(mat1)):
            s = 0
            for k in range(len(mat1[0])):
                s += mat1[j][k] * mat2[k][i]
            result[j][i] = s

    return result


class State:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent

    def __repr__(self):
        return f"({self.state[0]}, {self.state[1]})"


class Maze:
    def __init__(self, path):
        with open(path) as f:
            self.spaces = set()
            self.walls = set()
            self.start = None
            self.end = None
            lines = f.readlines()
            for i in range(len(lines)):
                for j in range(len(lines[i])):
                    if lines[i][j] == " ":
                        self.spaces.add((i, j))
                    elif lines[i][j] == "#":
                        self.walls.add((i, j))
                    elif lines[i][j] == "B":
                        self.end = (i, j)
                    elif lines[i][j] == "A":
                        self.start = (i, j)
            self.height = len(lines)
            self.width = len(lines[0]) - 1

    def actions(self, pos):
        acts = ["Up", "Down", "Left", "Right"]
        if not pos[0] or (pos[0] - 1, pos[1]) in self.walls:
            acts.remove("Up")
        if pos[0] == self.height - 1 or (pos[0] + 1, pos[1]) in self.walls:
            acts.remove("Down")
        if not pos[1] or (pos[0], pos[1] - 1) in self.walls:
            acts.remove("Left")
        if pos[1] == self.width - 2 or (pos[0], pos[1] + 1) in self.walls:
            acts.remove("Right")
        return acts

    @staticmethod
    def trans_model(pos, action):
       match action:
           case "Up":
               return pos[0] - 1, pos[1]
           case "Down":
               return pos[0] + 1, pos[1]
           case "Left":
               return pos[0], pos[1] - 1
           case "Right":
               return pos[0], pos[1] + 1

    def goal_check(self, pos):
        return True if pos == self.end else False

    def dfs(self):
        frontier = [State(self.start, None)]
        seen = set()
        sol = []

        while frontier:
            pos = frontier.pop()
            seen.add(pos.state)
            if self.goal_check(pos.state):
                node = pos
                sol.append(node)
                while node.parent:
                    sol.append(node.parent)
                    node = node.parent
                sol.reverse()
                return sol
            for a in self.actions(pos.state):
                state = self.trans_model(pos.state, a)
                if state not in frontier and state not in seen:
                    frontier.append(State(state, pos))

    def bfs(self):
        frontier = [State(self.start, None)]
        seen = set()
        sol = []

        while frontier:
            pos = frontier.pop(0)
            seen.add(pos.state)
            if self.goal_check(pos.state):
                node = pos
                sol.append(node)
                while node.parent:
                    sol.append(node.parent)
                    node = node.parent
                sol.reverse()
                return sol
            for a in self.actions(pos.state):
                state = self.trans_model(pos.state, a)
                if state not in frontier and state not in seen:
                    frontier.append(State(state, pos))



