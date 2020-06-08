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





