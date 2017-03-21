# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="My group", header="header", footer="footer"))
    #self.assertTrue(success)

def test_add_group(app):
    app.group.create(Group(name="", header="", footer=""))

