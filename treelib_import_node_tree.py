# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:40:11 2019

@author: BSDU
"""

from treelib import Node, Tree

new_tree = Tree()
new_tree.create_node("n1", 1)#root node
new_tree.create_node("n2", 2, parent=1)

new_tree.create_node("n3", 3, parent=1)
new_tree.create_node("n4", 4, parent=2)
new_tree.create_node("n5", 5, parent=3)

new_tree.show()