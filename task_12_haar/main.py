from cv2 import (
    CascadeClassifier,
    imread,
    imshow,
    resize,
    INTER_AREA,
    cvtColor,
    COLOR_BGR2GRAY,
    rectangle,
    waitKey
)

from colors import Colors

def main():
    result_scale_percent = 50

    face_cascade = CascadeClassifier('haarcascade_frontalface_default.xml')
    img = imread('input.jpg')

    width = int(img.shape[1] * result_scale_percent / 100)
    height = int(img.shape[0] * result_scale_percent / 100)
    dim = (width, height)
    img = resize(img, dim, interpolation=INTER_AREA)

    gray = cvtColor(img, COLOR_BGR2GRAY)

    for (x, y, w, h) in face_cascade.detectMultiScale(gray, 1.1, 4):
        rectangle(img, (x, y), (x + w, y + h), Colors.blue, 2)

    imshow('Detection result', img)
    waitKey()


if __name__ == "__main__":
    main()