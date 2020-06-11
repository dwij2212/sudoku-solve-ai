import cv2.cv2 as cv2


def capture_img():
    """Returns None if image is not captured and returns an image if successfully captured"""
    cam = cv2.VideoCapture(0)


    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            return None
        cv2.imshow("Capture (Space to capture)", frame)

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

    cam.release()
    cv2.destroyAllWindows()
    return img

def capture():
    

    while True:
        img = capture_img()

        if img is not None:
            #show the captured image
            print("Captured image will be shown")
            
            cv2.imshow('Captured  (Press any key to continue)', img)
            cv2.waitKey()
            cv2.destroyAllWindows()

            print("Input 'y' if satisfied, or input 'n' if you want to retake.")
            ch = input("Y/y or N/n:")
            if ch == 'Y' or ch == 'y':
                return img
            else:
                continue

        else:
            print("Error in capturing image.")

    
