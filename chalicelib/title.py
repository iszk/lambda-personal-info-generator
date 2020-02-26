import random

def get_random() -> str:
    a1 = all()
    return a1[random.randrange(len(a1))]

def all():
    return [
        'プロダクトマネージャー',
        'マネージャー',
        '代表取締役',
        'リーダー',
        '事業部長',
        'メンバー',
        '取締役',
        '部長',
        '課長',
        '主任',
        '係長',
        '社員',
        'CISO',
        'CTO',
        'COO',
        'CEO',
        'CIO',
        'CSO',
    ]
