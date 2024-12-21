import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        self.walker = Runner('First')
        for i in range(10):
            self.walker.walk()
        self.assertEqual(self.walker.distance, 50)


    def test_run(self):
        self.runner = Runner('Second')
        for i in range(10):
            self.runner.run()
        self.assertEqual(self.runner.distance, 100)


    def test_challenge(self):
        self.run1 = Runner('run1')
        self.run2 = Runner('run2')
        for i in range(10):
            self.run1.run()
        for i in range(10):
            self.run2.walk()
        self.assertNotEqual(self.run1.distance, self.run2.distance)

if __name__ == '__main__':
    unittest.main()