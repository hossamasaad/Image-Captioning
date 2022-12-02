import re
from tqdm import tqdm

class CaptionCleaner:
    def __init__(self):
        pass

    def load_captions(self, caption_path):
        """
        Load caption from captions path and return a dictionary contain image as key and list of captions for this image
        
        Args:
            caption_path: the caption path 
        """

        file = open(caption_path, 'r')
        text = file.readlines()
        file.close()
        
        new_data = {}

        for line in text[1:]:
            line = line.strip().split(',')
            if line[0] in new_data.keys():
                new_data[line[0]].append(line[2])
            else :
                new_data[line[0]] = [line[2]]

        return new_data

    def clean_captions(self, captions):
        """
        Clear symbols, numbers and single letters from sentences
        
        Args:
            data_path: the data path
        """
        
        new_data = {}
        for key, caps in tqdm(captions.items()):
            new_captions = []
            for caption in caps:
                # removing symbols and numbers
                caption = re.sub(r'[!@#.$(),"%^*?:;~`0-9]', ' ', caption)
                caption = re.sub(r'[[]]', ' ', caption)

                # removing single letters
                caption = ' '.join( [w for w in caption.split() if len(w)>1] )

                # conver to lower case
                caption = caption.lower()

                # append to new captions
                new_captions.append(caption)
            
            new_data[key] = new_captions

        return new_data