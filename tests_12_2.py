import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()                          # Применили к участнику из списка метод run
                if participant.distance >= self.full_distance: # Если дистанция участника >= всей дистанции
                    finishers[place] = participant      # Добавили в список finishers place(ключ) и participant(значение)
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усейн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
          for result in cls.all_results.values():
            result_run = {}                       # создаем словари - списки забегов
            for place, runner in result.items():
                result_run[place] = runner.name        # в каждый словарь записываем место и участника
            print(result_run)


    def test_Tournament(self):
        self.tournament90 = Tournament(90, self.runner1, self.runner3)
        self.all_results = self.tournament90.start()                  #в словарь all_result записываем результат
        last_runner = self.all_results[max(self.all_results.keys())].name  # записываем имя с максимальным местом
        self.assertTrue(last_runner == 'Ник')  # сравниваем имя последнего участника
        TournamentTest.all_results[1] = self.all_results  # записываем словарь с ключом 1


    def test_Tournament2(self):
        self.tournament90 = Tournament(90, self.runner2, self.runner3)
        self.all_results = self.tournament90.start()  # в словарь all_result записываем результат
        last_runner = self.all_results[max(self.all_results.keys())].name  # записываем имя с максимальным местом
        self.assertTrue(last_runner == 'Ник')  # сравниваем имя последнего участника
        TournamentTest.all_results[2] = self.all_results  # записываем словарь с ключом 1

    def test_Tournament3(self):
        self.tournament90 = Tournament(90, self.runner1, self.runner2,  self.runner3)
        self.all_results = self.tournament90.start()  # в словарь all_result записываем результат
        last_runner = self.all_results[max(self.all_results.keys())].name  # записываем имя с максимальным местом
        self.assertTrue(last_runner == 'Ник')  # сравниваем имя последнего участника
        TournamentTest.all_results[3] = self.all_results  # записываем словарь с ключом 1



if __name__ == '__main__':
    unittest.main()




