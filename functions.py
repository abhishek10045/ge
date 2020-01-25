from random import randint
from utils.Doctor import Doctor
from utils.Classifier import Classifier
import pickle

MODEL_FILE = 'model.pickle'

def listDoctors():
    doctors = []
    for i in range(65, 75):
        doctors.append(Doctor(chr(i) * 10, i ** 5))
    return doctors

def getResult(eye_img):
    with open(MODEL_FILE, 'rb') as file:
        # classifier = Classifier(pickle.load(file))
        # return classifier.predict(eye_img)
    return randint(0, 5)
    