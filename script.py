# This program prints Hello, world!
import logging
import sys

sys.path.append('/home/odoo/.local/lib/python3.5/site-packages')

import dexml

_logger = logging.getLogger(__name__)

from suds.client import Client

logging.getLogger('suds.client').setLevel(logging.DEBUG)

from dexml import fields

class Person(dexml.Model):
    name = fields.String()
    age = fields.Integer(tagname='age')

p = Person(name="Handsome B. Wonderful",age=36)
print (p.render())
