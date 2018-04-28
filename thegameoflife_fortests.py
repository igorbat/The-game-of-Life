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
        raise Exception


class Desk:
    def __init__(self, height, weight):
        self.height = height + 2
        self.weight = weight + 2
        self.matrix = list()
        for i in range(self.height):
            self.matrix.append(list())
            for j in range(self.weight):
                self.matrix[i].append(list())
                self.matrix[i][j].append(Void(i, j, self))
                self.matrix[i][j].append(Void(i, j, self))

    def SetStringMatrix(self, y, st):
        for i in range(self.weight - 2):
            self.matrix[y][i+1][0] = Create(st[i], y, i+1, self)

    def UpdateMatrix(self):
        for i in range(self.height-2):
            for j in range(self.weight-2):
                self.matrix[i+1][j+1][0].Update()
        for i in range(self.height-2):
            for j in range(self.weight-2):
                self.matrix[i+1][j+1][0] = self.matrix[i+1][j+1][1]

    def Print(self, r):
        for i in range(self.height-2):
            s = ""
            for j in range(self.weight-2):
                s = s + self.matrix[i+1][j+1][0].Print()
            if r == 1:
                sys.stdout.write(s + "\n")
            else:
                print(s)


def modeling(g, q):
    if g == 1:
        generations = int(sys.stdin.readline())
        ls = sys.stdin.readline().split()
    else:
        generations = int(input())
        ls = input().split()
    matrix = Desk(int(ls[0]), int(ls[1]))
    for t in range(matrix.height - 2):
        if g == 1:
            s = sys.stdin.readline()
        else:
            s = input()
        matrix.SetStringMatrix(t+1, s)
    while generations > 0:
        matrix.UpdateMatrix()
        generations -= 1
    matrix.Print(q)


class ObjInterface:
    def __init__(self, ycoor, xcoor, deskc):
        self.x = xcoor
        self.y = ycoor
        self.desk = deskc

    def Update(self):
        pass

    def Print(self):
        pass


class Fish(ObjInterface):
    def Print(self):
        return 'f'

    def Update(self):
        t = 0
        for i in range(3):
            for j in range(3):
                if type(self.desk.matrix[self.y - 1 + i][self.x - 1 + j][0])\
                        == Fish:
                    t += 1
        if t < 3:
            self.desk.matrix[self.y][self.x][1] = Void(self.y, self.x,
                                                       self.desk)
        elif t > 4:
            self.desk.matrix[self.y][self.x][1] = Void(self.y, self.x,
                                                       self.desk)
        else:
            self.desk.matrix[self.y][self.x][1] = Fish(self.y, self.x,
                                                       self.desk)


class Shrimp(ObjInterface):
    def Print(self):
        return 's'

    def Update(self):
        t = 0
        for i in range(3):
            for j in range(3):
                if type(self.desk.matrix[self.y - 1 + i][self.x - 1 + j][0])\
                        == Shrimp:
                    t += 1
        if t < 3:
            self.desk.matrix[self.y][self.x][1] = Void(self.y, self.x,
                                                       self.desk)
        elif t > 4:
            self.desk.matrix[self.y][self.x][1] = Void(self.y, self.x,
                                                       self.desk)
        else:
            self.desk.matrix[self.y][self.x][1] = Shrimp(self.y, self.x,
                                                         self.desk)


class Void(ObjInterface):
    def Print(self):
        return '.'

    def Update(self):
        t = 0

        for i in range(3):
            for j in range(3):
                if type(self.desk.matrix[self.y - 1 + i][self.x - 1 + j][0])\
                        == Fish:
                    t += 1
        if t == 3:
            self.desk.matrix[self.y][self.x][1] = Fish(self.y, self.x,
                                                       self.desk)
        else:
            t = 0
            for i in range(3):
                for j in range(3):
                    if type(self.desk.matrix[self.y - 1 + i][self.x - 1 + j][0])\
                            == Shrimp:
                        t += 1
            if t == 3:
                self.desk.matrix[self.y][self.x][1] = Shrimp(self.y, self.x,
                                                             self.desk)
            else:
                self.desk.matrix[self.y][self.x][1] = Void(self.y, self.x,
                                                           self.desk)


class Rock(ObjInterface):
    def Print(self):
        return '#'

    def Update(self):
        self.desk.matrix[self.y][self.x][1] = Rock(self.y, self.x,
                                                   self.desk)



