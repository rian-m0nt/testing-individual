import unittest, csv
from unittest import mock
from unittest.mock import MagicMock
from src.DataSource.ReadCSVFile import ReadCSVFile
from src.DataSource.DataSourceConstants import *
from src.DataSource.CsvReaderStub import CsvReaderStub

class TestReadCSVFile(unittest.TestCase):

    readCSVFile = ReadCSVFile()
    CsvReaderStub = CsvReaderStub()
    def test_getCustomerDataFromFile(self):
        fileData = self.readCSVFile.getFileData(ENTITIES_FOLDER,"customer" + ".csv")
        self.assertEqual( fileData[1] ,['derek.somerville@glasgow.ac.uk', 'Derek', 'Somerville', '1234'])

    def test_getLastLinesFromFile(self):
        fileLines = self.readCSVFile.getLastLines( ENTITIES_FOLDER, "customer" + ".csv",1)
        self.assertEqual( fileLines ,['matthew.barr@glasgow.ac.uk', 'Matt', 'Barr', '4321'])
    def test_getCustomerDataFromStub(self):
        data = CsvReaderStub.getData(self)
        self.assertEqual(data,['derek.somerville@glasgow.ac.uk', 'Derek', 'Somerville', '1234'])


    def test_getCustomerDataMock(self):
        mockData = []
        mockData.append('derek.somerville@glasgow.ac.uk')
        mockData.append('Derek')
        mockData.append('Somerville')
        mockData.append('1234')
        self.readCSVFile.getFileData = MagicMock(return_value=mockData)

        result = self.readCSVFile.getFileData(ENTITIES_FOLDER, "customer" + ".csv")
        self.assertEqual(result,['derek.somerville@glasgow.ac.uk', 'Derek', 'Somerville', '1234'])
    def test_get
def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()

