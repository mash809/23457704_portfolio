import cv2
from imwatermark import WatermarkEncoder

# Load image
img = cv2.imread("image.png")

# Create encoder
encoder = WatermarkEncoder()
encoder.set_watermark("bytes", b"W")

# Embed watermark
watermarked = encoder.encode(img, "dwtDct")

# Save result
cv2.imwrite("watermarked.png", watermarked)

print("Watermark applied and saved as watermarked.png")