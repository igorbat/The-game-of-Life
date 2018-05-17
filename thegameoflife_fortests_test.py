import unittest
from thegameoflife_fortests import *


class TestCaseForFish(unittest.TestCase):
    def test_fish_1(self):
        desk = Desk(3, 3)
        desk.matrix[2][2] = Shrimp(2, 2, desk)

        desk.matrix[1][1] = Shrimp(1, 1, desk)
        desk.matrix[1][2] = Shrimp(1, 2, desk)
        desk.matrix[1][3] = Shrimp(1, 3, desk)
        desk.matrix[2][1] = Void(2, 1, desk)
        desk.matrix[2][3] = Void(2, 3, desk)
        desk.matrix[3][1] = Fish(3, 1, desk)
        desk.matrix[3][2] = Rock(3, 2, desk)
        desk.matrix[3][3] = Rock(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2]) == Shrimp)

    def test_fish_2(self):
        desk = Desk(3, 3)
        desk.matrix[2][2] = Shrimp(2, 2, desk)

        desk.matrix[1][1] = Fish(1, 1, desk)
        desk.matrix[1][2] = Shrimp(1, 2, desk)
        desk.matrix[1][3] = Fish(1, 3, desk)
        desk.matrix[2][1] = Void(2, 1, desk)
        desk.matrix[2][3] = Void(2, 3, desk)
        desk.matrix[3][1] = Fish(3, 1, desk)
        desk.matrix[3][2] = Rock(3, 2, desk)
        desk.matrix[3][3] = Rock(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2]) == Void)

    def test_fish_3(self):
        desk = Desk(3, 3)
        desk.matrix[2][2] = Shrimp(2, 2, desk)

        desk.matrix[1][1] = Shrimp(1, 1, desk)
        desk.matrix[1][2] = Shrimp(1, 2, desk)
        desk.matrix[1][3] = Void(1, 3, desk)
        desk.matrix[2][1] = Void(2, 1, desk)
        desk.matrix[2][3] = Void(2, 3, desk)
        desk.matrix[3][1] = Fish(3, 1, desk)
        desk.matrix[3][2] = Shrimp(3, 2, desk)
        desk.matrix[3][3] = Shrimp(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2]) == Void)

    def test_fish_4(self):
        desk = Desk(3, 3)
        desk.matrix[2][2] = Shrimp(2, 2, desk)

        desk.matrix[1][1] = Shrimp(1, 1, desk)
        desk.matrix[1][2] = Shrimp(1, 2, desk)
        desk.matrix[1][3] = Void(1, 3, desk)
        desk.matrix[2][1] = Void(2, 1, desk)
        desk.matrix[2][3] = Void(2, 3, desk)
        desk.matrix[3][1] = Fish(3, 1, desk)
        desk.matrix[3][2] = Shrimp(3, 2, desk)
        desk.matrix[3][3] = Rock(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2]) == Shrimp)


class TestCaseForShrimp(unittest.TestCase):
    def test_shrimp_1(self):
        desk = Desk(3, 3)
        desk.matrix[2][2] = Shrimp(2, 2, desk)

        desk.matrix[1][1] = Shrimp(1, 1, desk)
        desk.matrix[1][2] = Shrimp(1, 2, desk)
        desk.matrix[1][3] = Shrimp(1, 3, desk)
        desk.matrix[2][1] = Void(2, 1, desk)
        desk.matrix[2][3] = Void(2, 3, desk)
        desk.matrix[3][1] = Fish(3, 1, desk)
        desk.matrix[3][2] = Rock(3, 2, desk)
        desk.matrix[3][3] = Rock(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2]) == Shrimp)

    def test_shrimp_2(self):
        desk = Desk(3, 3)
        desk.matrix[2][2] = Shrimp(2, 2, desk)

        desk.matrix[1][1] = Fish(1, 1, desk)
        desk.matrix[1][2] = Shrimp(1, 2, desk)
        desk.matrix[1][3] = Fish(1, 3, desk)
        desk.matrix[2][1] = Void(2, 1, desk)
        desk.matrix[2][3] = Void(2, 3, desk)
        desk.matrix[3][1] = Fish(3, 1, desk)
        desk.matrix[3][2] = Rock(3, 2, desk)
        desk.matrix[3][3] = Rock(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2]) == Void)

    def test_shrimp_3(self):
        desk = Desk(3, 3)
        desk.matrix[2][2] = Shrimp(2, 2, desk)

        desk.matrix[1][1] = Shrimp(1, 1, desk)
        desk.matrix[1][2] = Shrimp(1, 2, desk)
        desk.matrix[1][3] = Void(1, 3, desk)
        desk.matrix[2][1] = Void(2, 1, desk)
        desk.matrix[2][3] = Void(2, 3, desk)
        desk.matrix[3][1] = Fish(3, 1, desk)
        desk.matrix[3][2] = Shrimp(3, 2, desk)
        desk.matrix[3][3] = Shrimp(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2]) == Void)

    def test_shrimp_4(self):
        desk = Desk(3, 3)
        desk.matrix[2][2] = Shrimp(2, 2, desk)

        desk.matrix[1][1] = Shrimp(1, 1, desk)
        desk.matrix[1][2] = Shrimp(1, 2, desk)
        desk.matrix[1][3] = Void(1, 3, desk)
        desk.matrix[2][1] = Void(2, 1, desk)
        desk.matrix[2][3] = Void(2, 3, desk)
        desk.matrix[3][1] = Fish(3, 1, desk)
        desk.matrix[3][2] = Shrimp(3, 2, desk)
        desk.matrix[3][3] = Rock(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2]) == Shrimp)


