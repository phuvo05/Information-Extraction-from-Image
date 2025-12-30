import os
import random
import shutil
import time
import xml.etree.ElementTree as ET

import cv2
import matplotlib.pyplot as plt
import numpy as np
import timm
import torch
import torch.nn as nn
import ultralytics
import yaml
from PIL import Image
from sklearn.model_selection import train_test_split
from torch.nn import functional as F
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
from ultralytics import YOLO

import json
import easyocr
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import Levenshtein

# # Configure matplotlib for inline display in Jupyter notebooks
# %matplotlib inline

ultralytics.checks()
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")