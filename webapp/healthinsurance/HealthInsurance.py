import pickle
import numpy  as np
import pandas as pd

class HealthInsurance(object):
    def __init__(self):
        #paths
        self.annual_premium_scaler = pickle.load(open('features/annual_premium_scaler.pkl', 'rb'))
        self.age_scaler =  pickle.load(open('features/age_scaler.pkl', 'rb'))
        self.vintage_scaler = pickle.load(open('features/vintage_scaler.pkl', 'rb'))
        self.region_code_encode = pickle.load(open('features/region_code_encode.pkl', 'rb'))
        self.policy_sales_channel_encode = pickle.load( open('features/policy_sales_channel_encode.pkl', 'rb'))
        self.gender_encode = pickle.load(open('features/gender_encode.pkl', 'rb'))
        
                                                                                    
    def data_cleaning(self, data):
                                                                                       #Rename columns


        data.columns = [x.lower() for x in data.columns]
        return data
                                                                                     
                                                                                     
    def feature_engineering(self, data):
        data['vehicle_age'] = data['vehicle_age'].apply(lambda x: 'less_than_1_year' if x =='< 1 Year' else
                                                                  'more_than_2_years' if x== '> 2 Years' else
                                                                  'between_1_and_2_years' )
        return data
                                                                                     
    def data_preparation(self, data):

        #annual premium
        data['annual_premium'] = self.annual_premium_scaler.transform(data[['annual_premium']].values)

        #age
        data['age'] = self.age_scaler.transform(data[['age']].values)

        #vintage
        data['vintage'] = self.vintage_scaler.transform(data[['vintage']].values)

        #vehicle age -- One Hot Encoding / Order Target Encoding / Frequency Encoding
        data = pd.get_dummies(data, prefix='vehicle_age', columns=['vehicle_age'])

        #region code -- Target Encoding / Weighted Target Encoding / Frequency Encoding
        data.loc[:,'region_code'] = data['region_code'].map(self.region_code_encode)

        #policy_sales_channel -- Target Encoding / Frequency Encoding
        data.loc[:,'policy_sales_channel'] = data['policy_sales_channel'].map(policy_sales_channel_encode)

        #gender -- Target Encoding
        data.loc[:,'gender'] = data['gender'].map(self.gender_encode)

        #features selected
        cols_selected =['vintage','annual_premium','age','region_code','vehicle_damage','policy_sales_channel','previously_insured']
        

        return data[cols_selected]
       
    def get_prediction(self, model, original_data, test_data):
        #model prediction
        pred = model.predict_proba(test_data)
        
        #join prediction into original data
        original_data['score'] = pred[:,1].tolist()
        
        return original_data.to_json(orient='records', date_format='iso')