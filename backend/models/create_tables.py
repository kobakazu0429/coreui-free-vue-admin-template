import sys
sys.path.append("..")

from peewee import *
from backend.config import settings

from Type import *
from Group import *
from Category import *
from Format import *
from Attribute import *
from Layer import *

db = settings.DB

db.create_tables([Type, Group, Category, Format, Attribute, Layer])
