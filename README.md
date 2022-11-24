# Image Captioning

![GitHub repo size](https://img.shields.io/github/repo-size/hossamasaad/Image-Captioning)
![GitHub contributors](https://img.shields.io/github/contributors/hossamasaad/Image-Captioning)
![GitHub stars](https://img.shields.io/github/stars/hossamasaad/Image-Captioning?style=social)
![GitHub forks](https://img.shields.io/github/forks/hossamasaad/Image-Captioning?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/hossamasaad10?style=social)

Image Captioning is a task that combines computer vision and natural language processing, where it aims to generate descriptive legends for images.
<br>
In this project I tried to apply some diffrent archticture to create image caption generator like merging, injecting and visual attention,
used `InceptionV3` as image encoder to extract features from images. `GloVe` to create word embeddings.

## Dataset
[Flickr30K](https://www.kaggle.com/datasets/hsankesara/flickr-image-dataset) The Flickr30k dataset has become a standard benchmark for sentence-based image description.
This data consists of an image caption corpus consisting of 158,915 crowdsourced captions describing 31,783 images.

## Project Structure
```
.
├── data
│   ├── external
│   ├── interim
│   │   ├── captions.pickle
│   │   ├── data_v1.csv
│   │   └── word_index.pkl
│   ├── processed
│   └── raw
│       └── flickr30k_images
│           ├── images
├── models
├── notebooks
│   └── Image Captioning.ipynb
├── reports
│   └── figures
├── src
│   ├── __init__.py
│   ├── data
│   │   └── download_dataset.py
│   ├── exceptions
│   │   ├── __init__.py
│   │   └── exceptions.py
│   ├── features
│   │   └── build_features.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── DataGenerator.py
│   │   ├── decoder.py
│   │   ├── encoder.py
│   │   └── tokenizer.py
│   ├── preprocess
│   │   ├── __init__.py
│   │   ├── cleaner.py
│   │   └── preprocess.py
│   ├── tests
│   └── visualization
│       ├── __init__.py
│       └── visualize.py
├── setup.py
├── requirements.txt
├── README.md
├── LICENSE
└── tox.ini
```
## Model Archtichtures

## Results

## Tools
- Python
- Tensorflow
- NumPy
- Pandas
- Matplotlib
- PyTest

## Try this model
```
```

## References
- [An Overview of Image Caption Generation Methods](https://www.hindawi.com/journals/cin/2020/3062706/)
- [Deep Learning Techniques for Image Captioning](https://researchrepository.murdoch.edu.au/id/eprint/60782/1/Hossain2020.pdf)
- [Image captioning with visual attention](https://www.tensorflow.org/tutorials/text/image_captioning)

  
## Contributing to this project
To contribute to Consolo, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contact

If you want to contact me you can reach me at hossamasaad10@gmail.com.
