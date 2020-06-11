import os

import tensorflow as tf
from tensorflow import keras
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator, NumpyArrayIterator

model = tf.keras.models.load_model('scanned_digit2.h5')
# model.summary()
"""
Model: "sequential_10"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================`
conv2d_60 (Conv2D)           (None, 26, 26, 32)        320       
_________________________________________________________________
batch_normalization_70 (Batc (None, 26, 26, 32)        128       
_________________________________________________________________
conv2d_61 (Conv2D)           (None, 24, 24, 32)        9248      
_________________________________________________________________
batch_normalization_71 (Batc (None, 24, 24, 32)        128       
_________________________________________________________________
conv2d_62 (Conv2D)           (None, 12, 12, 32)        25632     
_________________________________________________________________
batch_normalization_72 (Batc (None, 12, 12, 32)        128       
_________________________________________________________________
dropout_30 (Dropout)         (None, 12, 12, 32)        0         
_________________________________________________________________
conv2d_63 (Conv2D)           (None, 10, 10, 64)        18496     
_________________________________________________________________
batch_normalization_73 (Batc (None, 10, 10, 64)        256       
_________________________________________________________________
conv2d_64 (Conv2D)           (None, 8, 8, 64)          36928     
_________________________________________________________________
batch_normalization_74 (Batc (None, 8, 8, 64)          256       
_________________________________________________________________
conv2d_65 (Conv2D)           (None, 4, 4, 64)          102464    
_________________________________________________________________
batch_normalization_75 (Batc (None, 4, 4, 64)          256       
_________________________________________________________________
dropout_31 (Dropout)         (None, 4, 4, 64)          0         
_________________________________________________________________
flatten_10 (Flatten)         (None, 1024)              0         
_________________________________________________________________
dense_20 (Dense)             (None, 128)               131200    
_________________________________________________________________
batch_normalization_76 (Batc (None, 128)               512       
_________________________________________________________________
dropout_32 (Dropout)         (None, 128)               0         
_________________________________________________________________
dense_21 (Dense)             (None, 10)                1290      
=================================================================
Total params: 327,242
Trainable params: 326,410
Non-trainable params: 832
_________________________________________________________________
"""

def predict_image(img):
  # cv2_imshow(img)
  # final = cv2.resize(processed, (28, 28))
  final = img.reshape(-1,28,28,1)/255

  pred = model.predict(final)

  #to print digits about which NN is not sure about.
  if np.max(pred) < 0.9:

    return np.argmax(pred) + 0.5 

  return np.argmax(pred)


def predict_sudoku(digits):
    sudoku = np.zeros((9,9))

    for i in range(9):
        for j in range(9):
            digit = digits[i*9 + j]
            #classify blank image as 0 by assumption that sum of all pixel values of that digit is less than 1000.
            if digit.sum() < 1000:
                sudoku[i][j] = 0
            else:
                sudoku[i][j] = predict_image(digit)

    return sudoku


def print_sudoku(sudoku):
  if sudoku is None:
    print("No solution")
  
  else:
    sudoku = np.array(sudoku)
    i,j = sudoku.shape
    if i != 9 and j != 9:
      print("Not valid puzzle")
    
    else:
      for i in range(9):
        for j in range(9):
          if sudoku[i][j] != 0 and (sudoku[i][j] - int(sudoku[i][j]) == 0):
            print("%s    " % int(sudoku[i][j]), end="")
          
          elif sudoku[i][j] != 0 and (sudoku[i][j] - int(sudoku[i][j]) != 0):
            print("%s  " % (sudoku[i][j]), end="")
            
          else:
            print("X    ", end ="")
        print()
        

def train_model(sudoku, epochs = 5, digits = None):
  """retrains model on new set of images to increase accuracy in future"""

  if digits is not None:
    print("Now fitting model on new data.")

    train_images = np.empty((0,28,28,1))
    train_labels = np.empty((0))

    for i in range(9):
      for j in range(9):
        if sudoku[i][j] != 0:

          img = digits[i*9 + j]
          img = img.reshape(1,28,28,1)
          train_images = np.append(train_images, img, axis = 0)
          train_labels = np.append(train_labels, sudoku[i][j])

    train_images = train_images/255.0
    train_labels = keras.utils.to_categorical(train_labels)

    datagen = ImageDataGenerator(rotation_range=5, data_format="channels_last", validation_split=0.1)
    train_data = datagen.flow(x=train_images, y=train_labels)

    #load model
    model = tf.keras.models.load_model('scanned_digit2.h5')

    #retrain model on new images
    model.fit(train_data, epochs=5, verbose=0)
    print("Successfully upgraded your model.")

    #save the model
    model.save('scanned_digit2.h5', save_format='h5')
    print("Successfully saved your model.")