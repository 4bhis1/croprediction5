import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r"/*": {
       "origins": "*"
    }
})

model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    data=json.dumps(request.form)
    ko=json.loads(data)
    
#     return ko['Temprature']
    kl=[float(ko['Rainfall']),float(ko['Temprature']),float(ko['Nitrogen']),float(ko['Phosphorus']),float(ko['Potassium']),float(ko['Ph'])]
    
    a=['Bajra', 'Banana', 'Barley', 'Bean', 'Black pepper', 'Blackgram','Bottle Gourd', 'Brinjal', 'Cabbage', 'Cardamom', 'Carrot','Castor seed', 'Cauliflower', 'Chillies', 'Colocosia', 'Coriander','Cotton', 'Cowpea', 'Drum Stick', 'Garlic', 'Ginger', 'Gram',
       'Grapes', 'Groundnut', 'Guar seed', 'Horse-gram', 'Jowar', 'Jute','Khesari', 'Lady Finger', 'Lentil', 'Linseed', 'Maize', 'Mesta',
       'Moong(Green Gram)', 'Moth', 'Onion', 'Orange', 'Papaya','Peas & beans (Pulses)', 'Pineapple', 'Potato', 'Raddish', 'Ragi','Rice', 'Safflower', 'Sannhamp', 'Sesamum', 'Soyabean','Sugarcane', 'Sunflower', 'Sweet potato', 'Tapioca', 'Tomato',
       'Turmeric', 'Urad', 'Varagu', 'Wheat']
    dicti={}
#     b=int(DT.predict([kl]))
    prediction = model.predict([kl])
    output = prediction[0]
    dicti["Crop"]=a[output]
    return json.dumps(dicti)
#     return render_template('index.html', prediction_text='The predicted value is {}'.format(a[output]))

if __name__ == "__main__":
    app.run()