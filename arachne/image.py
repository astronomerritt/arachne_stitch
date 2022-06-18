import matplotlib.pyplot as plt
from skimage import io
from skimage.transform import resize, rescale
from skimage import img_as_ubyte

class Image():
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = io.imread(self.image_path)
        self.original_image = self.image
        self.image_shape = self.image.shape
        self.aspect_ratio = float(self.image_shape[1] / self.image_shape[0])
    
    def plot_image(self):
        implot = plt.imshow(self.image)
        return implot
    
    def recalculate_image_shape(self):
        self.image_shape = self.image.shape
    
    def resize_image(self, height=None, width=None, aa=False):
        
        if width and not height:
            height = width / self.aspect_ratio
        if height and not width:
            width = height * self.aspect_ratio
        if not any([height, width]):
            print("Neither height or width supplied. No resizing done.")
            
        self.image = img_as_ubyte(resize(self.image, (height, width), anti_aliasing=aa))
        self.recalculate_image_shape()
    
    def rescale_image(self, scale, aa=False):
        self.image = img_as_ubyte(rescale(self.image, (scale, scale, 1), anti_aliasing=aa))
        self.recalculate_image_shape()
    
    def reset_image_to_original(self):
        self.image = self.original_image
        self.recalculate_image_shape()
    
    def grayscale_image():
        pass

    def monocolour_image():
        pass