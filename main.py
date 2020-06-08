from gridextractor import *
from predictor import *


def main():
    img = cv2.imread('Screenshot_20200605-200529.jpg', 0)
    proc = pre_process_image(img)

    points = find_corners_of_largest_polygon(proc)

    # img = display_points(img, points)
    cropped = crop_and_warp(img, points)

    #get points of 81 squares from cropped image
    squares = infer_grid(cropped)

    show_image(cropped)

    #extract digits of size 28 from cropped image, we then predict on these extracted digits
    digits = get_digits(cropped, squares, size=28)

    def change_sudoku(sudoku, i, j, n):
        sudoku[i][j] = n

    sudoku = predict_sudoku(digits)

    print_sudoku(sudoku)







if __name__=="__main__":
    main()