import unittest
import functions
import functions_with_errors


class TestFunc(unittest.TestCase):

    def test_greeting_by_name(self):
        self.assertEqual(functions.greeting_by_name("Vlad"),"Hello Vlad!",msg=f"Failed in {functions.__name__})")
        self.assertEqual(functions_with_errors.greeting_by_name("Vlad"),"Hello Vlad!",msg=f"Failed in {functions_with_errors.__name__}))")

    def test_get_symbol_position(self):
        self.assertEqual(functions.get_symbol_position("Hahaha","ha"),"Error! Symbol can be string with only one letter",msg=f"Failed in {functions.__name__})")
        self.assertEqual(functions_with_errors.get_symbol_position("Hahaha","ha"),2 ,msg=f"Failed in {functions_with_errors.__name__}))")

    def test_merge(self):
        dict1={"key":"text","pass":"gona"}
        dict2={"key":"text","pass":"changed"}
        dict3={"key":"text","pass":"changed"}
        self.assertEqual(functions.merge(dict1,dict2),dict3,msg=f"Failed in {functions.__name__})")
        self.assertEqual(functions_with_errors.merge(dict1,dict2),dict3,msg=f"Failed in {functions_with_errors.__name__}))")

if __name__=="__main__":
    unittest.main(verbosity=2)