class TestCaseForVoid(unittest.TestCase):
    def test_void_1(self):
        desk = Desk(3, 3)
        desk.matrix[2][2] = Void(2, 2, desk)

        desk.matrix[1][1] = Shrimp(1, 1, desk)
        desk.matrix[1][2] = Shrimp(1, 2, desk)
        desk.matrix[1][3] = Void(1, 3, desk)
        desk.matrix[2][1] = Void(2, 1, desk)
        desk.matrix[2][3] = Fish(2, 3, desk)
        desk.matrix[3][1] = Fish(3, 1, desk)
        desk.matrix[3][2] = Fish(3, 2, desk)
        desk.matrix[3][3] = Fish(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2]) == Void)

    def test_void_2(self):
        desk = Desk(3, 3)
        desk.matrix[2][2] = Void(2, 2, desk)

        desk.matrix[1][1] = Fish(1, 1, desk)
        desk.matrix[1][2] = Shrimp(1, 2, desk)
        desk.matrix[1][3] = Fish(1, 3, desk)
        desk.matrix[2][1] = Void(2, 1, desk)
        desk.matrix[2][3] = Void(2, 3, desk)
        desk.matrix[3][1] = Fish(3, 1, desk)
        desk.matrix[3][2] = Rock(3, 2, desk)
        desk.matrix[3][3] = Rock(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2]) == Fish)

    def test_void_3(self):
        desk = Desk(3, 3)
        desk.matrix[2][2] = Void(2, 2, desk)

        desk.matrix[1][1] = Shrimp(1, 1, desk)
        desk.matrix[1][2] = Shrimp(1, 2, desk)
        desk.matrix[1][3] = Void(1, 3, desk)
        desk.matrix[2][1] = Void(2, 1, desk)
        desk.matrix[2][3] = Void(2, 3, desk)
        desk.matrix[3][1] = Fish(3, 1, desk)
        desk.matrix[3][2] = Shrimp(3, 2, desk)
        desk.matrix[3][3] = Fish(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2]) == Shrimp)

    def test_void_4(self):
        desk = Desk(3, 3)
        desk.matrix[2][2] = Void(2, 2, desk)

        desk.matrix[1][1] = Shrimp(1, 1, desk)
        desk.matrix[1][2] = Shrimp(1, 2, desk)
        desk.matrix[1][3] = Fish(1, 3, desk)
        desk.matrix[2][1] = Void(2, 1, desk)
        desk.matrix[2][3] = Void(2, 3, desk)
        desk.matrix[3][1] = Fish(3, 1, desk)
        desk.matrix[3][2] = Shrimp(3, 2, desk)
        desk.matrix[3][3] = Fish(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2]) == Fish)


class TestCaseForRock(unittest.TestCase):
    def test_rock_1(self):
        desk = Desk(3, 3)
        desk.matrix[2][2] = Rock(2, 2, desk)

        desk.matrix[1][1] = Shrimp(1, 1, desk)
        desk.matrix[1][2] = Shrimp(1, 2, desk)
        desk.matrix[1][3] = Shrimp(1, 3, desk)
        desk.matrix[2][1] = Void(2, 1, desk)
        desk.matrix[2][3] = Void(2, 3, desk)
        desk.matrix[3][1] = Fish(3, 1, desk)
        desk.matrix[3][2] = Rock(3, 2, desk)
        desk.matrix[3][3] = Rock(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2]) == Rock)

    def test_rock_2(self):
        desk = Desk(3, 3)
        desk.matrix[2][2] = Rock(2, 2, desk)

        desk.matrix[1][1] = Fish(1, 1, desk)
        desk.matrix[1][2] = Shrimp(1, 2, desk)
        desk.matrix[1][3] = Fish(1, 3, desk)
        desk.matrix[2][1] = Void(2, 1, desk)
        desk.matrix[2][3] = Void(2, 3, desk)
        desk.matrix[3][1] = Fish(3, 1, desk)
        desk.matrix[3][2] = Rock(3, 2, desk)
        desk.matrix[3][3] = Rock(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2]) == Rock)

    def test_rock_3(self):
        desk = Desk(3, 3)
        desk.matrix[2][2] = Rock(2, 2, desk)

        desk.matrix[1][1] = Shrimp(1, 1, desk)
        desk.matrix[1][2] = Shrimp(1, 2, desk)
        desk.matrix[1][3] = Void(1, 3, desk)
        desk.matrix[2][1] = Void(2, 1, desk)
        desk.matrix[2][3] = Void(2, 3, desk)
        desk.matrix[3][1] = Fish(3, 1, desk)
        desk.matrix[3][2] = Shrimp(3, 2, desk)
        desk.matrix[3][3] = Shrimp(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2]) == Rock)

    def test_rock_4(self):
        desk = Desk(3, 3)
        desk.matrix[2][2] = Rock(2, 2, desk)

        desk.matrix[1][1] = Shrimp(1, 1, desk)
        desk.matrix[1][2] = Shrimp(1, 2, desk)
        desk.matrix[1][3] = Void(1, 3, desk)
        desk.matrix[2][1] = Void(2, 1, desk)
        desk.matrix[2][3] = Void(2, 3, desk)
        desk.matrix[3][1] = Fish(3, 1, desk)
        desk.matrix[3][2] = Shrimp(3, 2, desk)
        desk.matrix[3][3] = Rock(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2]) == Rock)


