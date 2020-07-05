# Keystroke Authentication Using Autoencoder

Keystroke dynamics, uses the information of how a person  interact with his  keyboard to draw his  digital fingerprint.
It deals with recording  the speed at which a user  type, the latency in his  keystrokes, the amount of pressure a valid user  apply on the keys, the key combinations you use, and a few other things. This, according to studies and different research, is unique per person. So it becomes easy to identify if user of a system is its valid ,authentic user or an intruder.

The combination of username and password have been used for security since very long time for all kinds of data and services online, including  to emails, banking, and gaming services etc .But it’s been proved a lot many times that this kind of security doesn’t really work well. If an intruder is able to crack passwords then very easily he will be able to enter the system and access it. 

In this Research Project ,I have combined Autoencoder with SVM and PCA as an oddity detection strategy with other different models like ,logistic regression,Random Forest Classifier, Decision Tree Classifier etc

# Data Acquisition
Our dataset generation is unique for each individual user. Each original user has  his own dataset, which will contain his password written many times by different users including himself(valid user) as well as other users who are not valid(imposters).This will enable our model to differentiate the
typing pattern of original user from others.
Dataset consists of 2 features , flight time and hold time.If length of password is n , then dimensions of the dataset will be 2n-1.We can use capital letters and all types of special characters.

# Results
In the results , I have shown Training and Testing Accuracies of different models with and without Autoencoder .

Let's now install the Hardware and Software part of project.

## Hardware Requirements

1. Laptop or Computer system  with keyboard.

## Software requirements

1. Jupyter notebook
2. Linux Operating system(For data generation)

## Installation

# Python libraries:
* Tensorflow
* Keras
* Sklearn

# Data Generation Library:
* Pyxhook - A library that allows you to listen for keyboard events on Linux.


## Running the project

1. Clone the repository.
2. Go to data_gen folder and run datagen.py as follows:

N = Number of times you want to write the password in 1 go.
dataset_name = Name of the csv file which will bw generated for the original user.

python3 datagen.py  N dataset_name

Then write the Name of the original and password to be set for the first time and  write the  password N number of times with pressing enter after writing whole password each time.

You will get the Down time, Up Time, Flight time, Dwell Time.The data of the user will be generated in the folder dataset with name  as "dataset_name".

Note-Length of the password should be of length 9 .
Password can contain lower case letters, upper case letters , numbers and special characters as well.
For upper case use shift key rather than capslock.

3. Copy this dataset generated in the folder "model" inside "keystroke_dy" folder.
4. To generate weights  run the file model.py in the folder "model".


For details refer [here](http://www.journaleca.com/gallery/jeca-2129.04-f.pdf).
 
Contributions highly appreciated!
