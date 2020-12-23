from cv2 import (
    CascadeClassifier,
    imread,
    imshow,
    resize,
    INTER_AREA,
    cvtColor,
    COLOR_BGR2GRAY,
    rectangle,
    waitKey,
    data
)

from colors import Colors

def main():
    haar_model_path = data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = CascadeClassifier(haar_model_path)
    input_image = imread('input.jpg')

    scale_coefficient = 0.25
    image_width = int(input_image.shape[1] * scale_coefficient)
    image_height = int(input_image.shape[0] * scale_coefficient)
    dimensions = (image_width, image_height)

    resized_image = resize(input_image, dimensions, interpolation=INTER_AREA)
    gray_scaled_color = cvtColor(resized_image, COLOR_BGR2GRAY)

    for (x, y, width, height) in face_cascade.detectMultiScale(gray_scaled_color, 1.1, 12):
        red_color = (0, 0, 255)
        rectangle(resized_image, (x, y), (x + width, y + height), red_color, 2)

    imshow('result', resized_image)
    waitKey()


if __name__ == "__main__":
    main()