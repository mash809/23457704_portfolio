import cv2
from imwatermark import WatermarkDecoder

# Load image
image = cv2.imread("watermarked.png")   # or regenerated.png

# Create decoder
decoder = WatermarkDecoder("bytes", 1)

# Decode watermark
watermark = decoder.decode(image, "dwtDct")

print("Recovered raw watermark bytes:", watermark)

try:
    print("Recovered text watermark:", watermark.decode("utf-8"))
except UnicodeDecodeError:
    print("Could not decode watermark as UTF-8 text.")
    print("This usually means the watermark was corrupted or not recovered exactly.")