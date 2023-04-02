from mtgstand_api import getCard
import os
from scan_main import cropImage
import time


file_name="test.jpg"
cmd1= "raspistill -o "
cmd1+=file_name
os.system(cmd1)

newImage = cropImage("test.jpg")

getCard(newImage)

os.remove(newImage)
os.remove(file_name)