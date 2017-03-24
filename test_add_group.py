# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="My group", header="header", footer="footer")
    app.group.create(group)
    #app.group.count as hash method
    assert len(old_groups)+1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_add_empty_group(app):
#    old_groups = app.group.get_group_list()
#    app.group.create(Group(name="", header="", footer=""))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups)+1 == len(new_groups)

