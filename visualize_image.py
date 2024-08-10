import cv2
import matplotlib.pyplot as plt

img_path = "images/00029.jpg"
bgr_img = cv2.imread(img_path)
img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB) 
height, width, channels = img.shape
print(f"H : {height}, W : {width}, CH : {channels}")

plt.subplots_adjust(bottom=0.1, top=0.95)
plt.xlabel('x')
plt.ylabel('y')
plt.imshow(img, extent=[0, 1, 1, 0])
plt.title('Food Dataset')
plt.show()