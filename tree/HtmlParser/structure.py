#coding:utf-8
__author__ = 'Xsank'
from util import SINGLE_NODE
from util import render


class Attribute(object):
    '''This contain the tag attribution.
    '''
    def __init__(self,attr,value):
        self._attr=attr
        self._value=value

    @property
    def attr(self):
        return self._attr

    @property
    def value(self):
        return self._value

    def __str__(self):
        return "attribute:%s,value:%s" % (self.attr,self.value)


class Node(object):
    '''This is the node of the html dom tree.It contains the
    relation ship among the dom tree nodes and html attributions.
    '''
    level=0

    def __init__(self,tag="",level=0):
        self._name=""
        self._attrs=[]
        self._attrmap={}
        self._content=""
        self._parent=None
        self._children=[]
        self._level=level
        self.init_node(tag)

    @property
    def name(self):
        return self._name

    @property
    def content(self):
        return self._content

    @property
    def children(self):
        return self._children

    @property
    def parent(self):
        return self._parent

    def init_node(self,tag):
        items=tag.split()
        if items:
            self._set_name(items[0])
            self._set_attrs(items[1:])

    def _set_name(self,name):
        if name.endswith('>'):
            self._name=name[1:-1]
        else:
            self._name=name[1:]

    def _set_attrs(self,attrs):
        for item in attrs:
            attr=item.split('=')[0]
            value=item.split('=')[-1].strip('>').strip('"')
            self._attrs.append(Attribute(attr=attr,value=value))
            self._attrmap[attr]=value

    def get_class(self):
        return self._attrmap['class'] if 'class' in self._attrmap else ''

    def get_id(self):
        return self._attrmap['id'] if 'id' in self._attrmap else ''

    def set_content(self,content):
        self._content=content

    def set_parent(self,parent=None):
        self._parent=parent

    def add_child(self,node=None):
        self._children.append(node)

    def is_single(self):
        return self._name in SINGLE_NODE

    def render(self):
        if render(self._name):
            return self.intend()+render(self._name)+self._content

    def intend(self):
        return '    '*self._level

    def __str__(self):
        return self._name
