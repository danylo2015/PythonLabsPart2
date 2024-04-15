import unittest
from src.penguins_need_gas import *


class TestPenguinsNeedGas(unittest.TestCase):

    def test_check_gas_supply_default(self):
        cities = ['Львів', 'Стрий', 'Долина']
        gas_storages = ['Сховище_1', 'Сховище_2']
        pipelines = [['Львів', 'Стрий'], ['Долина', 'Львів'], ['Сховище_1', 'Сховище_2']]

        res = check_gas_supply(cities, gas_storages, pipelines)
        self.assertEqual(res, [['Сховище_1', ['Львів', 'Стрий', 'Долина']], ['Сховище_2', ['Львів', 'Стрий', 'Долина']]])

    def test_gas_is_empty(self):
        cities = []
        gas_storages = []
        pipelines = []

        res = check_gas_supply(cities, gas_storages, pipelines)
        self.assertEqual(res, [])

    def test_gas_supply_to_all(self):
        cities = ['Львів', 'Стрий', 'Долина']
        gas_storages = ['Сховище_1', 'Сховище_2']
        pipelines = [['Львів', 'Стрий'], ['Долина', 'Львів'], ['Сховище_1', 'Сховище_2'],
                     ['Долина', 'Стрий'], ['Сховище_2', 'Львів'], ['Стрий', 'Долина']]

        res = check_gas_supply(cities, gas_storages, pipelines)
        self.assertEqual(res, [])
