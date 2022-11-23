import re
import os
import sys
import pandas as pd

sys.path.append(os.path.realpath('..'))

from exceptions import DataPathException

class Preprocess:

    def __init__(self):
        pass
    
    def parse_data(self, data_path):
        """
        Start parsing the data

        Args:
            data_path: the data path we will parse
        
        Returns:
            dataframe: Conatins image_name, Caption_number, caption
        
        """

        try:
            captions = pd.read_csv(data_path, on_bad_lines='skip')
            tuples = list(captions.apply(self._parse, axis=1))
        except:
            raise DataPathException
        else:
            return pd.DataFrame(tuples, columns=['image_name', 'caption_number', 'caption'])
        

    def _parse(self, line):
        """
        To parse data frame line by line to extract data

        Args:
            s: the current line

        Returns:
            image_name: the image name in the directory
            caption_number: the caption number
            caption: The image caption
        """
        line = line[0]
        pattern = "[0-9]*.jpg"
        match = re.match(pattern, line)

        image_name = match[0]
        comment_number = int(line[match.end()+2:match.end()+3])
        caption = line[match.end()+5:-2]

        return image_name, comment_number, caption