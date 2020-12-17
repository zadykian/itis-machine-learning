import numpy
import pygame
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten, Dense
from pathlib import Path
import tensorflow
from keras.models import load_model
from PIL import Image

# Распознаватель цифр.
class DigitRecognizer:

    def __init__(self):
        model_file_name = 'neural.keras'
        self._model = load_model(model_file_name) \
            if Path(model_file_name).exists() \
            else DigitRecognizer._create_and_save_model(model_file_name)

    @staticmethod
    def _create_and_save_model(model_file_name: str):
        digits_dataset = tensorflow.keras.datasets.mnist
        (x_train, y_train), (_, _) = digits_dataset.load_data()

        x_train = tensorflow.keras.utils.normalize(x_train, axis=1)
        # tensorflow.keras.utils.normalize(x_test, axis=1)

        model = Sequential()
        model.add(Flatten())

        model.add(Dense(256, activation=tensorflow.nn.relu))
        model.add(Dense(256, activation=tensorflow.nn.relu))
        model.add(Dense(10, activation=tensorflow.nn.softmax))

        model.compile(
            optimizer="adam",
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"])

        model.fit(x=x_train, y=y_train, epochs=16)
        model.save(model_file_name)
        return model

    # Распознать цифру.
    def recognize_digit(self, digit):
        path = 'digit.png'
        pygame.image.save(digit, path)
        img = Image.open(path)
        img = img.resize((28, 28))
        img = img.convert('L')
        img = numpy.array(img)
        img = img.reshape(1, 28, 28, 1)
        img = img / 255.0
        prediction = self._model.predict([img])[0]
        res = prediction.argsort()[::-1]
        print(res)