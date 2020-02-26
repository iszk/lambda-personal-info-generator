import random
import string

def get_random() -> str:
    return rand_str(3,10) + '@' + rand_str(4,10) + '.' + rand_str(2,4) + '.zz'

def rand_str(min:int, max:int):
    length = random.randrange(min, max)
    randlst = [random.choice(string.ascii_lowercase + string.digits) for i in range(length)]
    return ''.join(randlst)
