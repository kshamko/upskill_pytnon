import unittest
#from namespace 
import ns

class TestNs(unittest.TestCase):
    
    def test_create(self):
        ns.namespaces = {"global":([], {})}
        
        
        #add namespace to global
        
        namespaces = ns.create("a", "global")
        self.assertEqual(namespaces, {"global":([], {"a":([], {})})})
            
        
        #add namespace to non existing one
        
        namespaces = ns.create("b", "x")
        self.assertEqual(namespaces, {"global":([], {"a":([], {})})})
        
        
        #add namespace to child of global
        
        namespaces = ns.create("x", "a")
        self.assertEqual(namespaces, {"global":([], {"a":([], {"x":([],{})})})})

        namespaces = ns.create("c", "global")
        self.assertEqual(namespaces, {"global":([], {"a":([], {"x":([],{})})}, {"c":([], {})})}) 

        # Должен добавлять новое пространоство имен, а не заменять уже существующее.

    def test_add(self):
        ns.namespaces = {"global":([], {})}

        namespaces = ns.add("global", "x")  
        self.assertEqual(namespaces, {"global":(["x"], {})}) 

        ns.create("a", "global")
        ns.create("b", "a")
        namespaces = ns.add("b", "y")  
        self.assertEqual(namespaces, {"global":(["x"], {"a":([],{"b":(["y"],{})})})}) 

    def test_get(self):
        ns.namespaces = {"global":([], {})}

        namespaces = ns.get("global", "a")
        self.assertEqual(namespaces, None)

        ns.create("a", "global")
        ns.create("b", "a")
        ns.add("b", "y")
        namespaces = ns.get("b", "y") 
        self.assertEqual(namespaces, "b")                  # {"global":([], {"a":([],{"b":(["y"],{})})})}

        ns.add("global", "x")
        namespaces = ns.get("b", "x")
        self.assertEqual(namespaces, "global")             # {"global":(["x"], {"a":([],{"b":(["y"],{})})})}

        ns.add("a", "z")
        namespaces = ns.get("a", "z") 
        self.assertEqual(namespaces, "a")                  # {"global":(["x"], {"a":(["z"],{"b":(["y"],{})})})}

        ns.add("global", "v")
        namespaces = ns.get("a", "v") 
        self.assertEqual(namespaces, "global")             # {"global":(["x", "v"], {"a":(["z"],{"b":(["y"],{})})})}



if __name__ == '__main__':
    unittest.main()