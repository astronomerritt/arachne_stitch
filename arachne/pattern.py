import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from image import Image

class Pattern(Image):
    def __init__(self, name, db_name='./data/dmc_to_rgb.csv'):
        super().__init__(name)
        self.colours_db = pd.read_csv(db_name)
        self.colour_array = self.colours_db[['Red', 'Green', 'Blue']].copy().to_numpy()
        self.floss_array = self.colours_db["Floss#"].to_numpy()
    
    def closest_colour(self, colour, colours):
        dist = np.sum((colours - colour)**2, axis=1)
        return np.argmin(dist)
    
    def create_floss_map(self):
        colour_match_index_3d = np.zeros((self.image_shape[0], self.image_shape[1]))

        # this for-loop is nasty.
        for i in range(self.image_shape[0]):
            for j in range(self.image_shape[1]):
                colour_match_index_3d[i, j] = self.closest_colour(self.image[i, j, :], self.colour_array)
            
        self.floss_map = self.floss_array[colour_match_index_3d.astype(int)]
        self.floss_map_RGB = self.colour_array[colour_match_index_3d.astype(int)]
    
    def plot_floss_map(self):
        implot = plt.imshow(self.floss_map_RGB)
        return implot
    
    @property
    def number_unique_flosses(self):
        return np.unique(self.floss_map).shape[0]