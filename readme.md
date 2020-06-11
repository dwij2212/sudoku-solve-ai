# sudoku-solve-ai
A summer project made using tensorflow's keras API and opencv library. The program detects a sudoku from an image and solves it accordingly. 

## Getting Started
Run the following commands in your windows terminal to get the project running locally.
Make sure your python version is between 3.6-3.8.

```bash
git clone https://github.com/dwij2212/sudoku-solve-ai
```
Create a virtualenv and activate
```bash
python3 -m venv myvenv
myvenv\Scripts\activate
```
Run this to setup the dependencies in your virtual environment
```bash
pip install -r requirements.txt
```
## Usage
Go to the program main.py and change the following line in order to use your own image for recognition.

```python
#main.py

...
    img = cv2.imread(PATH_TO_YOUR_IMAGE, 0)
...

```
Pass the path to your image in the argument of imread.
Now run the following command in your terminal to run the program.

```bash
python3 main.py
```
## Modify how your program works
In the file main.py, make the following changes to capture image from your camera.
```python
#get image from camera or local path
#img = cv2.imread('sudokuimg.jpg', 0)

#uncomment this line and comment line above this to capture image from your camera and solve
img = capture()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```

## Upgrade model
What upgrading your model basically means is fitting your model on the data fed to program during runtime.
Make sure all data fed to the model is correct i.e. the sudoku is printed correctly before training or else model will become inaccurate.
This can be enabled by making the following change in main.py
```python
UPGRADE_MODEL = True
```
Since this step is computationally expensive for large dataset, it is False by default.



