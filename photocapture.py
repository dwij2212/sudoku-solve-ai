import cv2.cv2 as cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0


def capture_img():
    """Returns None if image is not captured and returns an image if successfully captured"""
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            return None
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            return None
            
        elif k%256 == 32:
            # SPACE pressed
            # img_name = "opencv_frame_{}.png".format(img_counter)
            # cv2.imwrite(img_name, frame)
            # print("{} written!".format(img_name))
            # img_counter += 1
            img = frame
            break
    
    return img

while True:
    img = capture_img()

    if img is not None:
        #show the captured image
        print("Captured image will be shown, input 'y' if its correct.")
        cv2.imshow('captured', img)
        cv2.waitKey()
        cv2.destroyAllWindows()
        ch = input("Y/y or N/n:")
        if ch == 'Y' or ch == 'y':
            break
        else:
            continue

    else:
        print("Error in capturing image.")

cam.release()

cv2.destroyAllWindows()