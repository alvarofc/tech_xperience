import tensorflow as tf
import keras as k
import cv2
from imageai.Prediction.Custom import ModelTraining

model_trainer = ModelTraining()
model_trainer.setModelTypeAsResNet()
model_trainer.setDataDirectory("pics")
model_trainer.trainModel(num_objects=4, num_experiments=200, enhance_data=True, batch_size=32, show_network_summary=True)
