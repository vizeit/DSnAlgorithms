from unittest import main, TestCase
import sys
sys.path.append('./src')

from algorithms import Bubblesort, Combinations, Insertionsort, Mergesort, Permutations, Quicksort, Radixsort, Selectionsort, Boyermoore

class test_algorithms(TestCase):
    def test_bubblesort(self):
        l = [5,7,3,1]
        Bubblesort(l)
        self.assertListEqual(l, [1,3,5,7])
    def test_combinations(self):
        self.assertListEqual([c for c in Combinations('ab')], ['a', 'b', 'ab'])
    def test_permutations(self):
        self.assertListEqual([c for c in Permutations('ab')], ['a', 'b', 'ab', 'ba'])
    def test_insertionsort(self):
        self.assertListEqual(Insertionsort([5,7,3,1]), [1,3,5,7])
    def test_mergesort(self):
        self.assertListEqual(Mergesort([5,7,3,1]), [1,3,5,7])
    def test_quicksort(self):
        l = [5,7,3,1]
        Quicksort(l)
        self.assertListEqual(l, [1,3,5,7])
    def test_radixesort(self):
        self.assertListEqual(Radixsort([5,7,3,1], 1, 10), [1,3,5,7])
    def test_selectionsort(self):
        l = [5,7,3,1]
        Selectionsort(l)
        self.assertListEqual(l, [1,3,5,7])
    def test_boyermoore(self):
        self.assertEqual(Boyermoore('thisisateststring','rin'), 13)

if __name__ == "__main__":
    main()
    


