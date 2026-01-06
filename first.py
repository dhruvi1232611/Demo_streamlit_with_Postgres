import streamlit as slt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df=pd.read_csv("data/Iris.csv")
slt.title("Iris Flower Classification")
slt.write(df.head())

x= df.loc[:,df.columns!="Species"]
y= df["Species"]

slt.write(x.head())
slt.write(y.head())

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=42)
model= LogisticRegression()
model.fit(x_train,y_train)

y_pred= model.predict(x_test)
slt.write(y_pred)

acc=accuracy_score(y_test,y_pred)
slt.write("Accuracy-score",acc)
