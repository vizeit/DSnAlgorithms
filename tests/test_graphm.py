from unittest import main, TestCase
import sys
sys.path.append('./src')

from datastructures import GraphM

class test_graphm(TestCase):
    def test_insertvertex(self):
        graphm = GraphM()
        self.assertEqual(graphm.insert_vertex('a').element(), 'a')
    def test_vertexcount(self):
        graphm = GraphM()
        graphm.insert_vertex('a')
        graphm.insert_vertex('b')
        self.assertEqual(graphm.vertex_count(), 2)
    def test_insertedge(self):
        graphm = GraphM()
        v0 = graphm.insert_vertex('a')
        v1 = graphm.insert_vertex('b')
        graphm.insert_edge(v0,v1,2)
        self.assertEqual(graphm.edges()[v0][v1], 2)
    def test_floydwarshall(self):
        g = GraphM()
        v0 = g.insert_vertex('a')
        v1 = g.insert_vertex('b')
        v2 = g.insert_vertex('c')
        v3 = g.insert_vertex('d')
        v4 = g.insert_vertex('e')
        v5 = g.insert_vertex('f')
        v6 = g.insert_vertex('g')
        g.insert_edge(v0,v1,4)
        g.insert_edge(v0,v6,2)
        g.insert_edge(v1,v1,-1)
        g.insert_edge(v1,v2,3)
        g.insert_edge(v6,v4,2)
        g.insert_edge(v2,v4,1)
        g.insert_edge(v2,v3,3)
        g.insert_edge(v3,v5,-2)
        g.insert_edge(v4,v5,2)

        d = g.floydwarshall()
        self.assertEqual(d[v0][v3], -float('inf'))

    
if __name__ == "__main__":
    main()
    


