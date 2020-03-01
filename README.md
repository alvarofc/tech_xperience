# Tech Xperience challenge

## Challenge description
In this challenge, the company asked to develop an image recognition software to recognize 4 different products. We were given a little set of pictures to make the prediction.

## Steps followed
### Image manipulations
It was clear that the set given was not enough to make an accurate model and the quality and background would also make it difficult. That´s why I decided to crop the pictures to just show the product also, in order to have more images in our set, I decided to rotate all the images from 15 to 360 degrees in 15 degrees intervals. (you can find the method used in the image_man.py file)
At the end, I managed to get 384 pictures of each product and then selected 305 to train and 79 to test the results.

### Model
I trained the model based on the imageai library using the pictures we got from the previous step. 

## Result
You can check the final model downloading the philips_cv.h5 file from the repo and use the model_class.json to retreive the labels.

## Further steps
I'm currently trying to upload the model to a webpage to be able to analyze pictures without the need of having the model locally. 
Check progress here: http://philips.us-east-2.elasticbeanstalk.com/
