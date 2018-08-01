# -*- coding: utf-8 -*-
import datetime

from backend.models.Category import *
from backend.flask.utils.msgs import returnResultCreate


def post_category(request):
    Category.create(
        category=request.json['category'],
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
    )

    return returnResultCreate()
