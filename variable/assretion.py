def a():
    a=2
    b=0
    assert b != 0 ,"denominator can not be zero"
    c=b/a;
    return c

try:
    result = a()
    print(result)
except Exception as e:
    print(e)

