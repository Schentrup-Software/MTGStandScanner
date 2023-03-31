import os
from scan_main import cropImage
import time


file_name="test.jpg"
cmd1= "raspistill -o "
cmd1+=file_name
os.system(cmd1)

cropImage("test.jpg")

