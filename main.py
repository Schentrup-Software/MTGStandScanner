from mtgstand_api import getCard
from scan_main import cropImage
from picamera import PiCamera

imageName = "rawImage.png"

camera = PiCamera()
camera.capture(imageName)

newImage = cropImage(imageName)

getCard(newImage)

#os.remove(newImage)
#os.remove(file_name)