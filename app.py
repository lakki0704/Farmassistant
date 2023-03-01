import numpy as np
from flask import Flask, render_template,request
import pickle#Initialize the flask App
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    int_features = [float(x) for x in request.form.values()]
    final_features = np.array(int_features).reshape(1,-1)
    prediction = model.predict(final_features)
    return render_template('index.html', prediction_text=' Recommended Crop : {}'.format(cropname(prediction)))

#rice = 1 , maize = 2 , chickpea -3 ,kidneybeans -4 , pigeonpeas -5, mothbeans -6 , mungbean -7, blackgram -8
#lentil -9 , pomegrenate =10 , banana =11, mango -12 , grapes -13 ,watermelon -14  , muskmelon -15, apple -16
#orange - 17, papaya -18 ,coconut -19 ,cotton -20, jute -21,coffee-22,

def cropname(num):
    if(num==1):
        return "Rice"
    elif(num==2):
        return "Maize"
    elif(num==3):
        return "Chickpea"
    elif (num == 4):
        return "Kidneybeans"
    elif (num == 5):
        return "Pigeonpeas"
    elif (num == 6):
        return "Mothbeans"
    elif (num == 7):
        return "Mungbean"
    elif (num == 8):
        return "Blackgram"
    elif (num == 9):
        return "lentil"
    elif (num ==10 ):
        return "Pomegrenate"
    elif (num ==11 ):
        return "banana"
    elif (num == 12):
        return "Mango"
    elif (num == 13):
        return "Grapes"
    elif (num == 14):
        return "Watermelon"
    elif (num == 15):
        return "Muskmelon"
    elif (num == 16):
        return "Apple"
    elif (num ==17 ):
        return "Orange"
    elif (num ==18 ):
        return "Papaya"
    elif (num == 19):
        return "Coconut"
    elif (num ==20):
        return "Cotton"
    elif (num == 21 ):
        return "Jute"
    elif (num == 22):
        return "Coffee"

#banana =11, mango -12 , grapes -13 ,watermelon -14  , muskmelon -15, apple -16
#orange - 17, papaya -18 ,coconut -19 ,cotton -20, jute -21,coffee-22,

if __name__ == "__main__":
    app.run(debug=True)