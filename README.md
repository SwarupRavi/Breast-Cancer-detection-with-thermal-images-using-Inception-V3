# Breast Cancer detection with thermal images using Inception V3

We have used a Keras CNN model called Inception V3 here..

For Thermal images we got an test accuracy of 56%

# Sample images


left side image is with positive cancer in the breast and the right side image is a healthy breast

<img width="345" alt="Screenshot 2024-04-03 at 4 11 09 PM" src="https://github.com/SwarupRavi/Breast-Cancer-detection-with-thermal-images-using-Inception-V3/assets/79323627/29befeb7-f55b-44ab-a65c-7cfdadacd96b">




<img width="332" alt="Screenshot 2024-04-03 at 4 11 21 PM" src="https://github.com/SwarupRavi/Breast-Cancer-detection-with-thermal-images-using-Inception-V3/assets/79323627/9f8b66d8-98e7-43e6-acc8-0cbb7485d693">










Post all the preprocessing

<img width="328" alt="Screenshot 2024-04-03 at 4 13 38 PM" src="https://github.com/SwarupRavi/Breast-Cancer-detection-with-thermal-images-using-Inception-V3/assets/79323627/517e266e-d5de-4734-89c3-995e6b0d7c09">





<img width="324" alt="Screenshot 2024-04-03 at 4 13 05 PM" src="https://github.com/SwarupRavi/Breast-Cancer-detection-with-thermal-images-using-Inception-V3/assets/79323627/9492f001-c164-4ef7-a9c4-f92cb21bee64">




# Train test split and Inference

The model was split into 80%-20% ratio as 80 being the training and 20 being the test split


img height=480
img width=640
classes=1
batch size= 32
epoch=3

inception = InceptionV3(input_shape=(480, 640, 3), weights='imagenet', include_top = False)


Training accuracy

<img width="652" alt="Screenshot 2024-04-03 at 4 16 55 PM" src="https://github.com/SwarupRavi/Breast-Cancer-detection-with-thermal-images-using-Inception-V3/assets/79323627/436d68f6-b301-44b0-927d-21971885c845">




Test Accuracy

<img width="618" alt="Screenshot 2024-04-03 at 4 18 19 PM" src="https://github.com/SwarupRavi/Breast-Cancer-detection-with-thermal-images-using-Inception-V3/assets/79323627/db86efc9-a800-4460-acd2-5a2291f5ce6a">



Confusion Matrix

<img width="539" alt="Screenshot 2024-04-03 at 4 18 44 PM" src="https://github.com/SwarupRavi/Breast-Cancer-detection-with-thermal-images-using-Inception-V3/assets/79323627/fd342bfb-6687-4812-a992-969b364b1bd1">










