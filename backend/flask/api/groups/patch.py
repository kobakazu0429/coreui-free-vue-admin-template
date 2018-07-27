# -*- coding: utf-8 -*-
import datetime

from backend.models.Group import *
from backend.flask.utils.msgs import returnResultPatch


def patch_group(id, request):
    patching_group = Group.get_by_id(id)

    patching_group.group = request.form['group']
    patching_group.updated_at = datetime.datetime.now()

    patching_group.save()

    return returnResultPatch()
