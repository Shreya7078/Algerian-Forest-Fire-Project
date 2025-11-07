from flask import Flask,request,jsonify,render_template
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
#render_template is used for url of any html file , when we use it, it looks for the html file present in the templates folder

application=Flask(__name__)
app=application 

## import ridge regressor and standard  scaler pickle
ridge_model=pickle.load(open('models/ridge.pkl','rb'))
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))


## Route for home page
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
      if request.method=="POST":
           Temperature=float(request.form.get('Temperature'))
           RH=float(request.form.get('RH'))
           Ws=float(request.form.get('Ws'))
           Rain=float(request.form.get('Rain'))
           FFMC=float(request.form.get('FFMC'))
           DMC=float(request.form.get('DMC'))
           ISI=float(request.form.get('ISI'))
           Classes=float(request.form.get('Classes'))
           Region=float(request.form.get('Region'))

           new_data_scaled=standard_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
           result=ridge_model.predict(new_data_scaled)

           return render_template('home.html',results=result[0])

      else:
           return render_template('home.html')



if __name__=="__main__":
    app.run(host="0.0.0.0") #port can also be passed here for running the application on a specific port
    #is mapped to the local Ip address of any machine on which you are working
