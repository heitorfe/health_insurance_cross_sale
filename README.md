# Health Insurance Cross Sell
![image](https://user-images.githubusercontent.com/77629603/158879224-d703e986-a8e4-4229-a384-2252c879f8ba.png)

# 1. Context

This project is based in a Kaggle Challenge wich simulates a business problem. An insurance company wants to start a cross-sell strategy. They want to sell car insurance to people who already is their client. They made a poll to investigate possible customers.

# 2. Challenge

Find out what type of customer is the more propense to buy the product and give the list to the business team. They have a budget to contact 20.000 people, we want to get the biggest number of clients 

## 2.1. Problem

The business team wants to get the highest precision possible to get new clients with the investment.

## 2.2. Causes

-There are nothing to order by propensity to buy

-Current method to call clients is randomly

-There is a specif budget to prospect clients

## 2.3. Solution

-Using Machine Learning model get propensity score of each client

-Propensity score will be returned in Google Sheets API

# 3. Solution Development

## 3.1. Data Description and Feature Engineering

Checking the shape of the datase, nulls and filling the nulls values. 

## 3.2. Exploratory Data Analysis

Trying to get insights by data analysis with graphs, histograms, plotlines and barplot. Also checking the correlation of the features and testing hypotesis.

## 3.3. Data Preparation

Using normalization, rescaling and encoding to prepare the data to the Machine Learning model.

## 3.4. Feature Selection

Using the Extra Trees Classifier to select the most important features to get the best Machine Learning performance.

## 3.5. Machine Learning Model

Training different Machine Learning models and comparing errors. The choosen method was the XGBoost Regressor because of the good speed and accuracy of the model. 

![image](https://user-images.githubusercontent.com/77629603/159000872-cfde09d8-137a-4f50-a43d-8d6e32e0f25a.png)


## 3.6. Error Translation

Giving business meaning to the project, translating accuracy in values to the business.

The metrics was:
*Precision at k*
How much the predict is correct in the top k of the list. 

*Recall at k*
How much response = 1 the model predicts correctly in the top k of the total responses = 1 of the list

I choose k = 20.000 due to the problem context. The result of the model chosen was:

![image](https://user-images.githubusercontent.com/77629603/159001525-67067def-b65c-44c1-b387-3fb3a03a38f5.png)

Translating into business languege we can compare the costs of prospecting randomly vs based in the model.

![image](https://user-images.githubusercontent.com/77629603/159006315-6457fce6-802d-4ab4-87df-bea41f1de329.png)

We can get 90% of the interested contacting 30% of the total base. In terms of costs, to get all these 90% the company would spent 66% less.

### 3.6.1 Cumulative Gain Curve

![image](https://user-images.githubusercontent.com/77629603/159339821-a726205f-2221-4296-b5bb-5c730ab1ba47.png)


### 3.6.2 Lift Curve

![image](https://user-images.githubusercontent.com/77629603/159339775-2c41edff-4a35-4ba0-b502-d1b79a5c596a.png)

### 3.6.3 ROC Curve

![image](https://user-images.githubusercontent.com/77629603/159339995-ce36f38d-1301-435d-bfd1-66e77029be4b.png)


## 3.7. Deploy and Google Sheets API

Deploy in the Heroku Cloud and configurating Flask API request by a Google Sheets. The business team can easily use the trained model with new data to get the propensity score of each contact.

# 4. Results and Conclusion

## 4.1. Main Concluions of Exploratory Data Analisys 

The main conclusios found in the EDA was:

### C1. Age

![image](https://user-images.githubusercontent.com/77629603/159340818-64537512-d512-4c02-9158-928b263b1621.png)
![image](https://user-images.githubusercontent.com/77629603/159340839-43426bfd-0d92-4be8-85a2-8ecb617ed5ac.png)

The volume of negative resposes is much larger than the positive ones. Looking into the postive responses, the target is in the middle age (about 40-50 years old). Looking into the negative responses, the conclusion is that the young people seems to be less interested in the product.

### C2. Annual premium.

Definition: The amount customer needs to pay as premium in the year

![image](https://user-images.githubusercontent.com/77629603/159341808-cc987722-f6a7-4ef9-ae89-4ead0dbf417e.png)

The distribution is almost the same, the only difference is the volume of the data. Conclusion: This variable is not helpful alone.


### C3. Policy sales channel

Definition: Anonymized code for the channel of outreaching to the customer ie. Different agents, over mail, over phone, in person, etc.

![image](https://user-images.githubusercontent.com/77629603/159342410-aa0178cf-63bd-4b50-9074-4a68f66c888c.png)

The most part of the distribution is similar, but it would be interested to check regions with differences between responses 0 and 1.

![image](https://user-images.githubusercontent.com/77629603/159343253-eb5287bf-c1f7-4798-ac1e-d05a65e43784.png)
Table with the region with more responses ordered by the percentage of positive response.

## 4.2.Conclusion
The model generates a the propensity score to each new contact in the base. The business can easily use the application in Google Sheets to get the more propensity contacts to call. 
The precision at top 20.000 is about 33,5%.

The user can get the propensity score of new contact in the database by Google Sheets. Here is some [demonstration](https://drive.google.com/file/d/1Y79eRMHXxkv_mNFX9yVo1DeTa3Y1R9_l/view?usp=sharing)!

# 5. Next Steps

*Collecting feedback of the users and improve the usability if necessary
*Improve the performance in the next CRISP cycle

# 6. References

The data is avaliable in this [page](https://www.kaggle.com/anmolkumar/health-insurance-cross-sell-prediction)
