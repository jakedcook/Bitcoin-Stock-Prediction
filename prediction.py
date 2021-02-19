#here is our prediction model to connect to our app.py
import os 
import cgi, cgitb
#import dependencies 
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import mpld3 
plt.style.use('bmh')

#create data frame 
#df = pd.read_csv('Resources/BTC-USD.csv')

#get only the adj. close price for this model 
#df = df[['Adj Close']]

#create variable for the amount of days you would like to predict the future close price
#for this model we will do the next 30 days 

def get_number_of_days(future_days):
    future_predict = int(future_days) 

    #create data frame 
    df = pd.read_csv('Resources/BTC-USD.csv')

    #get only the adj. close price for this model 
    df = df[['Adj Close']]

    #create new column with shifts (just moving everything up 30 days)
    df['Prediction'] = df[['Adj Close']].shift(-future_predict)

    #create data set as a numpy array 
    independent_data = np.array(df.drop(['Prediction'], 1))

    #remove the last 'future_predict' rows 
    independent_data = independent_data[:-future_predict]


    #create data set as a numpy array 
    dependent_data = np.array(df['Prediction'])

    #remove the last 'future_predict' rows 
    dependent_data = dependent_data[:-future_predict]
    #print(dependent_data)

    #split data into 80% data and 20% testing
    x_train, x_test, y_train, y_test = train_test_split(independent_data, dependent_data, test_size = 0.09)

    #create and train linear regression model 
    lr = LinearRegression()
    #train the model 
    lr.fit(x_train, y_train)

    #testing the linear regresssion model now 
    lr_accuracy = lr.score(x_test, y_test)
    lr_train_accuracy = lr.score(x_train, y_train)
    print("linear regression test accuracy: ", lr_accuracy)
    print("linear regression train accuracy: ", lr_train_accuracy)

    #looks like linear regression model gives us a better accuracy 
    future = np.array(df.drop(['Prediction'], 1))[-future_predict:]
    #print(future)

    #print the linear regression predicitons for the next 'future_predict' days 
    lr_prediction = lr.predict(future)
    #print(lr_prediction)

    #create variables to plot the data via html
    #original_data = df['Adj Close']
    #print(original_data)

    #create a new data frame with the predictions for the user inputed amount showing original and predicted 
    prediction_data = df[independent_data.shape[0]:]
    prediction_data['Prediction'] = lr_prediction
    
    html = prediction_data.to_html()
    #print(html) 
    html = prediction_data.to_html()

    text_file = open('templates/table.html', 'w')
    text_file.write(html)
    text_file.close()

    fig = plt.figure(figsize=(16,8))
    plt.title('Bitcoin Linear Regression Model')
    plt.xlabel('Days')
    plt.ylabel('Close Price USD $')
    plt.plot(df['Adj Close'])
    plt.plot(prediction_data['Prediction'])
    plt.legend(['Original', 'Predictions'])

    html_str = mpld3.fig_to_html(fig)
    Html_file= open('templates/table2.html','w')
    Html_file.write(html_str)
    Html_file.close()

    print(prediction_data)
    return(prediction_data)
    
