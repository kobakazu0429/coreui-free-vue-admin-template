# -*- coding: utf-8 -*-
import datetime

from backend.models.Type import *
from backend.flask.utils.msgs import returnResultPatch


def patch_type(id, request):
    patching_type = Type.get_by_id(id)

    patching_type.type = request.form['type']
    patching_type.updated_at = datetime.datetime.now()

    patching_type.save()

    return returnResultPatch()
