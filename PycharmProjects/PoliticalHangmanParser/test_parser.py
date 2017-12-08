import unittest
from Parser2 import *
import sqlite3


class TestParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')
        conn = sqlite3.connect('PoliticianCompare.db')
        c = conn.cursor()

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.politician = Politician_Parser('https://www.whitehouse.gov/administration/cabinet', 'div', 'field-item even')
        self.data_compare = DataInput_and_Checker('1','2','3','4')

    def tearDown(self):
        print('tearDown')
        pass

    def test_webParserTrue(self):
        #Checks to see if president returns a value
        print('test_webParserTrue')
        self.assertIsNotNone(self.politician)



    def test_writeToDb(self):
        # checks to see if parser data is written to db
        print('test_writetoDb')
        conn = sqlite3.connect('PoliticianCompare.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Politician_Data")
        self.assertNotEqual(len(c.fetchall()), 0)


    def test_compareData(self):
        print('test_compareData')
        self.assertFalse(self.data_compare.dataCompare())

    def test_isolateNewData(self):
        print('test_isolateData')
        self.assertIsNotNone(self.data_compare.dataDiff())



class TestNotifier(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def test_getIsoData(self):
        pass

    def test_DataIsTrue(self):
        pass

    def test_emailNotifier(self):
        pass


if __name__ == '__main__':
    unittest.main()
