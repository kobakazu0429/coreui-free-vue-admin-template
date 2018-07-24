# -*- coding: utf-8 -*-
import sys
sys.path.append("..")

import random
import datetime

from peewee import *

from backend.models.Type import *
from backend.models.Group import *
from backend.models.Category import *
from backend.models.Format import *
from backend.models.Attribute import *


cate = [
    'ベースマップ',
    '空中写真・衛星画像',
    '起伏を示した地図',
    '土地の特徴を示した地図',
    '基準点・測地観測',
    '地震、台風・豪雨等、火山',
    'その他'
]


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

    Type.create(
        type='base' if (i % 2 == 0) else 'overlay',
        created_at=random_date,
        updated_at=random_date,
    )

    Group.create(
        group='国土地理院' if (i % 4 == 0) else 'MIERUNE' if (
            i % 3 == 0) else 'OSM',
        created_at=random_date,
        updated_at=random_date,
    )

    Category.create(
        category=cate[random.randint(0, 6)],
        created_at=random_date,
        updated_at=random_date,
    )

    Format.create(
        format='XYZ' if (i % 3 == 0) else 'geojson' if (
            i % 4 == 0) else 'mvt',
        created_at=random_date,
        updated_at=random_date,
    )

    Attribute.create(
        title='hoge' + str(i),
        url='https://www.google.co.jp/',
        created_at=random_date,
        updated_at=random_date,
    )
