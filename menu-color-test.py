import cv2
import numpy as np

kembali = 'y'

while True:
    print("::::: Menu :::::")
    print("1. Cek warna biru")
    print("2. Cek warna hijau")
    print("3. Cek warna kuning")
    print("4. Cek warna biru dan hijau")
    print("5. Cek warna kuning dan hijau")
    print("6. Keluar")
    pilih = input("Pilih : ")

    if pilih == '1':
        print("\n::::: Cek Warna Biru :::::")
        for i in range(1, 4):
            img = cv2.imread('Asset0'+str(i)+'.png', 1)
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            # [100, 100, 100], [120, 255, 255] – Biru
            lower_api0 = np.array([100, 100, 100])
            upper_api0 = np.array([120, 255, 255])
            mask1 = cv2.inRange(hsv, lower_api0, upper_api0)

            mask = mask1
            new_img = cv2.bitwise_and(img, img, mask=mask)

            cv2.imshow("hasil"+str(i)+".png", new_img)
            cv2.imshow('image', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            pass
        kembali = input("\nkembali? (y/n) : ")
        pass

    if pilih == '2':
        print("\n::::: Cek Warna Hijau :::::")
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
            cv2.imshow('image', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            pass
        kembali = input("\nkembali? (y/n) : ")
        pass

    if pilih == '6':
        break
        pass
    if kembali == 'n':
        break
        pass
    pass
