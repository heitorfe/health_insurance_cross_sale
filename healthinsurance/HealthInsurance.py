class HealthInsurance():
    def __init__(self):
        #paths
        self.annual_premium_scaler = pickle.load(ss, open('/src/features/annual_premium_scaler.pkl', 'rb'))
        self.age_scaler =  pickle.load(mms_age, open('/src/features/age_scaler.pkl', 'rb'))
        self.vintage_scaler = pickle.load(mms_vintage, open('/src/features/vintage_scaler.pkl', 'rb'))
        self.region_code_encode = pickle.load(target_encode_region_code, open('/src/features/region_code_encode.pkl', 'rb'))
        self.policy_sales_channel_encode = pickle.load(fe_policy_sales_channel, open('/src/features/policy_sales_channel_encode.pkl', 'rb'))
        self.gender_encode = pickle.load(target_encode_gender, open('/src/features/gender_encode.pkl', 'rb'))
        
                                                                                    
    def data_cleaning(data):
                                                                                     #Rename columns
        old_cols = ['id', 'Gender', 'Age', 'DrivingLicense', 'RegionCode','PreviouslyInsured', 'Vehicle_Age', 'VehicleDamage', 'AnnualPremium','PolicySalesChannel', 'Vintage', 'Response']
        snakecase = lambda x: inflection.underscore(x)

        new_cols = list(map(snakecase, old_cols))
        data.columns = new_cols

        #changing types

        data['vehicle_damage'] = data['vehicle_damage'].apply(lambda x: 1 if x == 'Yes' else 0)
        data['policy_sales_channel'] = data['policy_sales_channel'].astype(int)
        data['annual_premium'] = data['annual_premium'].astype(int)
        data['region_code'] = data['region_code'].astype(int)
        data['vehicle_damage'] = data['vehicle_damage'].astype(int)
        return data
                                                                                     
                                                                                     
    def feature_engineering(data):
        data['vehicle_age'] = data['vehicle_age'].apply(lambda x: 'less_than_1_year' if x =='< 1 Year' else
                                                                  'more_than_2_years' if x== '> 2 Years' else
                                                                  'between_1_and_2_years' )
        return data
                                                                                     
    def data_preparation(data):
        X = data.drop('response', axis=1)
        y = data['response'].copy()
        x_train, x_validation, y_train, y_validation = ms.train_test_split(X, y, test_size=0.2)
        data = pd.concat([x_train, y_train], axis=1)

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
        pred = mode.predict_proba(test_data)
        
        #join prediction into original data
        original_data['score'] = pred
        
        return original_data.to_json(orient='records',data_format='iso')