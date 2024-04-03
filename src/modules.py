import seaborn as sns #data visualization and statistical plotting.
from matplotlib import pyplot as plt # statistical data
import os
from PIL import Image   #Pillow library for manipulation diff images
import pandas as pd #data cleaning
import numpy as np #arrays
from sklearn.model_selection import train_test_split #split for training and testing
from tensorflow import keras #tensor flow API call for DNN
from tensorflow.keras.preprocessing.image import ImageDataGenerator #data augmentation and preprocessing
from tensorflow.keras.models import Sequential #api call
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense #CNN
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input
from keras import backend as K #backend module
from keras.utils import np_utils #utility functions for numerical operations
from tf_clahe import clahe #clahe
np.random.seed(1671) # for reproducibility
import os
import itertools
from itertools import repeat

#model based imports
from keras.optimizers import SGD, RMSprop, Adam #
from keras.layers.core import Activation
from keras.applications.inception_v3 import InceptionV3
from keras.models import Model
from keras.layers import Input, Conv2D, Dense, Flatten
from keras.layers.pooling.global_average_pooling2d import GlobalAveragePooling2D
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn import metrics
