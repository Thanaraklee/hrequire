import os
import sys
import math

import pandas as pd               
import numpy as np                
import matplotlib.pyplot as plt   

from datetime import datetime, timedelta
from collections import defaultdict, Counter

from math import sqrt, pi

from bs4 import BeautifulSoup     
import yaml                       
import PIL.Image as Image         
import sklearn.metrics as skm    
import cv2                        
from langchain.chains import LLMChain
from google.auth import impersonated_credentials

import importlib

def example_usage():
    html = "<html><body><h1>Test</h1></body></html>"
    soup = BeautifulSoup(html, "html.parser")
    print("HTML title:", soup.h1.text)

    data = {"name": "Thanarak", "age": 30}
    yaml_str = yaml.dump(data)
    print("YAML:", yaml_str)

    print("Square root of 16:", sqrt(16))
    print("Pi value:", pi)
    print("Today:", datetime.now())

if __name__ == "__main__":
    example_usage()