class TestCaseForPrint(unittest.TestCase):
    def test_void(self):
        desk = Desk(1, 1)
        desk.matrix[1][1] = Void(1, 1, desk)
        t = desk.matrix[1][1].Print()
        self.assertTrue(t == "Void")

    def test_rock(self):
        desk = Desk(1, 1)
        desk.matrix[1][1] = Rock(1, 1, desk)
        t = desk.matrix[1][1].Print()
        self.assertTrue(t == "Rock")

    def test_fish(self):
        desk = Desk(1, 1)
        desk.matrix[1][1] = Fish(1, 1, desk)
        t = desk.matrix[1][1].Print()
        self.assertTrue(t == "Fish")

    def test_shrimp(self):
        desk = Desk(1, 1)
        desk.matrix[1][1] = Shrimp(1, 1, desk)
        t = desk.matrix[1][1].Print()
        self.assertTrue(t == "Shrimp")


class TestCaseForGenerations(unittest.TestCase):
    def test_1(self):
        desk = Desk(3, 3)
        desk.matrix[2][2] = Fish(2, 2, desk)

        desk.matrix[1][1] = Fish(1, 1, desk)
        desk.matrix[1][2] = Fish(1, 2, desk)
        desk.matrix[1][3] = Fish(1, 3, desk)
        desk.matrix[2][1] = Fish(2, 1, desk)
        desk.matrix[2][3] = Fish(2, 3, desk)
        desk.matrix[3][1] = Fish(3, 1, desk)
        desk.matrix[3][2] = Fish(3, 2, desk)
        desk.matrix[3][3] = Rock(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[3][3]) == Rock)
        self.assertTrue(type(desk.matrix[1][3]) == Fish)
        self.assertTrue(type(desk.matrix[2][3]) == Void)
        self.assertTrue(type(desk.matrix[1][2]) == Void)
        self.assertTrue(type(desk.matrix[2][2]) == Void)
        self.assertTrue(type(desk.matrix[3][2]) == Void)
        self.assertTrue(type(desk.matrix[1][1]) == Fish)
        self.assertTrue(type(desk.matrix[2][1]) == Void)
        self.assertTrue(type(desk.matrix[3][1]) == Fish)

        def test_2(self):
            desk = Desk(3, 3)
            desk.matrix[2][2] = Fish(2, 2, desk)

            desk.matrix[1][1] = Fish(1, 1, desk)
            desk.matrix[1][2] = Fish(1, 2, desk)
            desk.matrix[1][3] = Fish(1, 3, desk)
            desk.matrix[2][1] = Fish(2, 1, desk)
            desk.matrix[2][3] = Fish(2, 3, desk)
            desk.matrix[3][1] = Fish(3, 1, desk)
            desk.matrix[3][2] = Fish(3, 2, desk)
            desk.matrix[3][3] = Rock(3, 3, desk)
            desk.UpdateMatrix()
            desk.UpdateMatrix()
            self.assertTrue(type(desk.matrix[3][3]) == Rock)
            self.assertTrue(type(desk.matrix[1][3]) == Void)
            self.assertTrue(type(desk.matrix[2][3]) == Void)
            self.assertTrue(type(desk.matrix[1][2]) == Void)
            self.assertTrue(type(desk.matrix[2][2]) == Void)
            self.assertTrue(type(desk.matrix[3][2]) == Void)
            self.assertTrue(type(desk.matrix[1][1]) == Void)
            self.assertTrue(type(desk.matrix[2][1]) == Void)
            self.assertTrue(type(desk.matrix[3][1]) == Void)


if __name__ == '__main__':
    unittest.main()
