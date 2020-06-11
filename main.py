from gridextractor import pre_process_image, find_corners_of_largest_polygon, crop_and_warp, infer_grid, show_image,get_digits
from predictor import model, predict_sudoku, print_sudoku, train_model
import cv2.cv2 as cv2
from photocapture import capture
from solve import solve, isinvalid

#Upgrade model with new data i.e. train model with existing digits
#WARNING: Keep this false until and unless you want to retrain your model which is computationally expensive.
UPGRADE_MODEL = False

def main():
    #get image from camera or local path
    img = cv2.imread('sudokuimg.jpg', 0)

    #uncomment this line and comment line above this to capture image from your camera and solve
    # img = capture()

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

            ch = input("Satisfied? (y/n)")
            change_required = isinvalid(sudoku)
            if ch == 'n' or ch == 'N' or change_required:

                num = int(input("Enter corrected number: "))
                i = int(input("row number(starts from 0): "))
                j = int(input("col number(starts from 0): "))
                change_sudoku(sudoku, i, j, num)
                print_sudoku(sudoku)

            elif ch == 'y' or ch == 'Y':
                break

            else:
                print("Enter valid input.")
            

    
    #predict and print grid
    sudoku = predict_sudoku(digits)

    print("Those numbers with decimals are those about which model is unsure of.")
    print("Please check those numbers and correct them.")
    print("Also just have a quick look at other numbers to verify if they are correct.")
    print_sudoku(sudoku)

    #ask if any changes required
    make_change()
    train_sudoku = sudoku
    solved = solve(sudoku)

    if UPGRADE_MODEL and solved is not None:
        train_model(sudoku = train_sudoku, epochs=5, digits = digits)

    print("Answer: ")
    print_sudoku(solved)





if __name__=="__main__":
    main()