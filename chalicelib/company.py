import random
import string

def get_random() -> str:
    a1 = rand_name()
    a2 = all_suffix()
    a3 = all_companytype()

    name = a1 + a2[random.randrange(len(a2))]

    if random.random() < 0.4:
        return name + a3[random.randrange(len(a3))]
    return a3[random.randrange(len(a3))] + name

def rand_name():
    length = random.randrange(2,4)
    randlst = [random.choice(string.ascii_uppercase) for i in range(length)]
    return ''.join(randlst)

def all_suffix():
    return [
        'ソリューション',
        'カンパニー',
        'システム',
        '商事',
        '開発',
        '企画',
        'データ',
        'コンサルティング',
        '',
    ]

def all_companytype():
    return [
        '株式会社',
        '合同会社',
        '有限会社',
    ]
