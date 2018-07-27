# -*- coding: utf-8 -*-
import datetime

from backend.models.Attribute import *
from backend.flask.utils.msgs import returnResultPatch


def patch_attribute(id, request):
    patching_attribute = Attribute.get_by_id(id)

    patching_attribute.title = request.form['title']
    patching_attribute.url = request.form['url']
    patching_attribute.updated_at = datetime.datetime.now()

    patching_attribute.save()

    return returnResultPatch()
