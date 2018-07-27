# -*- coding: utf-8 -*-
import datetime

from backend.models.Group import *
from backend.flask.utils.msgs import returnResultCreate


def post_group(request):
    Group.create(
        group=request.form['group'],
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
    )

    return returnResultCreate()
