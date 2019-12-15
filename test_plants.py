from plants import *
import unittest
import heapq

class TestScheduler(unittest.TestCase):

    def setUp(self):
        self.schedule = [None] * 12*7

    def test_assign_0(self):
        assign(self.schedule,"Croton",0)
        self.assertEqual(self.schedule[0],"Croton")

    def test_assign_1(self):
        assign(self.schedule,"Croton",0)
        assign(self.schedule,"Dracaena",0)
        self.assertEqual(self.schedule[0],"Croton, Dracaena")

    def test_scheduler_2_days(self):
        self.plants = [
            {
                "name": "A",
                "water_after": "2 days"
            },
        ]
        scheduler(self.plants,self.schedule)
        solution = ['A',None,'A',None,'A',None,None,'A','A',None,'A','A',None,None]
        for i in range(0,len(solution)):
            self.assertEqual(self.schedule[i],solution[i])

    def test_scheduler_3_days(self):
        self.plants = [
            {
                "name": "A",
                "water_after": "3 days"
            },
        ]
        scheduler(self.plants,self.schedule)
        solution = ['A',None,None,'A',None,None,None,'A',None,'A',None,'A',None,None]
        for i in range(0,len(solution)):
            self.assertEqual(self.schedule[i],solution[i])

    def test_scheduler_4_days(self):
        self.plants = [
            {
                "name": "A",
                "water_after": "4 days"
            },
        ]
        scheduler(self.plants,self.schedule)
        solution = ['A',None,None,None,'A',None,None,None,'A',None,None,'A',None,None]
        for i in range(0,len(solution)):
            self.assertEqual(self.schedule[i],solution[i])

    def test_scheduler_5_days(self):
        self.plants = [
            {
                "name": "A",
                "water_after": "5 days"
            },
        ]
        scheduler(self.plants,self.schedule)
        solution = ['A',None,None,None,'A',None,None,None,None,None,'A',None,None,None]
        for i in range(0,len(solution)):
            self.assertEqual(self.schedule[i],solution[i])

    def test_scheduler_6_days(self):
        self.plants = [
            {
                "name": "A",
                "water_after": "6 days"
            },
        ]
        scheduler(self.plants,self.schedule)
        solution = ['A',None,None,None,None,None,None,'A',None,None,None,'A',None,None]
        for i in range(0,len(solution)):
            self.assertEqual(self.schedule[i],solution[i])

    def test_scheduler_7_days(self):
        self.plants = [
            {
                "name": "A",
                "water_after": "7 days"
            },
        ]
        scheduler(self.plants,self.schedule)
        solution = ['A',None,None,None,None,None,None,'A',None,None,None,None,None,None]
        for i in range(0,len(solution)):
            self.assertEqual(self.schedule[i],solution[i])

if __name__ == '__main__':
    unittest.main()
