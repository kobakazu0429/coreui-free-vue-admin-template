# -*- coding: utf-8 -*-
import datetime

from backend.models.Format import *
from backend.flask.utils.msgs import returnResultPatch


def patch_format(id, request):
    patching_format = Format.get_by_id(id)

    patching_format.format = request.json['format']
    patching_format.updated_at = datetime.datetime.now()

    patching_format.save()

    return returnResultPatch()
