from unittest import main, TestCase
import sys
sys.path.append('./src')

from datastructures import Graph

class test_graph(TestCase):
    def test_insertvertex(self):
        graphm = Graph()
        self.assertEqual(graphm.insert_vertex('a').element(), 'a')
    def test_vertexcount(self):
        graphm = Graph()
        graphm.insert_vertex('a')
        graphm.insert_vertex('b')
        self.assertEqual(graphm.vertex_count(), 2)
    def test_insertedge(self):
        graphm = Graph()
        v0 = graphm.insert_vertex('a')
        v1 = graphm.insert_vertex('b')
        graphm.insert_edge(v0,v1,2)
        self.assertEqual(graphm.edges().pop().element(), 2)

    
if __name__ == "__main__":
    main()
    


