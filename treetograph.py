from __future__ import unicode_literals, print_function


class TreeToGraph(object):
    """A spaCy v2.0 pipeline component that takes the tree output of an SRL parser
     and reconstructs missing relations and removes dummy relations that exist due to the
     limitations of the parser to tree. The output is a non-tree graph that is closer to the
     expected SRL relations"""

    name = "tree_to_graph"

    def __call__(self, doc):
        for token in doc:
            if token.dep_ == "dummy" or token.dep_ == "root":
                token.dep_ = ''
                token.dep = 0
                token.head = token
        return doc