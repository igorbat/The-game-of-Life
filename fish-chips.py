
# coding: utf-8

# In[10]:


class Cell:
    def __init__(self, sType):
        self.specie = sType
        top = self
        bot = self
        right = self
        left = self
    def UpdateFish(self):
        t = 0
        if (top.specie == 'f'):
            t += 1
        if (left.specie == 'f'):
            t += 1
        if (right.specie == 'f'):
            t += 1
        if (bot.specie == 'f'):
            t += 1
        if(t)
    #def UpdateVoid:
        
    def UpdateRock:
        pass
    def Update(self):
        if self.specie:
            self.UpdateFish()
        elif self.specie == '#':
            self.UpdateRock()
        elif self.specie
    def Check(self):
        self.specie = self.newspecie
class Desk:
    height = 12
    weight = 12
    def SetHeight(self, count):
        self.height = count+2
    def SetWeight(self, count):
        self.weight = count+2
    def SetMatrix(self):
        self.matrix = list()
        for i in range(self.height):
            self.matrix.append(list())
            for j in range(self.weight):
                self.matrix[i].append(Cell('.'))
        for i in range(self.height-2):
            for j in range(self.weight-2):
                self.matrix[i+1][j+1].left = &self.matrix[i+1][j]
                self.matrix[i+1][j+1].right = &self.matrix[i+1][j+2]
                self.matrix[i+1][j+1].top = &self.matrix[i][j+1]
                self.matrix[i+1][j+1].bot = &self.matrix[i+2][j+1]
    def SetStringMatrix(self, y, st):
        for i in range(self.weight - 2):
            self.matrix[y][i+1].specie = st[i]

    def UpdateMatrix(self):
        for i in range(self.height-2):
            for j in range(self.weight-2):
                self.matrix[i+1][j+1].Update()
                self.matrix[i+1][j+1].Check()
    def Print(self):
        for i in range(self.height-2):
            for j in range(self.weight-2):
                print(self.matrix[i+1][j+1], end="")
            print("", end="\n")
        


# In[11]:


generations = int(input())        
ls = input().split()        
matrix = Desk()
matrix.SetHeight(int(ls[0]))
matrix.SetWeight(int(ls[1]))
matrix.SetMatrix()
for t in range(matrix.height - 2):
    s = input()
    matrix.SetStringMatrix(t+1, s)
while generations > 0:
    matrix.UpdateMatrix()
    generations -= 1
matrix.Print()


# In[ ]:


#checker_coordinates_of_ceils

#checker_types_of_ceils

#checker_table_sizes

#check_zero

#check_1xN_Mx1

#check_rock_table

