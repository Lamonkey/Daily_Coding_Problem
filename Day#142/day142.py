import pytest
class note:
    def __init__(self,pre,stack):
        self.pre = pre
        self.stack = stack


    def go_back(self):
        return self.pre


    
def checkBalance(input):
    stack = []
    preOne = None
    nextOne = None
    for i in input:
        #if * is between ()
        #elif * try pop and try *
        #if ( stack
        if(i == "("):
            stack.append(i)
        #else if ) pop
        elif(i == ")"):
            try:
                stack.pop()
            except Exception:
                return False
        
    return len(stack) == 0

def test_mach():
    assert True == checkBalance("(())")
    assert True == checkBalance("()()(())")
    assert False == checkBalance("(")
    assert False == checkBalance(")")
    assert False == checkBalance("())")
    assert False == checkBalance("(()")
    assert False == checkBalance("()))))")
    assert False == checkBalance("()()()(()")
    

test_mach()