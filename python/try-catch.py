try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)

finally:
    print('finally...')
print('END')


def foo(s):
    n = int(s)
    assert n != 0,'n is  zero!'
    return  10/n

def main():
    return  foo('1')

import  logging
logging.basicConfig(level=logging.INFO)
s='0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)