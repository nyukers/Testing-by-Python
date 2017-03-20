# -*- coding: utf-8 -*-

#import time, unittest
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(self):
     app.login(username="admin", password="secret")
     app.create_group(Group(name="My group", header="My group", footer="footer"))
     app.logout()
     #self.assertTrue(success)

