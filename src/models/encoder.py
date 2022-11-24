import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.applications.inception_v3 import InceptionV3

class Encoder():

    def __init__(self) -> None:
        """
        Construct encode to extract features from images
        We will use InceptionV3
        """
        self.feature_extractor = self.feature_extractor()

    def preprocess(self, image_path) -> None:
        """
        Preprocess images befor feeding to the encoder  

        Args:
            image_path: path of image to load it

        Returns:
            x: preprocessed image
        """
        
        # load all images and convert to (299, 299) as expected by InceptionV3
        img = tf.keras.preprocessing.image.load_img(image_path, target_size=(299, 299))
        
        x = tf.keras.preprocessing.image.img_to_array(img)          # Convert PIL image to numpy array
        x = np.expand_dims(x, axis=0)                               # add one more dimension
        x = tf.keras.applications.inception_v3.preprocess_input(x)  # preprocess the image to be ready for InceptionV3

        return x
    
    def feature_extractor(self):
        """
        Create the inception model

        Returns:
            an Inception model to extract features
        """
        inception = InceptionV3(weights='imagenet')

        my_input = inception.input
        my_output = inception.layers[-2].output

        return Model(inputs=my_input, outputs=my_output)

    def encode(self, image_path):
        """
        Start encoding images and extract features

        Args:
            image_path: path of image to load it
        
        Returns:
            features: extracted features
        """
        image = self.preprocess(image_path)
        features = self.feature_extractor.predict(image)
        features = np.reshape(features, features.shape[1])

        return features