import unittest
from thegameoflife_fortests import *


class TestCaseForFish(unittest.TestCase):
    def test_fish_1(self):
        desk = Desk(3, 3)
        desk.matrix[2][2][0] = Shrimp(2, 2, desk)

        desk.matrix[1][1][0] = Shrimp(1, 1, desk)
        desk.matrix[1][2][0] = Shrimp(1, 2, desk)
        desk.matrix[1][3][0] = Shrimp(1, 3, desk)
        desk.matrix[2][1][0] = Void(2, 1, desk)
        desk.matrix[2][3][0] = Void(2, 3, desk)
        desk.matrix[3][1][0] = Fish(3, 1, desk)
        desk.matrix[3][2][0] = Rock(3, 2, desk)
        desk.matrix[3][3][0] = Rock(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2][0]) == Shrimp)

    def test_fish_2(self):
        desk = Desk(3, 3)
        desk.matrix[2][2][0] = Shrimp(2, 2, desk)

        desk.matrix[1][1][0] = Fish(1, 1, desk)
        desk.matrix[1][2][0] = Shrimp(1, 2, desk)
        desk.matrix[1][3][0] = Fish(1, 3, desk)
        desk.matrix[2][1][0] = Void(2, 1, desk)
        desk.matrix[2][3][0] = Void(2, 3, desk)
        desk.matrix[3][1][0] = Fish(3, 1, desk)
        desk.matrix[3][2][0] = Rock(3, 2, desk)
        desk.matrix[3][3][0] = Rock(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2][0]) == Void)

    def test_fish_3(self):
        desk = Desk(3, 3)
        desk.matrix[2][2][0] = Shrimp(2, 2, desk)

        desk.matrix[1][1][0] = Shrimp(1, 1, desk)
        desk.matrix[1][2][0] = Shrimp(1, 2, desk)
        desk.matrix[1][3][0] = Void(1, 3, desk)
        desk.matrix[2][1][0] = Void(2, 1, desk)
        desk.matrix[2][3][0] = Void(2, 3, desk)
        desk.matrix[3][1][0] = Fish(3, 1, desk)
        desk.matrix[3][2][0] = Shrimp(3, 2, desk)
        desk.matrix[3][3][0] = Shrimp(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2][0]) == Void)

    def test_fish_4(self):
        desk = Desk(3, 3)
        desk.matrix[2][2][0] = Shrimp(2, 2, desk)

        desk.matrix[1][1][0] = Shrimp(1, 1, desk)
        desk.matrix[1][2][0] = Shrimp(1, 2, desk)
        desk.matrix[1][3][0] = Void(1, 3, desk)
        desk.matrix[2][1][0] = Void(2, 1, desk)
        desk.matrix[2][3][0] = Void(2, 3, desk)
        desk.matrix[3][1][0] = Fish(3, 1, desk)
        desk.matrix[3][2][0] = Shrimp(3, 2, desk)
        desk.matrix[3][3][0] = Rock(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2][0]) == Shrimp)


class TestCaseForShrimp(unittest.TestCase):
    def test_shrimp_1(self):
        desk = Desk(3, 3)
        desk.matrix[2][2][0] = Shrimp(2, 2, desk)

        desk.matrix[1][1][0] = Shrimp(1, 1, desk)
        desk.matrix[1][2][0] = Shrimp(1, 2, desk)
        desk.matrix[1][3][0] = Shrimp(1, 3, desk)
        desk.matrix[2][1][0] = Void(2, 1, desk)
        desk.matrix[2][3][0] = Void(2, 3, desk)
        desk.matrix[3][1][0] = Fish(3, 1, desk)
        desk.matrix[3][2][0] = Rock(3, 2, desk)
        desk.matrix[3][3][0] = Rock(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2][0]) == Shrimp)

    def test_shrimp_2(self):
        desk = Desk(3, 3)
        desk.matrix[2][2][0] = Shrimp(2, 2, desk)

        desk.matrix[1][1][0] = Fish(1, 1, desk)
        desk.matrix[1][2][0] = Shrimp(1, 2, desk)
        desk.matrix[1][3][0] = Fish(1, 3, desk)
        desk.matrix[2][1][0] = Void(2, 1, desk)
        desk.matrix[2][3][0] = Void(2, 3, desk)
        desk.matrix[3][1][0] = Fish(3, 1, desk)
        desk.matrix[3][2][0] = Rock(3, 2, desk)
        desk.matrix[3][3][0] = Rock(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2][0]) == Void)

    def test_shrimp_3(self):
        desk = Desk(3, 3)
        desk.matrix[2][2][0] = Shrimp(2, 2, desk)

        desk.matrix[1][1][0] = Shrimp(1, 1, desk)
        desk.matrix[1][2][0] = Shrimp(1, 2, desk)
        desk.matrix[1][3][0] = Void(1, 3, desk)
        desk.matrix[2][1][0] = Void(2, 1, desk)
        desk.matrix[2][3][0] = Void(2, 3, desk)
        desk.matrix[3][1][0] = Fish(3, 1, desk)
        desk.matrix[3][2][0] = Shrimp(3, 2, desk)
        desk.matrix[3][3][0] = Shrimp(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2][0]) == Void)

    def test_shrimp_4(self):
        desk = Desk(3, 3)
        desk.matrix[2][2][0] = Shrimp(2, 2, desk)

        desk.matrix[1][1][0] = Shrimp(1, 1, desk)
        desk.matrix[1][2][0] = Shrimp(1, 2, desk)
        desk.matrix[1][3][0] = Void(1, 3, desk)
        desk.matrix[2][1][0] = Void(2, 1, desk)
        desk.matrix[2][3][0] = Void(2, 3, desk)
        desk.matrix[3][1][0] = Fish(3, 1, desk)
        desk.matrix[3][2][0] = Shrimp(3, 2, desk)
        desk.matrix[3][3][0] = Rock(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2][0]) == Shrimp)


