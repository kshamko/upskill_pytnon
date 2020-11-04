ns = lambda name, arg, action: exec("%s('%s','%s')" % (action, name, arg))

namespaces = {"global":([], {})}

def create(namespace, parent):    
    def _create(nss, start_ns, ns, parent):        
        if parent == start_ns:
            vals, child = nss.get(parent)
            nss[parent] = (vals, {ns:([], {})})
        else:
            vals, children = nss[start_ns]
            keys = list(children.keys())
            if len(keys) == 0:
                return
            return _create(children, keys[0], ns, parent)
        
    return _create(namespaces, "global", namespace, parent)

    
def add(namespace, val):
    def _add(nss, global_ns, ns, val):         
        if ns == global_ns:  
            vals, children = nss[ns]
            vals.append(val)
            return 
        else:
            vals, children = nss[global_ns]
            keys = list(children.keys())
            if len(keys) == 0:
                return            
            return _add(children, keys[0], namespace, val)
            
    #global namespaces    
    return _add(namespaces, "global", namespace, val)        

def get(namespace, var):  
    ns = None
    start = namespaces
    namespace_exists = False
    
    while True:        
        keys = list(start.keys())
        if len(keys) == 0:
            break
        else:
            vals, start = start[keys[0]]            
            if (var in vals):
                ns = keys[0]                 
            if keys[0] == namespace:
                namespace_exists = True
                break
                
    if not namespace_exists:
        print(None)
        return None
    else:
        print(ns)
        return ns

   
for i in range(int(input())):
    cmd, namespace, arg = input().split() 
    ns(namespace, arg, cmd)   