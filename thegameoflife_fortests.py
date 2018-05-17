import sys


def Create(name, y, x, desk):
    if name == ".":
        return Void(y, x, desk)
    elif name == "f":
        return Fish(y, x, desk)
    elif name == "#":
        return Rock(y, x, desk)
    elif name == "s":
        return Shrimp(y, x, desk)
    else:
        raise ValueError

def GetSymbol(name):
    if name == "Void":
        return "."
    elif name == "Fish":
        return "f"
    elif name == "Rock":
        return "#"
    elif name == "Shrimp":
        return "s"
    else:
        raise ValueError

class Desk:
    def __init__(self, height, weight):
        self.height = height + 2
        self.weight = weight + 2
        self.matrix = list()
        self.matrix = [[] for i in range(self.height)]
        for i in range(self.height):
            self.matrix[i] = [Void(i, j, self) for j in range(self.weight)]


    def SetStringMatrix(self, y, st):
        for i in range(self.weight - 2):
            self.matrix[y][i+1] = Create(st[i], y, i+1, self)

    def ClearNewMatrix(self):
        self.newmatrix = list()
        self.newmatrix = [[] for i in range(self.height)]
        for i in range(self.height):
            self.newmatrix[i] = [Void(i, j, self) for j in range(self.weight)]

    def UpdateMatrix(self):
        self.ClearNewMatrix()
        for i in range(self.height-2):
            for j in range(self.weight-2):
                self.matrix[i+1][j+1].Update()
        for i in range(self.height-2):
            for j in range(self.weight-2):
                self.matrix[i+1][j+1] = self.newmatrix[i+1][j+1]

    def Print(self, OutputWhere):
        for i in range(self.height-2):
            s = ""
            for j in range(self.weight-2):
                s = s + GetSymbol(self.matrix[i+1][j+1].Print())
            print(s, file=OutputWhere)


def modeling(InputFrom, OutputWhere):
    Input = InputFrom.read().split('\n')
    generations = int(Input[0])
    ls = Input[1].split()
    matrix = Desk(int(ls[0]), int(ls[1]))
    for t in range(matrix.height - 2):
        s = Input[t+2]
        matrix.SetStringMatrix(t+1, s)
    while generations > 0:
        matrix.UpdateMatrix()
        generations -= 1
    matrix.Print(OutputWhere)


class ObjInterface:
    def __init__(self, ycoor, xcoor, deskc):
        self.x = xcoor
        self.y = ycoor
        self.desk = deskc

    def Update(self):
        pass

    def CheckCondition(self, obj):
        counter = 0
        for i in range(3):
            for j in range(3):
                if type(self.desk.matrix[self.y - 1 + i][self.x - 1 + j]) == obj:
                    counter += 1
        return counter

    def Print(self):
        pass


class Fish(ObjInterface):
    def Print(self):
        return "Fish"

    def Update(self):
        t = self.CheckCondition(Fish)
        if t < 3:
            self.desk.newmatrix[self.y][self.x] = Void(self.y, self.x, self.desk)
        elif t > 4:
            self.desk.newmatrix[self.y][self.x] = Void(self.y, self.x, self.desk)
        else:
            self.desk.newmatrix[self.y][self.x] = Fish(self.y, self.x, self.desk)


class Shrimp(ObjInterface):
    def Print(self):
        return "Shrimp"

    def Update(self):
        t = self.CheckCondition(Shrimp)
        if t < 3:
            self.desk.newmatrix[self.y][self.x] = Void(self.y, self.x, self.desk)
        elif t > 4:
            self.desk.newmatrix[self.y][self.x] = Void(self.y, self.x, self.desk)
        else:
            self.desk.newmatrix[self.y][self.x] = Shrimp(self.y, self.x, self.desk)


class Void(ObjInterface):
    def Print(self):
        return "Void"

    def Update(self):
        t = self.CheckCondition(Fish)
        if t == 3:
            self.desk.newmatrix[self.y][self.x] = Fish(self.y, self.x, self.desk)
        else:
            t = self.CheckCondition(Shrimp)
            if t == 3:
                self.desk.newmatrix[self.y][self.x] = Shrimp(self.y, self.x, self.desk)
            else:
                self.desk.newmatrix[self.y][self.x] = Void(self.y, self.x, self.desk)


class Rock(ObjInterface):
    def Print(self):
        return "Rock"

    def Update(self):
        self.desk.newmatrix[self.y][self.x] = Rock(self.y, self.x, self.desk)
