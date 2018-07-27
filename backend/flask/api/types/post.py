# -*- coding: utf-8 -*-
import datetime

from backend.models.Type import *
from backend.flask.utils.msgs import returnResultCreate


def post_type(request):
    Type.create(
        type=request.form['type'],
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
    )

    return returnResultCreate()
