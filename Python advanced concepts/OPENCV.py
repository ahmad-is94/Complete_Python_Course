import cv2
import urllib.request
from matplotlib import pyplot as plt

# 1. Test image URL (Hum internet se ek image download karenge)
image_url = "https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg"
image_path = "test_image.jpg"

print("Downloading test image...")
try:
    # Image ko computer mein save karein
    urllib.request.urlretrieve(image_url, image_path)
    print("Download complete!")
except Exception as e:
    print(f"Internet error: Image download nahi ho saki: {e}")
    exit()

# 2. Image ko OpenCV se open karein
img = cv2.imread(image_path)
if img is None:
    raise FileNotFoundError("Image load nahi ho saki!")

# 3. Colors change karein (gray for detection, RGB for plotting)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 4. Built-in Haar Cascade load karein (Face detection ke liye)
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

# 5. Face detection run karein
detections = face_cascade.detectMultiScale(
    img_gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

print(f"Total faces detected: {len(detections)}")

# 6. Har face ke gird green box lagayein
for (x, y, width, height) in detections:
    cv2.rectangle(img_rgb, (x, y), (x + width, y + height), (0, 255, 0), 3)

# 7. Image show karein
plt.imshow(img_rgb)
plt.axis("off")
plt.show()