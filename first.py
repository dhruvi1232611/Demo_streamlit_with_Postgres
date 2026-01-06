import streamlit as slt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df=pd.read_csv("data/Iris.csv")
slt.title("Iris Flower Classification")
slt.write(df.head())

x= df.drop(columns=df["Species"])
y= df["Species"]

x_train , x_test , y_train , y_test = train_test_split(test_size=0.2,randome_state=42)
model= LogisticRegression()
model.fit(x_train,y_train)

y_pred= model.predict(y_test)
slt.write(y_pred)

acc=accuracy_score(x_test,y_pred)
slt.write("Accuracy-score",acc)