class TestCaseForVoid(unittest.TestCase):
    def test_void_1(self):
        desk = Desk(3, 3)
        desk.matrix[2][2][0] = Void(2, 2, desk)

        desk.matrix[1][1][0] = Shrimp(1, 1, desk)
        desk.matrix[1][2][0] = Shrimp(1, 2, desk)
        desk.matrix[1][3][0] = Void(1, 3, desk)
        desk.matrix[2][1][0] = Void(2, 1, desk)
        desk.matrix[2][3][0] = Fish(2, 3, desk)
        desk.matrix[3][1][0] = Fish(3, 1, desk)
        desk.matrix[3][2][0] = Fish(3, 2, desk)
        desk.matrix[3][3][0] = Fish(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2][0]) == Void)

    def test_void_2(self):
        desk = Desk(3, 3)
        desk.matrix[2][2][0] = Void(2, 2, desk)

        desk.matrix[1][1][0] = Fish(1, 1, desk)
        desk.matrix[1][2][0] = Shrimp(1, 2, desk)
        desk.matrix[1][3][0] = Fish(1, 3, desk)
        desk.matrix[2][1][0] = Void(2, 1, desk)
        desk.matrix[2][3][0] = Void(2, 3, desk)
        desk.matrix[3][1][0] = Fish(3, 1, desk)
        desk.matrix[3][2][0] = Rock(3, 2, desk)
        desk.matrix[3][3][0] = Rock(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2][0]) == Fish)

    def test_void_3(self):
        desk = Desk(3, 3)
        desk.matrix[2][2][0] = Void(2, 2, desk)

        desk.matrix[1][1][0] = Shrimp(1, 1, desk)
        desk.matrix[1][2][0] = Shrimp(1, 2, desk)
        desk.matrix[1][3][0] = Void(1, 3, desk)
        desk.matrix[2][1][0] = Void(2, 1, desk)
        desk.matrix[2][3][0] = Void(2, 3, desk)
        desk.matrix[3][1][0] = Fish(3, 1, desk)
        desk.matrix[3][2][0] = Shrimp(3, 2, desk)
        desk.matrix[3][3][0] = Fish(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2][0]) == Shrimp)

    def test_void_4(self):
        desk = Desk(3, 3)
        desk.matrix[2][2][0] = Void(2, 2, desk)

        desk.matrix[1][1][0] = Shrimp(1, 1, desk)
        desk.matrix[1][2][0] = Shrimp(1, 2, desk)
        desk.matrix[1][3][0] = Fish(1, 3, desk)
        desk.matrix[2][1][0] = Void(2, 1, desk)
        desk.matrix[2][3][0] = Void(2, 3, desk)
        desk.matrix[3][1][0] = Fish(3, 1, desk)
        desk.matrix[3][2][0] = Shrimp(3, 2, desk)
        desk.matrix[3][3][0] = Fish(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2][0]) == Fish)


