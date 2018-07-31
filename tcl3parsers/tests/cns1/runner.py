"""Testing suite runner file for cns1"""
import unittest
import os
import sys

import constants

TCL3PARSERS_PATH = os.path.dirname(os.path.realpath("../"))
sys.path.append(TCL3PARSERS_PATH)

SAMPLEDATAPATH = TCL3PARSERS_PATH + "/tests/example_files/cns1/SampleData"

import cns1

# Test Modules
import value_tests
import variable_tests

class Runner():
    """Executes parser and runs the testing suite"""
    def __init__(self):
        """Loads all tests"""
        tests = unittest.TestSuite()
        loader = unittest.TestLoader()
        tests.addTests(loader.loadTestsFromModule(value_tests))
        tests.addTests(loader.loadTestsFromModule(variable_tests))
        self.suite = tests
        self.sampleDataPath = SAMPLEDATAPATH
        self.sampleFlightName = ""
        self.MI_FILE_NAME = ""
        self.DF_FILE_NAME = ""
        self.FIELD_VARS_NAME = ""
        self.OUTFILE_NAME = ""

    def __runParser(self):
        """Runs parser"""
        cns1.generate(self.MI_FILE_NAME,
                      self.DF_FILE_NAME,
                      self.FIELD_VARS_NAME,
                      self.OUTFILE_NAME)

    def run(self):
        """Runs testing suite"""
        self.__runParser()
        runner = unittest.TextTestRunner(verbosity=3)
        return runner.run(self.suite)

    def setFlightName(self, flightName):
        self.sampleFlightName = flightName
        sampleFlightPath = self.sampleDataPath +  "/" + self.sampleFlightName
        sampleFlightFiles = [name for name in os.listdir(sampleFlightPath)]
        for fileName in sampleFlightFiles:
            if "mission_insight.csv" in fileName:
                self.MI_FILE_NAME = sampleFlightPath + "/" + fileName
            elif ".log" in fileName:
                self.DF_FILE_NAME = sampleFlightPath + "/" + fileName
            elif "field_vars.csv" in fileName:
                self.FIELD_VARS_NAME = sampleFlightPath + "/" + fileName
        self.OUTFILE_NAME = self.sampleDataPath + "/" + self.sampleFlightName + "/cns1_data.json"
        constants.OUTFILE_NAME = self.OUTFILE_NAME

if __name__ == '__main__':
    sampleFlightData = [name for name in os.listdir(SAMPLEDATAPATH) if os.path.isdir(SAMPLEDATAPATH + "/" + name)]
    for sampleFlightName in sampleFlightData:
        testRunner = Runner()
        testset = testRunner.setFlightName(sampleFlightName)
        print("Testing against: " + sampleFlightName)
        testset = testRunner.run()
        print("Tested against: " + sampleFlightName + "\n\n")
        failure = len(testset.failures)
        if failure:
            break
