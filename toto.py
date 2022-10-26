import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib as mp
import matplotlib.pyplot as plt

student_mat = pd.read_csv('./student_mat.csv')
df = pd.DataFrame(data = student_mat)

st.write('Violonplot la consommation dalcool au travail par rapport à la santé.')
fig = plt.figure(figsize=(10, 4))
sb.violinplot(data=df, x="Dalc", y="health")
st.pyplot(fig)

st.write('Violonplot la consommation dalcool le Weekend par rapport à la santé.')
fig = plt.figure(figsize=(10, 4))
sb.violinplot(data=df, x="Walc", y="health")
st.pyplot(fig)

st.write('Histogramme la consommation dalcool le Weekend par rapport à la santé.')
fig = plt.figure(figsize=(10, 4))
sb.histplot(data=df, x="Walc", y="health", hue="health",multiple="dodge")
st.pyplot(fig)

st.write('boite à moustache la consommation dalcool au travail par rapport à la relation amoureuse ou non.')
fig = plt.figure(figsize=(10, 4))
sb.boxplot(data=df, x="romantic" , y="Dalc" )
st.pyplot(fig)

cond = df
dalc = st.selectbox(
    'Taux de consommation dalcool au travail par etudiant',
    ("", 0, 1, 2, 3, 4, 5)
)
if(dalc != ""):
    cond = df[df['Dalc'] <= dalc]

cond = cond.describe()

st.dataframe(data=cond, use_container_width=True)