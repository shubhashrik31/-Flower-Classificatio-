from flask import Flask,jsonify,render_template,request
from project_app.utils import MedicalInsurance
import numpy as np
app = Flask(__name__)

####home page
@app.route('/')
def homepage():
    print('flower Project')
    return render_template('homepage.html')


####result.html
@app.route('/predict',methods = ['POST','GET'])
def get_insurance_charges():
    if request.method == 'POST':
        print('We are in POST Method')
        data = request.form
        print(data)
        one=data['one']
        two=data['two']
        three = data['three']
        four = data['four']
        print(data)
        print(f'one >> {one}, two >>{two} , three >> {three},four >> {four}')
        med_ins = MedicalInsurance(one,two,three,four)    
        Charges = med_ins.predict_charges()
        return render_template('Result.html',Charges=Charges)
        # return jsonify({f'Hello {name}': f' Your Predicted Medical Insurance Charges are:  RS.{Charges} '})
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)   