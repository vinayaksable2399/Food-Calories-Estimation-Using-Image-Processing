
<b><span style="color: red; font-family: Babas; font-size: 2em;">Food Calories Estimation Using Image Processing</span></b>
<img src="1.jpg" alt="python" width="150" height="190" align="right">

## [Vinayak Sable](https://www.linkedin.com/in/vinayak-sable-675502131) 

+ ###  Problem
 The problem can be simply stated as, given a set of food images with calibration object thumb with the food name and an unlabeled set of food images from the same group of food, identify food and estimate food volume and calories intake.
+ ### Objectives
 1.	To detect food type by using Convolutional Neural Network (CNN)
 2.	To estimate food weight and calories of food

+ ### Data collection
 For this project I used two datasets:
    1. FOODD
    2. ECUST Food Dataset (ECUSTFD)
  >In this project I used 6 food items like apple, banana, carrot, cucumber, onion, orange and tomato which details given in table below

| Fruits | Density |	Calorie | Label |	Shape |
|--------|---------|----------|--------|---------|
| Apple| 	0.609 | 	52 | 	1	| Sphere | 
| Banana |	0.94 |	89 |	2 |	Cylinder |
| Carrot |	0.641|	41 |3	|Cylinder|
|Cucumber|	0.641|	16	|4|	Cylinder|
|Onion	|0.513|	40|	5|	Sphere|
|Orange	|0.482|	47|	6|	Sphere|
|Tomato	|0.481 |18|	7|	Sphere|
#### Sample food images in dataset:

<img src="2.png" alt="python" width="615" height="224" align="centre">


### Recognition method
Food Recognition deals with recognition of food item when given an image. For this problem I used Convolutional Neural Network (CNN). The Architecture of  CNN given below figure 
<img src="3.png" alt="python" width="615" height="224" align="centre">
> *all thids work done in ```cnn.py`` file*

### Requirements
+ Windows 10 Pro CPU 
+ Anaconda Distribution 4.6.11
+ Python
+ Tensorflow 
+ keras 


### model summary



### Estimation Method:
+ #### Image Segmentation:
A mixture of methods including canny edge detection, watershed segmentation, morphological operators and Otsu’s method were used to segment the food item to obtain the contour of the fruit and the contour of the thumb. We use the thumb finger for calibration purposes. The thumb is placed next to the dish while clicking the photo and this thumb gives us the estimate of the real-life size of the food item and helps estimate volume accurately.
> *all this done ```image_segment.py``` and ```calorie.py```*

### Result



### Limitation and Scope
+ #### Limitations:
    1.	Actual weight and calories can’t find due to image quality
    2.	Difficult To Find Appropriate Angle Between Fruit And Camera
    
+ #### Scope:
    1.	Estimate the calorie from all types of fruits.
    2.	Minimize error of calories estimation
    
### Reference:
   1. P.Pouladzadeh, S.Shirmohammadi, and R.Almaghrabi, “Measuring Calorie and Nutrition from Food Image”, IEEE Transactions on Instrumentation & Measurement, Vol.63, No.8, p.p. 1947 – 1956, August 2014.

   2. Parisa Pouladzadeh, Abdulsalam Yassine, and Shervin Shirmohammadi, “Foodd: An image-based food detection dataset for calorie measurement,” in InternationalConferenceonMultimediaAssistedDietaryManagement, 2015

   3. Meghana M Reddy, “Calorie-estimation-from-food-images-opencv”, [Git repo](https://github.com/meghanamreddy/Calorie-estimation-from-food-images-OpenCV) , May 2016




<a href="mailto:vinayak.sable.56@gmail.com">@vinayak</a> What do you think about these ?
