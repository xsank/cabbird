__author__ = 'Xsank'
import re

from structure import Node


class HtmlParser(object):
    '''It contains the root of the html dom tree,and it provide the
    travel method and rend method.
    '''
    def __init__(self,name):
        self.name=name
        self.dom=Node()
        self.nodes=[self.dom]
        self.stack=[self.dom]
        self.elements=self._prepare(name)
        self._parse()

    def _prepare(self,name):
        with open(name,'r') as f:
            content=''.join(f.read().split('\n'))
            return [element for element in re.split(r"(<.*?>)",content) if element.strip()]

    def _parse(self):
        level=0
        for element in self.elements:
            if element[0]=='<':
                if element[1]=='!':
                    continue
                if element[1]!='/':
                    node=Node(element,level)
                    parent=self.stack[-1]
                    node.set_parent(parent)
                    parent.add_child(node)
                    self.nodes.append(node)
                    self.stack.append(node)
                    if not node.is_single():
                        level+=1
                    else:
                        self.stack.pop()
                else:
                    self.stack.pop()
                    level-=1
            else:
                self.nodes[-1].set_content(element)

    def get_node_by_class(self,name):
        for node in self.nodes:
            if node.get_class()==name:
                print "tag %s,class=%s" % (node,name)

    def get_node_by_id(self,id):
        for node in self.nodes:
            if node.get_id()==id:
                print "tag %s,id:%s,parent:%s,child:%s" % (node,id,node.parent,node.children)

    def travel(self):
        print '*'*80
        print 'print the dom tree:'
        print '*'*80
        self._preorder(self.dom)

    def _preorder(self,node):
        print node.intend()+node.name
        for child in node.children:
            self._preorder(child)

    def render(self):
        print '*'*80
        print 'render the dom tree:'
        print '*'*80
        for node in self.nodes:
            if node.render():
                print node.render()

if __name__=="__main__":
    hp=HtmlParser('About - Opera Software.html')
    hp.travel()
    hp.render()
    hp.get_node_by_class('hf--level-2')
    hp.get_node_by_id('footnav')


