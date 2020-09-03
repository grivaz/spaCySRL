import unittest

import spacy

from treetograph import TreeToGraph


class TestTreeToGraph(unittest.TestCase):

    def test_upper(self):
        nlp = spacy.load("./model-best")
        component = TreeToGraph()  # initialise component
        nlp.add_pipe(component, last=True)  # add last to the pipeline

        doc = nlp("This is a test")
        self.assertTrue("tree_to_graph" in nlp.pipe_names)  # pipeline contains component name
        self.assertTrue("parser" in nlp.pipe_names)
        self.assertTrue(doc[0].dep_ == '')
        self.assertTrue(doc[0].dep == 0)
        self.assertTrue(doc[0].head == doc[0])


if __name__ == '__main__':
    unittest.main()