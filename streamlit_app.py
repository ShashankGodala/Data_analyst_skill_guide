import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
jobs_data = pd.read_csv('https://raw.githubusercontent.com/ShashankGodala/Data_analyst_skill_guide/main/indeed_jobdata_cleaned.csv',usecols=['Title','Company','Location','lat','lon','Job_link','Type'])
soft_skills = pd.read_csv('https://raw.githubusercontent.com/ShashankGodala/Data_analyst_skill_guide/main/soft_skills_frequency.csv')
soft_skills_sorted = soft_skills.sort_values(by='frequency', ascending = True)
hard_skills = pd.read_csv('https://raw.githubusercontent.com/ShashankGodala/Data_analyst_skill_guide/main/hard_skills_frequency.csv')
hard_skills_sorted = hard_skills.sort_values(by = 'frequency', ascending = True)
tools = pd.read_csv('https://raw.githubusercontent.com/ShashankGodala/Data_analyst_skill_guide/main/tools_frequency.csv')
tools_sorted = tools.sort_values(by = 'frequency', ascending = True)
languages = pd.read_csv('https://raw.githubusercontent.com/ShashankGodala/Data_analyst_skill_guide/main/languages_frequency.csv')
languages_sorted = languages.sort_values(by = 'frequency', ascending = True)


st.set_page_config(page_title='Skills for data analysts',page_icon = ':tada:',layout = 'wide')
st.title('Hello, I am Shashank :wave:')


with st.container():
    st.markdown('### welcome to the Data Analyst skill guide')
    st.markdown('##### Increase your chances of landing a Data analyst job by developing all the hard skills and soft skills in demand.', unsafe_allow_html = True)
    st.markdown('##### This data is from 2500 Data analyst job postings accross Australia.', unsafe_allow_html = True)
    st.markdown('Last updated 9 AUG 2022')
    
st.write('---')

st.markdown("<h3 style='text-align: center;'>Top skills and their frequency of appearance in job descriptions</h3>", unsafe_allow_html=True)

# building soft skills bar chart
soft_skills_fig = px.bar(soft_skills_sorted,x='frequency',y='name',color_discrete_sequence =['#808080']*len(soft_skills_sorted))
soft_skills_chart = soft_skills_fig.update_layout({
                                        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                                        },
                                        yaxis_title='',xaxis_visible= False, 
                                        xaxis_showticklabels =False,
                                        yaxis = dict(tickfont = dict(size=20)))

# building hard skills bar chart
hard_skills_fig = px.bar(hard_skills_sorted,x='frequency',y='name',color_discrete_sequence =['#808080']*len(hard_skills_sorted))
hard_skills_chart = hard_skills_fig.update_layout({
                                        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                                        },
                                        yaxis_title='',xaxis_visible= False, 
                                        xaxis_showticklabels =False,
                                        yaxis = dict(tickfont = dict(size=20)))

# building top tools bar chart
tools_fig = px.bar(tools_sorted,x='frequency',y='name',color_discrete_sequence =['#808080']*len(tools_sorted))
tools_chart = tools_fig.update_layout({
                                        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                                        },
                                        yaxis_title='',xaxis_visible= False, 
                                        xaxis_showticklabels =False,
                                        yaxis = dict(tickfont = dict(size=20)))

# building languages bar chart
languages_fig = px.bar(languages_sorted,x='frequency',y='name',color_discrete_sequence =['#808080']*len(hard_skills_sorted))
languages_chart = languages_fig.update_layout({
                                        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                                        },
                                        yaxis_title='',xaxis_visible= False, 
                                        xaxis_showticklabels =False,
                                        yaxis = dict(tickfont = dict(size=20)))
                                        

with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("<h4 style='text-align: center;'>Soft skills</h4>", unsafe_allow_html=True)
        st.plotly_chart(soft_skills_chart)
        st.markdown("<h4 style='text-align: center;'>Tools</h4>", unsafe_allow_html=True)
        st.plotly_chart(tools_chart)
    with right_column:
        st.markdown("<h4 style='text-align: center;'>Hard skills</h4>", unsafe_allow_html=True)
        st.plotly_chart(hard_skills_chart)
        st.markdown("<h4 style='text-align: center;'>Programming languages</h4>", unsafe_allow_html=True)
        st.plotly_chart(languages_chart)


with st.container():
    st.write('---')
    col1,col2,col3 = st.columns((1,2,1))
    with col2:
        st.markdown("<h3 style='text-align: center;'>Where are the jobs loacated</h3>", unsafe_allow_html=True)
        st.map(data=jobs_data, use_container_width=False)

quick_search_data = jobs_data[['Title','Company','Location','Type','Job_link']]

with st.container():
    st.write('---')
    st.markdown("<h2 style='text-align: center;'>Quick search</h2>", unsafe_allow_html=True)
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        Company = st.multiselect('Select Company',options=quick_search_data['Company'].drop_duplicates(), default=None)
    with col2:
        Location = st.multiselect('Select Location',options=quick_search_data['Location'].drop_duplicates(), default=None)
    with col3:
        Type = st.multiselect('Select job type',options=quick_search_data['Type'].drop_duplicates(), default=None)

if len(Company) > 0:
    data = quick_search_data[quick_search_data['Company'].isin(Company)]
elif len(Location) > 0:
    data = quick_search_data[quick_search_data['Location'].isin(Location)]
elif len(Type) > 0:
    data = quick_search_data[quick_search_data['Type'].isin(Type)]
else:
    data = quick_search_data

st.dataframe(data= data, height = 500)



