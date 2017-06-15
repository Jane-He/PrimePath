from PrimePath import *
from selenium import webdriver
import unittest,time
from HTMLTestRunner import HTMLTestRunner

class TestPrimePath(unittest.TestCase):
    '''PrimePath测试'''
    def setUp(self):
        print("test start")

    def test_PrimePath(self):
        '''测试文件case15的测试用例'''
        current_path = os.path.dirname(os.path.abspath("PrimePath.py"))
        testcase = 'case15.txt'
        ##########读文件##########
        MyAnswer = os.path.join(current_path,'answer', testcase)
        HeAnswer = os.path.join(current_path,'hshanswer', testcase)
        
        Myfile =  open(MyAnswer, 'r')
        Hefile =  open(HeAnswer, 'r')

        MyList = []
        HeList = []
        while True:
            line = Myfile.readline()
            if not line:break
            line = line.strip("[]\n")
            line = line.replace(' ', '')
            tmpline = list(line.split(","))
            tmpline = [int(element) for element in tmpline]
            MyList.append(tmpline)
        while True:
            line = Hefile.readline()
            if not line:break
            line = line.strip("[]\n")
            line = line.replace(' ', '')
            tmpline = list(line.split(","))
            tmpline = [int(element) for element in tmpline]
            HeList.append(tmpline)
        self.assertEqual(MyList, HeList)

    def tearDown(self):
        print("test end")

# if __name__== '__main__':
#     testunit = unittest.TestSuite()
#     testunit.addTest(TestPrimePath("test_PrimePath"))

#     now = time.strftime("%Y-%m-%d %H_%M_%S")

#     filename = './PrimePathReport-' + now + "-result.html"
#     fp = open(filename, "wb")

#     runner = HTMLTestRunner(stream=fp, 
#                         title="何娟娟————PrimePath测试报告", 
#                         description="用例执行情况:")
    
#     runner.run(testunit)
#     fp.close()