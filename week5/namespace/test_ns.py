import unittest
from namespace import ns

namespaces = {
    "global":(
        [], 
        {
            "a": ([], {})
        }
    )
}
class TestNs(unittest.TestCase):
    
    def test_create(self):
        ns.namespaces = {"global":([], {})}
        
        '''
        add namespace to global
        '''
        namespaces = ns.create("a", "global")
        self.assertEqual(namespaces, {"global":([], {"a":([], {})})})
            
        '''
        add namespace to non existing one
        '''
        namespaces = ns.create("b", "x")
        self.assertEqual(namespaces, {"global":([], {"a":([], {})})})
        
        '''
        add namespace to child of global
        '''
        namespaces = ns.create("x", "a")
        self.assertEqual(namespaces, {"global":([], {"a":([], {"x":([],{})})})})

    def test_add(self):
        ns.namespaces = {"global":([], {})}

        namespaces = ns.add("global", "x")  
        self.assertEqual(namespaces, {"global":(["x"], {})}) 

        ns.create("a", "global")
        ns.create("b", "a")
        namespaces = ns.add("b", "y")  
        self.assertEqual(namespaces, {"global":(["x"], {"a":([],{"b":(["y"],{})})})}) 


if __name__ == '__main__':
    unittest.main()