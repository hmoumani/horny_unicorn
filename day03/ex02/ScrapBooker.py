import numpy as np

class ScrapBooker:
    def crop(self, array, dim, position=(0,0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        Args:
        -----
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Return:
        -------
        new_arr: the cropped numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        try:
            assert isinstance(array, np.ndarray)
            assert isinstance(dim, tuple)
            assert isinstance(position, tuple)
            assert len(dim) == 2
            assert len(position) == 2
            assert dim[0] >= 0 and dim[1] >= 0
            assert position[0] >= 0 and position[1] >= 0
            assert position[0] <= array.shape[0] and position[1] <= array.shape[1]
            return array[position[0]:position[0] + dim[0], position[1]:position[1] + dim[1]]
        except Exception:
            return None
        
    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
        Args:
        -----
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the array
        (depending of axis value).
        axis: positive non null integer.
        Return:
        -------
        new_arr: thined numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        try:
            assert isinstance(array, np.ndarray)
            assert isinstance(n, int)
            assert isinstance(axis, int)
            assert n > 0 and n < array.shape[axis]
            assert axis == 0 or axis == 1
            return np.delete(array, np.s_[n-1::n] , int(not axis))
        except Exception:
            return None

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Return:
        -------
        new_arr: juxtaposed numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        try:


# spb = ScrapBooker()
# arr1 = np.arange(0,25).reshape(5,5)
# print(spb.crop(arr1, (3,1),(1,0)))

# arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
# print(spb.thin(arr2,3,0))