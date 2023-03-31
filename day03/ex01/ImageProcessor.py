from PIL import Image
import numpy as np
import os
import matplotlib

import matplotlib.pyplot as plt
matplotlib.use('TkAgg') # set the backend to TkAgg

class ImageProcessor:
    
    def load(self, path):
        try:
            assert isinstance(path, str)
            assert path.endswith(".png")
            img = Image.open(path)
            print("Loading image of dimensions {} x {}".format(img.size[0], img.size[1]))
            return np.array(img)
        except Exception as e:
            if hasattr(e, 'errno') and isinstance(e.errno, int):
                print('Exception: {} -- strerror: {}'.format(type(e).__name__, os.strerror(e.errno)))
            else:    
                print('Exception: OSError -- strerror: None')
                
    def display(self, array):
        try:
            assert isinstance(array, np.ndarray)
            plt.get_current_fig_manager().window.title('loaded image')
            plt.imshow(array, cmap='gray')
            plt.axis('off')
            plt.show()
        except Exception as e:
            if hasattr(e, 'errno') and isinstance(e.errno, int):
                print('Exception: {} -- strerror: {}'.format(type(e).__name__, os.strerror(e.errno)))
            else:    
                print('Exception: OSError -- strerror: None')


# imp = ImageProcessor()
# arr = imp.load("non_existing_file.png")
# # Output :
# print(arr)
# # Output :
# None
# arr = imp.load("empty.png")
# # Output :
# print(arr)
# # Output :
# None
# arr = imp.load("42AI.png")
# # Output :
# print(arr)