import cv2
import numpy
import os
import time

def capture(width, height, timeout=0, path='face.jpg'):
    command = 'raspistill  --width ' + str(width) + ' --height ' + str(height) + ' --timeout ' + str(timeout) + ' --output ' + str(path)
    os.system(command)

def detect(path):
    img = cv2.imread(path)
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    rects = cascade.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))

    if len(rects) == 0:
        print 0
        return [], img
    else:
        print 2
        rects[:, 2:] += rects[:, :2]
        return rects, img

def box(rects, img):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), (127, 255, 0), 2)
    cv2.imwrite('face_box.jpg', img);
    im = cv2.imread('face_box.jpg')

    ## Display code for testing purposes
##    numberRows, numberColumns, numberBands = numpy.shape(im)
##    displayRows = numberRows
##    displayColumns = numberColumns
##    cv2.namedWindow('Facial Detection', cv2.WINDOW_AUTOSIZE)
##    cv2.imshow('Facial Detection', cv2.resize(im, (displayColumns, displayRows)))
##    cv2.waitKey(0)


capture(640, 480)
rects, img = detect('face.jpg')
box(rects, img)
