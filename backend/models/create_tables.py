import sys
sys.path.append("..")

from peewee import *
from backend.config import settings

from backend.models.Type import *
from backend.models.Group import *
from backend.models.Category import *
from backend.models.Format import *
from backend.models.Attribute import *
from backend.models.Layer import *

db = settings.DB

db.create_tables([Type, Group, Category, Format, Attribute, Layer])
