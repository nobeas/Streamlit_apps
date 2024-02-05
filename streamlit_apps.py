import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('data1.csv')
st.write(data.head())
x=data["Week"]
y=data["Methanol"]
st.write(x)
st.write(y)
fig, ax = plt.subplots()
ax.plot(x,y)
plt.xlabel("week")
plt.ylabel("Methanol")
st.pyplot(fig)
