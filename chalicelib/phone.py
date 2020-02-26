import random

def get_random() -> str:
    ary = ['03', '03', '03', '03', '03', '0120', '090', '080']
    a = ary[random.randrange(len(ary))]
    if a == '03':
        a = "03-{:04d}-{:04d}".format(random.randint(0, 9999), random.randint(0, 9999))
    if a == '0120':
        a = "0120-{:03d}-{:03d}".format(random.randint(0, 999), random.randint(0, 999))
    if a == '090':
        a = "090-{:04d}-{:04d}".format(random.randint(0, 9999), random.randint(0, 9999))
    if a == '080':
        a = "080-{:04d}-{:04d}".format(random.randint(0, 9999), random.randint(0, 9999))

    if random.random() < 0.4:
        a = a.replace('-', '')

    return a
