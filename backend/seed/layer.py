# -*- coding: utf-8 -*-
import sys
sys.path.append("..")

import random
import datetime

from peewee import *

from backend.models.Layer import *

ID_START = 1
ID_END = 30


for i in range(ID_START, ID_END+1):
    now = datetime.datetime.now()

    y = random.randint(0, 10)
    m = random.randint(0, 12)
    d = random.randint(0, 1000)
    h = random.randint(0, 24)
    mi = random.randint(0, 60)
    s = random.randint(0, 60)
    ms = random.randint(0, 100000)

    random_date = now + datetime.timedelta(
        days=d,
        hours=h,
        minutes=mi,
        seconds=s,
        microseconds=ms
    )

    Layer.create(
        type_id=random.randint(1, ID_END),
        group_id=random.randint(1, ID_END),
        category_id=random.randint(1, ID_END),
        name='hogehoge' + str(i),
        url='https://www.google.co.jp/',
        format_id=random.randint(1, ID_END),
        attribute_id=random.randint(1, ID_END),
        description='hoge' * i,
        created_at=random_date,
        updated_at=random_date,
    )
