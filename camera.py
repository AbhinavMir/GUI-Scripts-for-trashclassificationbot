import cv2
import os
cam = cv2.VideoCapture(0)
if(os.path.exist(c:/users/hp/desktop/test'):
	os.chdir('c:/users/hp/desktop/test')
else:
	os.mkdir('c:/users/hp/desktop/test')
	os.chdir('c:/users/hp/desktop/test')
	
cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "im.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
