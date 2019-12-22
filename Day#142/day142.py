import pytest
def checkBalance(input):
    stack = []
    for i in input:
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