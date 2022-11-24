import os
import random
import pandas as pd
import matplotlib.pyplot as plt

class Visualize:
    
    def __init__(self) -> None:
        pass

    def show_images(self, image_path):
        """
        Show 9 random images from images
        
        Args:
            images: The path of the images
        """
        fig = plt.figure(figsize=(20, 15))
        images = os.listdir(image_path)
        indexs = random.sample(range(0, len(images)), 9)

        for i in range(9):
            img = plt.imread(image_path + images[indexs[i]])
            fig.add_subplot(3,3,i+1)
            plt.imshow(img)

        plt.show()
    

    def show_image_with_captions(self, image_path, captions_path):
        """
        Show some random images with their captions

        Args:
            image_path: The path of the images
            captions_path: The Path of the processed data
        """

        images = os.listdir(image_path)
        data = pd.read_csv(captions_path)

        # get some random indecies
        indexs = random.sample(range(0, len(images)), 9)

        for i in range(9):
            img = plt.imread(image_path + images[indexs[i]])                                # read image
            captions = list(data[ data['image_name'] == images[indexs[i]]]['caption'])      # get captions
            plt.imshow(img)                                                                 # show image
            plt.show()
            for cap in captions:                                                            # print captions
                print(cap)