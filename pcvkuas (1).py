# -*- coding: utf-8 -*-
"""PCVKUAS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JoZ5_k42hqIq-rTsYxu5Nek9nh5JWnh4
"""

import cv2
from google.colab import files
from IPython.display import Image, display

"""upload file cascade.xml"""

uploaded = files.upload()

cascade_path = next(iter(uploaded))
cascade_classifier = cv2.CascadeClassifier(cascade_path)

"""upload gambar untuk ditest"""

uploaded = files.upload()

image_path = next(iter(uploaded))
image = cv2.imread(image_path)

"""mengkonversi gambar ke grayscale"""

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

traffic_lights = cascade_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

detected_traffic_lights = 0
for (x, y, w, h) in traffic_lights:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    detected_traffic_lights += 1

"""menghitung akurasi dalam menilai gambar"""

accuracy = detected_traffic_lights / len(traffic_lights) if len(traffic_lights) > 0 else 0

output_image_path = 'traffic_light_output.jpg'
cv2.imwrite(output_image_path, image)

label = "GO" if detected_traffic_lights > 0 else "STOP"

display(Image(image_path))
display(Image(output_image_path))

display(Image(image_path))
display(Image(output_image_path))

print("Perintah: {}".format(label))