class TestCaseForRock(unittest.TestCase):
    def test_rock_1(self):
        desk = Desk(3, 3)
        desk.matrix[2][2][0] = Rock(2, 2, desk)

        desk.matrix[1][1][0] = Shrimp(1, 1, desk)
        desk.matrix[1][2][0] = Shrimp(1, 2, desk)
        desk.matrix[1][3][0] = Shrimp(1, 3, desk)
        desk.matrix[2][1][0] = Void(2, 1, desk)
        desk.matrix[2][3][0] = Void(2, 3, desk)
        desk.matrix[3][1][0] = Fish(3, 1, desk)
        desk.matrix[3][2][0] = Rock(3, 2, desk)
        desk.matrix[3][3][0] = Rock(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2][0]) == Rock)

    def test_rock_2(self):
        desk = Desk(3, 3)
        desk.matrix[2][2][0] = Rock(2, 2, desk)

        desk.matrix[1][1][0] = Fish(1, 1, desk)
        desk.matrix[1][2][0] = Shrimp(1, 2, desk)
        desk.matrix[1][3][0] = Fish(1, 3, desk)
        desk.matrix[2][1][0] = Void(2, 1, desk)
        desk.matrix[2][3][0] = Void(2, 3, desk)
        desk.matrix[3][1][0] = Fish(3, 1, desk)
        desk.matrix[3][2][0] = Rock(3, 2, desk)
        desk.matrix[3][3][0] = Rock(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2][0]) == Rock)

    def test_rock_3(self):
        desk = Desk(3, 3)
        desk.matrix[2][2][0] = Rock(2, 2, desk)

        desk.matrix[1][1][0] = Shrimp(1, 1, desk)
        desk.matrix[1][2][0] = Shrimp(1, 2, desk)
        desk.matrix[1][3][0] = Void(1, 3, desk)
        desk.matrix[2][1][0] = Void(2, 1, desk)
        desk.matrix[2][3][0] = Void(2, 3, desk)
        desk.matrix[3][1][0] = Fish(3, 1, desk)
        desk.matrix[3][2][0] = Shrimp(3, 2, desk)
        desk.matrix[3][3][0] = Shrimp(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2][0]) == Rock)

    def test_rock_4(self):
        desk = Desk(3, 3)
        desk.matrix[2][2][0] = Rock(2, 2, desk)

        desk.matrix[1][1][0] = Shrimp(1, 1, desk)
        desk.matrix[1][2][0] = Shrimp(1, 2, desk)
        desk.matrix[1][3][0] = Void(1, 3, desk)
        desk.matrix[2][1][0] = Void(2, 1, desk)
        desk.matrix[2][3][0] = Void(2, 3, desk)
        desk.matrix[3][1][0] = Fish(3, 1, desk)
        desk.matrix[3][2][0] = Shrimp(3, 2, desk)
        desk.matrix[3][3][0] = Rock(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[2][2][0]) == Rock)


class TestCaseForPrint(unittest.TestCase):
    def test_void(self):
        desk = Desk(1, 1)
        desk.matrix[1][1][0] = Void(1, 1, desk)
        t = desk.matrix[1][1][0].Print()
        self.assertTrue(t == ".")

    def test_rock(self):
        desk = Desk(1, 1)
        desk.matrix[1][1][0] = Rock(1, 1, desk)
        t = desk.matrix[1][1][0].Print()
        self.assertTrue(t == "#")

    def test_fish(self):
        desk = Desk(1, 1)
        desk.matrix[1][1][0] = Fish(1, 1, desk)
        t = desk.matrix[1][1][0].Print()
        self.assertTrue(t == "f")

    def test_shrimp(self):
        desk = Desk(1, 1)
        desk.matrix[1][1][0] = Shrimp(1, 1, desk)
        t = desk.matrix[1][1][0].Print()
        self.assertTrue(t == "s")


class TestCaseForGenerations(unittest.TestCase):
    def test_1(self):
        desk = Desk(3, 3)
        desk.matrix[2][2][0] = Fish(2, 2, desk)

        desk.matrix[1][1][0] = Fish(1, 1, desk)
        desk.matrix[1][2][0] = Fish(1, 2, desk)
        desk.matrix[1][3][0] = Fish(1, 3, desk)
        desk.matrix[2][1][0] = Fish(2, 1, desk)
        desk.matrix[2][3][0] = Fish(2, 3, desk)
        desk.matrix[3][1][0] = Fish(3, 1, desk)
        desk.matrix[3][2][0] = Fish(3, 2, desk)
        desk.matrix[3][3][0] = Rock(3, 3, desk)
        desk.UpdateMatrix()
        self.assertTrue(type(desk.matrix[3][3][0]) == Rock and
                        type(desk.matrix[1][3][0]) == Fish and
                        type(desk.matrix[2][3][0]) == Void and
                        type(desk.matrix[1][2][0]) == Void and
                        type(desk.matrix[2][2][0]) == Void and
                        type(desk.matrix[3][2][0]) == Void and
                        type(desk.matrix[1][1][0]) == Fish and
                        type(desk.matrix[2][1][0]) == Void and
                        type(desk.matrix[3][1][0]) == Fish)

        def test_2(self):
            desk = Desk(3, 3)
            desk.matrix[2][2][0] = Fish(2, 2, desk)

            desk.matrix[1][1][0] = Fish(1, 1, desk)
            desk.matrix[1][2][0] = Fish(1, 2, desk)
            desk.matrix[1][3][0] = Fish(1, 3, desk)
            desk.matrix[2][1][0] = Fish(2, 1, desk)
            desk.matrix[2][3][0] = Fish(2, 3, desk)
            desk.matrix[3][1][0] = Fish(3, 1, desk)
            desk.matrix[3][2][0] = Fish(3, 2, desk)
            desk.matrix[3][3][0] = Rock(3, 3, desk)
            desk.UpdateMatrix()
            desk.UpdateMatrix()
            self.assertTrue(type(desk.matrix[3][3][0]) == Rock and
                            type(desk.matrix[1][3][0]) == Void and
                            type(desk.matrix[2][3][0]) == Void and
                            type(desk.matrix[1][2][0]) == Void and
                            type(desk.matrix[2][2][0]) == Void and
                            type(desk.matrix[3][2][0]) == Void and
                            type(desk.matrix[1][1][0]) == Void and
                            type(desk.matrix[2][1][0]) == Void and
                            type(desk.matrix[3][1][0]) == Void)


if __name__ == '__main__':
    unittest.main()