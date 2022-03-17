from healthinsurance import HealthInsurance
import pickle
import pandas as pd
from flask import Flask, request, Response

print('init')
#loading model
model = pickle.load(open(r'/src/model/xgb_model.pkl', 'rb'))

#initialize API
app = Flask(__name__)

print('API initialize')
@app.route('/predict', methods=['POST'])
def healthinsurance_predict():
    test_json = request.get_json()
    if test_json: #there is data
        if isinstance(test_json, dict):  #unique example 
            test_raw = pd.DataFrame(test_json, index=[0])
        
        else:                             #multiple example
            test_raw = pd.DataFrame(test_json, columns = test_json[0].keys())
            
        #Initialize HealthInsurance Class
        pipeline = HealthInsurance()
        print('pipeline')
            
        #data cleaning
        data = data_cleaning(test_raw)
        print('data cleaning')
        
        #feature engineering
        data = feature_engineering(data)
        print('feature engineering')
        
        #data preparation
        data = data_preparation(data)
        print('data preparation')
        
        #prediction
        df_response = get_prediction(model, test_raw, data)
        print('prediction')
            
        return df_response
        
    
    else:
        return Response('{}', status = 200, mimetype = 'application/json')

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)
            
            
            


