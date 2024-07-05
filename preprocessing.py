# Replace xxxx with downloaded .csv file from kaggle set https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents
#My data set was from Febuary 2016 to December 2021
import pandas as pd
df = pd.read_csv('xxxx.csv',header=None)
df


#check for null
df.isnull().any()

df.tail(-1)

df = df.head(1000000)

df
