import streamlit as st

st.write("UFC Predictions")

st.write('Here we will add the code for the front-end')

fighters = ['fighter1', 'fighter2', 'fighter3', 'fighter4', 'fighter5']

fighter1 = st.selectbox("fighter 1:", fighters )
fighter2 = st.selectbox("fighter 2:",fighters)