import numpy as np
from numpy import array

class NumPyCreator:
    def from_list(self, lst):
        try:
            assert isinstance(lst, list)
            if any(isinstance(i, list) for i in lst):
                _len = len(lst[0])
                if not all(isinstance(i, list) for i in lst) or not all(_len  == len(i) for i in lst):
                        return None
            return np.array(lst)
        except Exception:
            return None

    def from_tuple(self, tpl):
        try:
            assert isinstance(tpl, tuple)
            if any(isinstance(i, tuple) for i in tpl):
                _len = len(tpl[0])
                if not all(isinstance(i, tuple) for i in tpl) or not all(_len  == len(i) for i in tpl):
                        return None
            return np.array(tpl)
        except Exception:
            return None

    def from_iterable(self, itr):
        try:
            return np.array(itr)
        except Exception:
            return None

    def from_shape(self, shape, value=0):
        try:
            return np.full(shape, value, dtype=np.float64)
        except Exception:
            return None
    
    def random(self, shape):
        try:
            return np.random.random(shape)
        except Exception:
            return None

    def identity(self, n):
        try:
            return np.identity(n, dtype=np.float64)
        except Exception:
            return None

    
if __name__ == "__main__": 
    npc = NumPyCreator()
    print(npc.from_list([[1,2,3],[6,3,4]]))
    # Output :
    array([[1, 2, 3],
    [6, 3, 4]])
    print(npc.from_list([[1,2,3],[6,4]]))
    # Output :
    None    
    print(npc.from_list([[1,2,3],['a','b','c'],[6,4,7]]))
    # Output :
    array([['1','2','3'], ['a','b','c'], ['6','4','7']], dtype='<U21')
    print(npc.from_list(((1,2),(3,4))))# Output :
    None
    print(npc.from_tuple(("a", "b", "c")))
    # Output :
    array(['a', 'b', 'c'])
    print(npc.from_tuple(["a", "b", "c"]))
    # Output :
    None
    print(npc.from_iterable(range(5)))
    # Output :
    array([0, 1, 2, 3, 4])
    shape=(3,5)
    print(npc.from_shape(shape))
    # Output :
    array([[0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]])
    print(npc.random(shape))
    # Output :
    array([[0.57055863, 0.23519999, 0.56209311, 0.79231567, 0.213768 ],
    [0.39608366, 0.18632147, 0.80054602, 0.44905766, 0.81313615],
    [0.79585328, 0.00660962, 0.92910958, 0.9905421 , 0.05244791]])
    print(npc.identity(4))
    # Output :
    array([[1., 0., 0., 0.],
    [0., 1., 0., 0.],
    [0., 0., 1., 0.],
    [0., 0., 0., 1.]])