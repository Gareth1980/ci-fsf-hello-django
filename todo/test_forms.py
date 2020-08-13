from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    form = ItemForm({'name': ''})
    self.assertfalse(form.is_valid())