from gridextractor import pre_process_image, find_corners_of_largest_polygon, crop_and_warp, infer_grid, show_image,get_digits
from predictor import model, predict_sudoku, print_sudoku
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
    
    def change_sudoku(sudoku, i, j, n):
        sudoku[i][j] = n
    
    def make_change():
        while True:
            
            print("satisfied? (y/n)")
            ch = input()
            if ch == 'y' or 'Y':
                break

            print("first number, then row number(starts from 0), then column number(Starts from 0)")
            num = int(input())
            i = int(input())
            j = int(input())

            change_sudoku(sudoku, i, j, num)

            

    
    #predict grid
    sudoku = predict_sudoku(digits)

    print_sudoku(sudoku)

    #ask if any changes required
    make_change()






if __name__=="__main__":
    main()