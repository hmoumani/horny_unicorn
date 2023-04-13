from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt

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
            plt.gcf().canvas.manager.set_window_title("loaded image")
            plt.imshow(array)
            plt.axis('off')
            plt.show()
        except Exception as e:
            if hasattr(e, 'errno') and isinstance(e.errno, int):
                print('Exception: {} -- strerror: {}'.format(type(e).__name__, os.strerror(e.errno)))
            else:    
                print('Exception: OSError -- strerror: None', e)

if __name__ == "__main__":
    imp = ImageProcessor()

    arr = imp.load("../42AI.png")
    # Output :

    imp.display(arr)

