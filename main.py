
# Import libraries
import streamlit as st
import pandas as pd
import plotly as py
import plotly.graph_objects as go

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# --- Header Section ---
with st.container():
    st.subheader("Hi, my name is Jonathan Dickinson :wave:")
    st.title("An aspiring data professional from California")
    st.write("I wanted to create this webpage to present the previous projects that I have worked on in the hope that you might find some of them useful or interesting.")
    st.write("[GitHub >](https://github.com/jonathjd)")

# ---What I do ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About me")
        st.write("##")
        st.write(
            """
            I am a young data professional who enjoys doing two things, analyzing data and automating processes associated with those analyses.
            Having spent 7 years in higher education, by far my favorite aspect of science was analyzing the data. I find joy in discovering
            novel insights and being able to tell a story with those data. Finally, some tasks associated with science are redundant and if you're
            not careful you can often find yourself doing repetitive tasks that can (hopefully) be automated through either a python script or 
            simply some clever thinking.

            A couple more interesting tid bits about myself:
            - I enjoy reading (Currently reading Ageless: The new science of getting older without getting old)
            - I competed in track and field for 4 years at UC Irvine (Go Eaters!)
            - I take my coffee black with 1 sugar.
            """
        )
        st.write("Feel free to share anything you find valuable here with a peer or colleague!")
    with right_column:
        st.markdown("![Alt Text](https://i.pinimg.com/originals/e4/26/70/e426702edf874b181aced1e2fa5c6cde.gif)")

# --- Projects ---
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")

image_column, text_column = st.columns((1,2))
with image_column:
    st.image("https://cdn11.bigcommerce.com/s-jyvxk5hzsq/images/stencil/500x659/products/8329/46012/8759square__99323.1604697767.jpg?c=2")
with text_column:
    st.header("College Cost Analysis")
    st.subheader("Description:")
    st.write(
        '''
        The U.S. Department of Education provides the the most reliable data on college costs, graduation, and 
        post-graduation earnings. The purpose of the College Scorecard project is to increase transparancy and awareness
        on the true cost of higher education so that students and families can make informed decisions about college.
        Personally, I believe these data are very valuable and should be widely accessible, however the highly dimensional
        nature of the dataset is not very userfriendly. My goal is to help make this dataset more accessible to those looking
        to continue their education in postsecondary education.

        If you would like to look further into the data documentation, or how these visualization were created, click the
        link to my GitHub at the top of the web page.

        These visualizations will be continually updated as the analysis progresses.
        '''
    )
st.subheader("Median Cost of Attendance Map")

#---Insert Plotly graph ---
df = pd.read_csv('https://raw.githubusercontent.com/jonathjd/webapp/main/cleaned_cost_data')
df_display = pd.read_csv('https://raw.githubusercontent.com/jonathjd/webapp/main/web_app_data.csv')

# Clean data
df = df.groupby(by='STABBR').median()


# Create dictionary with data
# This map will display median state income
data = dict(type='choropleth',
            locations = df.index,
            locationmode='USA-states',
            z=df['COSTT4_A'],
            colorscale="Reds",
            colorbar_title="USD"
            )

# configure layout
layout = dict(geo=dict(
    scope='usa',
    showlakes=True,
    lakecolor="rgb(85,173,240)")
             )

#---Display Plotly Graph--
with st.container():
    fig = go.Figure(data=[data], layout=layout)
    st.plotly_chart(fig)
    st.write('''
             The figure above is an interative map that allows you to hover over the state of interest and observe the median
             value of the average cost of attendance for each state. The The average annual total cost of attendance, including 
             tuition and fees, books and supplies, and living expenses, minus the average grant/scholarship aid, by detailed income category. 
             It is calculated for all full-time, first-time, degree/certificate-seeking undergraduates who receive Title IV aid.
            
            The median value of the average cost of attendance for every institution that primarily awards either graduate
            or bachelors degree is shown.
             ''')

#--- Display dataframe---
with st.container():
    st.subheader("Institutional Data")
    st.write(df_display)
        
