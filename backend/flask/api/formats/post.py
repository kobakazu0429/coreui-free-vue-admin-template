# -*- coding: utf-8 -*-
import datetime

from backend.models.Format import *
from backend.flask.utils.msgs import returnResultCreate


def post_format(request):
    Format.create(
        format=request.json['format'],
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
    )

    return returnResultCreate()
