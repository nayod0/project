import requests
import numpy as np
from PIL import Image as im3
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import base64 
from PIL import Image
import io
import time

imageFilename = "Cat4.png"
files = {'file' : open(imageFileName, 'rb')}
rq = requests.post("https://angsila.informatics.buu.ac.th/~64160025/test_import_img/dbwrite.php", files=files)
chack_url = rq.text
print("the sensor data is :{}".format(chack_url))