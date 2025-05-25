import streamlit as st
from scripts.fighters import get_fighter_options, get_fighter_stats, get_fight_prediction, get_weight_classes

st.html("<h1 style='text-align: center; font-size: 40px; border-bottom: solid 1px lightgrey;'> UFC Predictions</h1>")

st.html("<h3 style='text-align: center; font-size: 22px; '> Please select two fighters from the drop down to compare the performance and predict the winner</h3>")

weight_class = st.selectbox('Select Weight Class', get_weight_classes())

col1, col2 = st.columns(2)
fighters_options = get_fighter_options(weight_class)
fighters = list(fighters_options.keys())

with col1:
    fighter1 = st.selectbox("Fighter 1:", fighters )
    fighter1_stats = get_fighter_stats(fighters_options[fighter1])
    container1 = st.container(border=True)
    container1.subheader('Fighter 1 Stats', divider='gray')
    container1.write('Name : ' + fighter1_stats['N_Name'])
    container1.write('DOB : ' + fighter1_stats['DOB'])
    container1.write('Weight : '+ fighter1_stats['Weight'])
    container1.write('Height : ' + fighter1_stats['Height'])
    container1.write('Reach : ' + fighter1_stats['Reach'])
    container1.write('Stance : ' + fighter1_stats['STANCE'])
    container1.write('SLpM : ' + str(fighter1_stats['SLpM']))
    container1.write('Str. Acc. : ' + fighter1_stats['Str. Acc.'])
    container1.write('SApM : ' + str(fighter1_stats['SApM']))
    container1.write('Str. Def : ' + fighter1_stats['Str. Def'])
    container1.write('TD Avg. : ' + str(fighter1_stats['TD Avg.']))
    container1.write('TD Acc. : ' + fighter1_stats['TD Acc.'])
    container1.write('TD Def. : ' + fighter1_stats['TD Def.'])
    container1.write('Sub. Avg. : ' + str(fighter1_stats['Sub. Avg.']))

with col2:
    fighter2 = st.selectbox("Fighter 2:",fighters)
    fighter2_stats = get_fighter_stats(fighters_options[fighter2])
    container2 = st.container(border=True)
    container2.subheader('Fighter 2 Stats', divider='gray')
    container2.write('Name : ' + fighter2_stats['N_Name'])
    container2.write('DOB : ' + fighter2_stats['DOB'])
    container2.write('Weight : ' + fighter2_stats['Weight'])
    container2.write('Height : ' + fighter2_stats['Height'])
    container2.write('Reach : ' + fighter2_stats['Reach'])
    container2.write('Stance : ' + fighter2_stats['STANCE'])
    container2.write('SLpM : ' + str(fighter2_stats['SLpM']))
    container2.write('Str. Acc. : ' + fighter2_stats['Str. Acc.'])
    container2.write('SApM : ' + str(fighter2_stats['SApM']))
    container2.write('Str. Def : ' + fighter2_stats['Str. Def'])
    container2.write('TD Avg. : ' + str(fighter2_stats['TD Avg.']))
    container2.write('TD Acc. : ' + fighter2_stats['TD Acc.'])
    container2.write('TD Def. : ' + fighter2_stats['TD Def.'])
    container2.write('Sub. Avg. : ' + str(fighter2_stats['Sub. Avg.']))

if st.button("Predict", use_container_width=True, icon=":material/sports_mma:", type='primary'):
    result = get_fight_prediction(fighters_options[fighter1], fighters_options[fighter2], weight_class)
    st.html("<h2 style='text-align: center; font-size: 40px; border-bottom: solid 1px lightgrey;'> Winner</h2>")
    st.html("<h3 style='text-align: center; font-size: 22px; width: 100%; '> The winner between the two selected fighters will be: </h3>")
    st.html("<h2 style='text-align: center; font-size: 40px;'>"+result+"</h2>")

