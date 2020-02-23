# jika ingin dicoba dengan file png yang berbeda maka ubah Asset0 menjadi sesuai dgn nama file png dan ubah range jika ingin mencoba lebih atau kurang dari 3 file png
import cv2
import numpy as np

for i in range(1, 4):
    img = cv2.imread('Asset0'+str(i)+'.png', 1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # [50, 100, 100], [70, 255, 255] – Hijau
    lower_api0 = np.array([50, 100, 100])
    upper_api0 = np.array([70, 255, 255])
    mask1 = cv2.inRange(hsv, lower_api0, upper_api0)

    mask = mask1

    new_img = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("hasil"+str(i)+".png", new_img)
    # cv2.imshow('mask',mask)
    cv2.imshow('image', img)

    # menunggu tombol key ditekan
    cv2.waitKey(0)
    cv2.destroyAllWindows()
