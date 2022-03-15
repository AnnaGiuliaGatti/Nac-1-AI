#!/usr/bin/python
# -*- coding: utf-8 -*-

# Programa simples com camera webcam e opencv

import cv2
import os,sys, os.path
import numpy as np


def image_da_webcam(img):
    """
    ->>> !!!! FECHE A JANELA COM A TECLA ESC !!!! <<<<-
        deve receber a imagem da camera e retornar uma imagems filtrada.
    """
#    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)



    image_lower_hsvB = np.array([70, 130, 100])  
    image_upper_hsvB = np.array([130, 255, 255])

    mask_hsvB = cv2.inRange(img_hsv, image_lower_hsvB, image_upper_hsvB)

    image_lower_hsv1 = np.array([0, 100, 100])  
    image_upper_hsv1 = np.array([15, 255, 255])

    mask_hsv1 = cv2.inRange(img_hsv, image_lower_hsv1, image_upper_hsv1)

    image_lower_hsv2 = np.array([165, 100, 100])  
    image_upper_hsv2 = np.array([180, 255, 255])

    mask_hsv2 = cv2.inRange(img_hsv, image_lower_hsv2, image_upper_hsv2)

    mask_hsvR = cv2.bitwise_or(mask_hsv1, mask_hsv2)


    mask_hsvFinal = cv2.bitwise_or(mask_hsvR, mask_hsvB)

    return mask_hsvFinal

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)


if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    
    img = image_da_webcam(frame)


    cv2.imshow("preview", img)

    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cv2.destroyWindow("preview")
vc.release()
