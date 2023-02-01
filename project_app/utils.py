import numpy as np
import pandas as pd
import config
import pickle


import warnings
warnings.filterwarnings('ignore')

class MedicalInsurance:
    
    def __init__(self,one,two,three,four):
        
        self.one = one
        self.two = two
        self.three = three
        self.four = four
   
        
    def load_model(self):
       
        with open(config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)
        
    def predict_charges(self):
        
        self.load_model()
        test_array = np.zeros(4)
        test_array[0] = self.one
        test_array[1] = self.two
        test_array[2] = self.three
        test_array[3] = self.four
        
        result = self.model.predict([test_array])
        print(result[0])
        return result[0]

if __name__ == '__main__':
    obj=MedicalInsurance(5.1,3.5,1.4,0.2)
    obj.predict_charges()