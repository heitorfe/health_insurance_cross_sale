# health_insurance_cross_sale
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

#3. Solution Development

## 3.1. Data Description and Feature Engineering

Checking the shape of the datase, nulls and filling the nulls values. 

## 3.2. Exploratory Data Analysis

Trying to get insights by data analysis with graphs, histograms, plotlines and barplot. Also checking the correlation of the features and testing hypotesis.

## 3.3. Data Preparation

Using normalization, rescaling and encoding to prepare the data to the Machine Learning model.

## 3.4. Feature Selection

Using the Boruta algorithm to select the most important features to get the best Machine Learning performance.

## 3.5. Machine Learning Model

Training different Machine Learning models and comparing errors. The choosen method was the XGBoost Regressor because of the speed and accuracy of the model. 

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

## 3.7. Deploy and Google Sheets API

Deploy in the Heroku Cloud and configurating Flask API request by a Google Sheets.

# 4. Results and Conclusion

## 4.1. Main Hypotesis 

The main hypotesis confirmed in the EDA step:

### H1. Stores with larger assortments should sell more.
False. Stores with larger assortments should sell less.

![Sales sum by assortment](https://user-images.githubusercontent.com/77629603/155387884-6c33a7be-82e5-4c57-8648-28bf0f217aae.png)


### H2. Stores with closer competitors should sell less.
False. Stores with closer competitors sell more.

![Sales by competition distance (bin = 0-1000)](https://user-images.githubusercontent.com/77629603/155381618-a59fdbc2-e4af-45dd-8458-3159ddc01eac.png)


### H3. Stores with longer active promotions should sell more.
False. We can see that sales increase in the standard promos and decreases in the extended promos.
(Negative promo duration is regular promo, positive promo duration is extanded promo)

![Regplot representing sales by promo duration](https://user-images.githubusercontent.com/77629603/155382386-6c6462ab-0820-4dae-a1ca-51ea9a0aad33.png)

## 4.2.Conclusion
The model generates a dataframe with the prediction of each store and the respectives worst and best scenarios. 
The CFO now can know the budget available to renovate the stores, with 90% accuracy.

![First 15 rows of the prediction dataset.](https://user-images.githubusercontent.com/77629603/155379600-1321b4d9-6db2-4941-80cf-96012798fe00.png)

The user can get the results by Telegram. Here is some [demonstration](https://www.linkedin.com/posts/heitor-felix_datascience-datadriven-business-activity-6902361790051606528-2Fjo)!

## 4.3. Machine Learning Performance

Here is the demonstration of the model prediction vs real sales by date

![Seaborn lineplot](https://user-images.githubusercontent.com/77629603/155380531-060fbf29-4f30-486f-b875-4d3b0ead5178.png)


# 5. Next Steps

*Collecting feedback of the users and improve the usability if necessary
*Improve the performance in the next CRISP cycle

# 6. References

The data is avaliable in this [page](https://www.kaggle.com/c/rossmann-store-sales)
