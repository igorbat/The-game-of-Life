
# coding: utf-8

# In[2]:


'a'.center(10)


# In[5]:


import collections


# In[6]:


class Desk:
    def __init__(self, height, weight):
        self.height = height + 2
        self.weight = weight + 2
        self.matrix = list()
        for i in range(self.height):
            self.matrix.append(list())
            for j in range(self.weight):
                self.matrix[i].append(list())
                self.matrix[i][j].append('n')
                self.matrix[i][j].append('n')
    
    def UpdateFish(self, y, x):
        t = 0
        if self.matrix[y-1][x][0] == 'f':
            t += 1
        if self.matrix[y-1][x-1][0] == 'f':
            t += 1
        if self.matrix[y-1][x+1][0] == 'f':
            t += 1
        if self.matrix[y][x-1][0] == 'f':
            t += 1
        if self.matrix[y][x+1][0] == 'f':
            t += 1
        if self.matrix[y+1][x+1][0] == 'f':
            t += 1
        if self.matrix[y+1][x][0] == 'f':
            t += 1
        if self.matrix[y+1][x-1][0] == 'f':
            t += 1
        if t < 2:
            self.matrix[y][x][1] = 'n'
        else:
            if t > 3:
                self.matrix[y][x][1] = 'n'
            else:
                self.matrix[y][x][1] = 'f'
    
    def UpdateShrimp(self, y, x):
        t = 0
        if self.matrix[y-1][x][0] == 's':
            t += 1
        if self.matrix[y-1][x-1][0] == 's':
            t += 1
        if self.matrix[y-1][x+1][0] == 's':
            t += 1
        if self.matrix[y][x-1][0] == 's':
            t += 1
        if self.matrix[y][x+1][0] == 's':
            t += 1
        if self.matrix[y+1][x+1][0] == 's':
            t += 1
        if self.matrix[y+1][x][0] == 's':
            t += 1
        if self.matrix[y+1][x-1][0] == 's':
            t += 1
        if t < 2:
            self.matrix[y][x][1] = 'n'
        else:
            if t > 3:
                self.matrix[y][x][1] = 'n'
            else:
                self.matrix[y][x][1] = 's'
    
    def UpdateVoid(self, y, x):
        t = 0
        if self.matrix[y-1][x][0] == 'f':
            t += 1
        if self.matrix[y-1][x-1][0] == 'f':
            t += 1
        if self.matrix[y-1][x+1][0] == 'f':
            t += 1
        if self.matrix[y][x-1][0] == 'f':
            t += 1
        if self.matrix[y][x+1][0] == 'f':
            t += 1
        if self.matrix[y+1][x+1][0] == 'f':
            t += 1
        if self.matrix[y+1][x][0] == 'f':
            t += 1
        if self.matrix[y+1][x-1][0] == 'f':
            t += 1
        if t == 3:
            self.matrix[y][x][1] = 'f'
        else:
            t = 0
            if self.matrix[y-1][x][0] == 's':
                t += 1
            if self.matrix[y-1][x-1][0] == 's':
                t += 1
            if self.matrix[y-1][x+1][0] == 's':
                t += 1
            if self.matrix[y][x-1][0] == 's':
                t += 1
            if self.matrix[y][x+1][0] == 's':
                t += 1
            if self.matrix[y+1][x+1][0] == 's':
                t += 1
            if self.matrix[y+1][x][0] == 's':
                t += 1
            if self.matrix[y+1][x-1][0] == 's':
                t += 1
            if t == 3:
                self.matrix[y][x][1] = 's'
            else:
                self.matrix[y][x][1] = 'n'
    
    def UpdateRock(self, y, x):
        self.matrix[y][x][1] = 'r'
        
    def Update(self, y, x):
        if self.matrix[y][x][0] == 'f':
            self.UpdateFish(y, x)
        elif self.matrix[y][x][0] == 'r':
            self.UpdateRock(y, x)
        elif self.matrix[y][x][0] == 'n':
            self.UpdateVoid(y, x)
        elif self.matrix[y][x][0] == 's':
            self.UpdateShrimp(y, x)
    
    def SetStringMatrix(self, y, st):
        for i in range(self.weight - 2):
            self.matrix[y][i+1][0] = st[i]
    
    def UpdateMatrix(self):
        for i in range(self.height-2):
            for j in range(self.weight-2):
                self.Update(i+1, j+1)
        for i in range(self.height-2):
            for j in range(self.weight-2):
                self.matrix[i+1][j+1][0] = self.matrix[i+1][j+1][1]
    
    def PrintCell(self, y, x):
        #here should be strange print for every type of life on cell|Rock is life too
        print(self.matrix[y][x][0], end="")
    
    def Print(self):
        for i in range(self.height-2):
            for j in range(self.weight-2):
                self.PrintCell(i+1, j+1)
            print("", end="\n")       
ls = input().split()        
matrix = Desk(int(ls[0]), int(ls[1]))
generations = int(ls[2])
for t in range(matrix.height - 2):
    s = input()
    matrix.SetStringMatrix(t+1, s)
while generations > 0:
    matrix.UpdateMatrix()
    generations -= 1
matrix.Print()        


# In[ ]:


3 3 1
nff
fff
fff
5 5 2
nffss
ffrrs
fffss
ssnss
frnnf

