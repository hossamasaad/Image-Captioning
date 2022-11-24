import pickle
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

class MyTokenizer():

    def __init__(self, data_path) -> None:
        """
        Construc MyTokenizer class that can add tokens to captions and map images to sequences

        Args:
            data_path: The path of the current cleaned captions
        """
        self.tokenizer = Tokenizer()
        with open(data_path, "rb") as input_file:
            self.data = pickle.load(input_file)

        self.images = list(self.data.keys())
        self.counts = {}

    def add_tokens(self):
        """
        Add <start> and <end> tokens to captions and
        update counts which will help in mapping sequences to images

        Returns
            Captions: list of captions after adding tokens
        """
        captions = []
        for i in range(len(self.images)):
            for cap in self.data[self.images[i]]:
                cap = '<start> ' + cap + ' <end>'
                captions.append(cap)
                
                try:
                    self.counts[self.images[i]] += 1
                except:
                    self.counts[self.images[i]] = 1

        return captions
    
    def get_image_sequences(self, sequences):
        """
        Map image to sequences

        Args:
            sequences: sequences of indecies will be mapped to images
        
        Returs:
            image_sequences: matp of images to their caption sequences 
        """
        # Image to sequences to pass to generator
        image_sequences = {}
        i = 0
        for image in self.images:
            image_sequences[image] = sequences[i:i+self.counts[image]]
            i += self.counts[image]
            
        return image_sequences