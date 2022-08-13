# importing libraries 
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# importing data into respective variables
jobs_data = pd.read_csv('https://raw.githubusercontent.com/ShashankGodala/Data_analyst_skill_guide/main/indeed_jobdata_cleaned.csv',usecols=['Title','Company','Location','lat','lon','Job_link','Type'])

# soft skills and their frequency
soft_skills = pd.read_csv('https://raw.githubusercontent.com/ShashankGodala/Data_analyst_skill_guide/main/soft_skills_frequency.csv')
#sorting the data according to the frequency
soft_skills_sorted = soft_skills.sort_values(by='frequency', ascending = True)

# hard skills and their frequency
hard_skills = pd.read_csv('https://raw.githubusercontent.com/ShashankGodala/Data_analyst_skill_guide/main/hard_skills_frequency.csv')
hard_skills_sorted = hard_skills.sort_values(by = 'frequency', ascending = True)

# top tools and their frequency
tools = pd.read_csv('https://raw.githubusercontent.com/ShashankGodala/Data_analyst_skill_guide/main/tools_frequency.csv')
tools_sorted = tools.sort_values(by = 'frequency', ascending = True)

# top languages and their frequency
languages = pd.read_csv('https://raw.githubusercontent.com/ShashankGodala/Data_analyst_skill_guide/main/languages_frequency.csv')
languages_sorted = languages.sort_values(by = 'frequency', ascending = True)

# setting page icon and title
st.set_page_config(page_title='Skills for data analysts',page_icon = ':tada:',layout = 'wide')


# Introduction
st.title('Hello, I am Shashank :wave:')

with st.container():
    st.markdown('### welcome to the Data Analyst skill guide')
    st.markdown('##### Increase your chances of landing a Data analyst job by developing all the hard skills and soft skills in demand.', unsafe_allow_html = True)
    st.markdown('##### This data is from 2500 Data analyst job postings accross Australia.', unsafe_allow_html = True)
    st.markdown('Last updated 9 AUG 2022')
    
st.write('---')

# skills dashboard title
st.markdown("<h3 style='text-align: center;'>Top skills and their frequency of appearance in job descriptions</h3>", unsafe_allow_html=True)

# building soft skills bar chart
soft_skills_fig = px.bar(soft_skills_sorted,x='frequency',y='name', text_auto=True,color_discrete_sequence =['#add8e6']*len(soft_skills_sorted))
soft_skills_traces = soft_skills_fig.update_traces(textfont_size=16)
soft_skills_chart = soft_skills_traces.update_layout({
                                        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                                        },
                                        yaxis_title='',xaxis_visible= False, 
                                        xaxis_showticklabels =False,
                                        yaxis = dict(tickfont = dict(size=20)))

# building hard skills bar chart
hard_skills_fig = px.bar(hard_skills_sorted,x='frequency',y='name',text_auto=True,color_discrete_sequence =['#add8e6']*len(hard_skills_sorted))
hard_skills_traces = hard_skills_fig.update_traces(textfont_size=16)
hard_skills_chart = hard_skills_traces.update_layout({
                                        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                                        },
                                        yaxis_title='',xaxis_visible= False, 
                                        xaxis_showticklabels =False,
                                        yaxis = dict(tickfont = dict(size=20)))

# building top tools bar chart
tools_fig = px.bar(tools_sorted,x='frequency',y='name',text_auto=True,color_discrete_sequence =['#add8e6']*len(tools_sorted))
tools_traces = tools_fig.update_traces(textfont_size=16)
tools_chart = tools_traces.update_layout({
                                        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                                        },
                                        yaxis_title='',xaxis_visible= False, 
                                        xaxis_showticklabels =False,
                                        yaxis = dict(tickfont = dict(size=20)))

# building languages bar chart
languages_fig = px.bar(languages_sorted,x='frequency',y='name',text_auto=True,color_discrete_sequence =['#add8e6']*len(hard_skills_sorted))
languages_traces = languages_fig.update_traces(textfont_size=16)
languages_chart = languages_traces.update_layout({
                                        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                                        },
                                        yaxis_title='',xaxis_visible= False, 
                                        xaxis_showticklabels =False,
                                        yaxis = dict(tickfont = dict(size=20)))
                                        

# arranging all the charts plotted above in a dashboard layout
with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("<h4 style='text-align: center;'>Soft skills</h4>", unsafe_allow_html=True)
        st.plotly_chart(soft_skills_chart)
        st.write('some tips to develop communication and leadership skills,')
        st.write('Step Outside Your Comfort Zone, Self-Reflect, Actively Listen, Improve Writing Skills.')
        st.write('Take on a Leadership Role, Communicate Often, Work on Critical-Thinking Skills.')
        st.markdown("<h4 style='text-align: center;'>Tools</h4>", unsafe_allow_html=True)
        st.plotly_chart(tools_chart) 
        st.write('Amazing complete courses on both BI tools are available from Pawan Lalwani, Edureka, and simplilearn.')
        st.write('Visit Leila Gharani and Chandoo on YouTube for advanced Excel.')
        st.write('An excellent YouTube channel to learn powerpoint tips and tricks is Kevin Stratvert.')
    with right_column:
        st.markdown("<h4 style='text-align: center;'>Hard skills</h4>", unsafe_allow_html=True)
        st.plotly_chart(hard_skills_chart)
        st.write('Although analytical, reporting, and visualisation skills can be acquired, they can only be enhanced by continuing to work on projects that involve the aforementioned.')
        st.write('Use less text and more visuals in your presentation, be passionate and engaging, maintain eye contact, and invite questions at the conclusion as some advice for practising effective presentations.')
        st.markdown("<h4 style='text-align: center;'>Programming languages</h4>", unsafe_allow_html=True)
        st.plotly_chart(languages_chart)
        st.write('For absolute beginners I recommend SQL Mastery course from CodewithMosh.com (keep an eye for sale)')
        st.write('stratascratch, Hackerrank and w3 schools are great websites to practice SQL problems.')
        st.write('freecodecamp.org has a free video on youtube on python for data analytics.')
st.write('---')
st.write('Follow [Alex freberg](https://www.youtube.com/c/AlexTheAnalyst), [Shashank Kalanithi](https://www.youtube.com/c/ShashankKalanithiData) and [Luke Barousse](https://www.youtube.com/c/LukeBarousse) on youtube.')
st.write('Read or listen to "story telling with data" book by Cole nussbaumer knaflic.')


# jobs location map
with st.container():
    st.write('---')
    col1,col2,col3 = st.columns((1,2,1))
    with col2:
        st.markdown("<h3 style='text-align: center;'>Where are the jobs loacated</h3>", unsafe_allow_html=True)
        st.map(data=jobs_data, use_container_width=False)
        

st.write('')
st.markdown('#### Built by Shashank Godala')
st.write('[Website](https://shashankgodala.me/)')
st.write('[Github](https://github.com/ShashankGodala)')
st.write('[Linkedin](https://www.linkedin.com/in/shashank-godala/)')
st.write('[Tableau Public](https://public.tableau.com/app/profile/shashank4870)')




