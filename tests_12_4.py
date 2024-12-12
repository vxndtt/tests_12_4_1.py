import logging
import unittest
import rt_with_exceptions


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner = rt_with_exceptions.Runner('Sasha', -5)
            for i in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('test_walk выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner = rt_with_exceptions.Runner(5)
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('Неверный тип данных для объекта Runner')
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = rt_with_exceptions.Runner('Katya')
        runner2 = rt_with_exceptions.Runner('Igor')
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()
