# Forest Fire Weather Index (FWI) Prediction

## Overview
Machine learning model to predict Forest Fire Weather Index using Ridge Regression with Flask web interface.

## Project Structure

RidgeLassoElasticNet/
├── models/           # Trained models (ridge.pkl, scaler.pkl)
├── notebooks/        # Jupyter notebooks and datasets
├── templates/        # HTML templates
├── application.py    # Flask web app
└── Requirements.txt  # Dependencies


## Features
- Input: Temperature, RH, Wind Speed, Rain, FFMC, DMC, ISI, Classes, Region
- Output: FWI prediction
- Model: Ridge Regression with StandardScaler
- Web Interface: Flask application

## Quick Start

1. Install dependencies:
bash
pip install -r Requirements.txt


2. Run application:
bash
python application.py


<<<<<<< HEAD
3. Access: Open browser → `http://localhost:5000`
=======
3. Access: Open browser → http://localhost:5000
>>>>>>> 557717b855f4d08be81470b99121ab07d4470418

## Usage
1. Fill weather parameters in the form
2. Click "Predict" 
3. Get FWI prediction result

### Example Input:

Temperature: 29, RH: 57, Ws: 18, Rain: 0.0
FFMC: 65.7, DMC: 3.4, ISI: 1.3
Classes: 0, Region: 0


## Model Details
- Algorithm: Ridge Regression (L2 regularization)
- Preprocessing: Removed multicollinear features (BUI, DC)
- Scaling: StandardScaler normalization
- Dataset: Algerian Forest Fires data

## Files
<<<<<<< HEAD
- `ModelTraining.ipynb`: Complete ML pipeline
- `application.py`: Flask web server
- `models/`: Saved model and scaler
- `templates/`: HTML interface
=======
- ModelTraining.ipynb: Complete ML pipeline
- application.py: Flask web server
- models/: Saved model and scaler
- templates/: HTML interface
>>>>>>> 557717b855f4d08be81470b99121ab07d4470418
