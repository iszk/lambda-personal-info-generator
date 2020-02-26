from datetime import datetime
import random
import json

from . import family_name
from . import given_name
from . import phone
from . import department
from . import address
from . import company
from . import email
from . import title

def get_random_lead():

    fname, fkana = family_name.get_random()
    gname, gkana = given_name.get_random()
    postal, pref, addr = address.get_random()

    now = int(datetime.now().timestamp())

    return {
        'family_name': fname,
        'family_name_kana': fkana,
        'given_name': gname,
        'given_name_kana': gkana,
        'phone': phone.get_random(),
        'department': department.get_random(),
        'company': company.get_random(),
        'email': email.get_random(),
        'title': title.get_random(),
        'postal_code': postal,
        'prefecture': pref,
        'address': addr,
        'registered_at': now,
        'id': now,
    }

    # print(get_random_lead())
