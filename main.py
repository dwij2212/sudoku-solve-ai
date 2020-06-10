from gridextractor import *
from predictor import *
import cv2.cv2 as cv2
from photocapture import capture

def main():
    #get image from camera
    img = capture()
    
    #pre-process image
    proc = pre_process_image(img)

    #find 4 corners of sudoku
    points = find_corners_of_largest_polygon(proc)

    # img = display_points(img, points)
    #crop and warp the image wrt the pts
    cropped = crop_and_warp(img, points)

    #get points of 81 squares from cropped image
    squares = infer_grid(cropped)

    show_image(cropped)

    #extract digits of size 28 from cropped image, we then predict on these extracted digits
    digits = get_digits(cropped, squares, size=28)
    

    final = digits[1].reshape(-1,28,28,1)/255

    pred = model.predict(final)
    print(pred)

    def change_sudoku(sudoku, i, j, n):
        sudoku[i][j] = n

    sudoku = predict_sudoku(digits)

    print_sudoku(sudoku)







if __name__=="__main__":
    main()