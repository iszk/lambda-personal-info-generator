import random

def get_random() -> str:
    a1 = all()
    a2 = all_suffix()
    return a1[random.randrange(len(a1))] + a2[random.randrange(len(a2))]

def all():
    return [
        '総務',
        '人事',
        '法務',
        '経理',
        '財務',
        'マーケティング',
        '広報',
        '販売促進',
        '営業',
        '営業推進',
        '開発',
        '技術',
        '企画',
        '企画開発',
        '営業開発',
        '情報システム',
        'ビジネスコンサルティング',
        'ビジネスソリューション',
    ]

def all_suffix():
    return [
        '部',
        '課',
        'Div',
        'ユニット',
        'チーム',
    ]
