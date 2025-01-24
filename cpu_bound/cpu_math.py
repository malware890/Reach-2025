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
            self.sol_path: str = "mazes/sol1.txt" if path[-5] == 'e' else "mazes/sol2.txt"
            self.spaces = set()
            self.walls = set()
            self.start = None
            self.end = None
            self.lines = f.readlines()
            
            for i in range(len(self.lines)):
                for j in range(len(self.lines[i])):
                    if self.lines[i][j] == " ":
                        self.spaces.add((i, j))
                    elif self.lines[i][j] == "#":
                        self.walls.add((i, j))
                    elif self.lines[i][j] == "B":
                        self.end = (i, j)
                    elif self.lines[i][j] == "A":
                        self.start = (i, j)
            self.height = len(self.lines)
            self.width = len(self.lines[0]) - 1

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
                while node:
                    sol.append(node.state)
                    node = node.parent

                return sol

            for a in self.actions(pos.state):
                state = self.trans_model(pos.state, a)
                if state not in seen and state not in (s.state for s in frontier):
                    frontier.append(State(state, pos))

        print("No solution found")


    def bfs(self):
        frontier = [State(self.start, None)]
        seen = set()
        sol = []

        while frontier:
            pos = frontier.pop(0)
            seen.add(pos.state)

            if self.goal_check(pos.state):
                node = pos
                while node:
                    sol.append(node.state)
                    node = node.parent

                return sol

            for a in self.actions(pos.state):
                state = self.trans_model(pos.state, a)
                if state not in seen and state not in (s.state for s in frontier):
                    frontier.append(State(state, pos))

        print("No solution found")


class Symbol:
    def __init__(self, name):
        self.name = name

    def evaluate(self, model):
        return bool(model[self.name])

    def symbols(self):
        return {self.name}

class Not:
    def __init__(self, operand):
        self.operand = operand

    def evaluate(self, model):
        return not self.operand.evaluate(model)

    def symbols(self):
        return self.operand.symbols()

class And:
    def __init__(self, *conjuncts):
        self.conjuncts = list(conjuncts)

    def evaluate(self, model):
        return all(conjunct.evaluate(model) for conjunct in self.conjuncts)

    def symbols(self):
        return set.union(*[conjunct.symbols() for conjunct in self.conjuncts])

class Or:
    def __init__(self, *disjuncts):
        self.disjuncts = list(disjuncts)

    def evaluate(self, model):
        return any(disjunct.evaluate(model) for disjunct in self.disjuncts)

    def symbols(self):
        return set.union(*[disjunct.symbols() for disjunct in self.disjuncts])

class Implication:
    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent

    def evaluate(self, model):
        return ((not self.antecedent.evaluate(model))
                or self.consequent.evaluate(model))

    def symbols(self):
        return set.union(self.antecedent.symbols(), self.consequent.symbols())

class Biconditional:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, model):
        return ((self.left.evaluate(model)
                 and self.right.evaluate(model))
                or (not self.left.evaluate(model)
                    and not self.right.evaluate(model)))

    def symbols(self):
        return set.union(self.left.symbols(), self.right.symbols())


def model_check(knowledge, query):
    def check_all(knowledge, query, symbols, model):
        if not symbols:
            if knowledge.evaluate(model):
                return query.evaluate(model)
            return True
        else:
            remaining = symbols.copy()
            p = remaining.pop()

            model_true = model.copy()
            model_true[p] = True

            model_false = model.copy()
            model_false[p] = False

            return (check_all(knowledge, query, remaining, model_true) and
                    check_all(knowledge, query, remaining, model_false))

    symbols = set.union(knowledge.symbols(), query.symbols())

    return check_all(knowledge, query, symbols, dict())
