
# Import libraries
import streamlit as st
import pandas as pd
import plotly as py
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Jon's Portfolio", page_icon=":tada:", layout="wide")


##################################### Header Section *******************************************************************
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
            - I enjoy reading (Currently reading Jobs (Steve Jobs' documentary))
            - I competed in track and field for 4 years at UC Irvine (Go Eaters!)
            - I take my coffee black with 1 sugar.
            """
        )
        st.write("Feel free to share anything you find valuable here with a peer or colleague!")
    with right_column:
        st.markdown("![Alt Text](https://i.pinimg.com/originals/e4/26/70/e426702edf874b181aced1e2fa5c6cde.gif)")


########################################### Projects ########################################################################
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")

    # --- Drop down to hide projects ---
    with st.expander("College Cost Analysis"):

        image_column, text_column = st.columns((1,2))
        with image_column:
            st.image("https://cdn11.bigcommerce.com/s-jyvxk5hzsq/images/stencil/500x659/products/8329/46012/8759square__99323.1604697767.jpg?c=2")
        with text_column:
            st.header("College Cost Analysis")

############################################## College Cost Project q#############################################################

            st.subheader("Description:")
            st.write(
            '''
            The U.S. Department of Education provides the most reliable data on college costs, graduation, and 
            post-graduation earnings. The purpose of the College Scorecard project is to increase transparancy and awareness
            on the true cost of higher education so that students and families can make informed decisions about college.
            Personally, I believe these data are very valuable and should be widely accessible, however the highly dimensional
            nature of the dataset is not very user friendly. My goal is to help make this dataset more accessible to those looking
            to continue their education in postsecondary education.

            '''
            )

        st.write("---")

# ------------------------------------- Quick insights to project -------------------------------------------------------------
        st.header("Quick insights")
        st.write(
        '''
        - The median cost of attendance for one year at a **junior college**  in the US is **$14000** USD.
        - The median cost of attendance for one year at a **primarily undergraduate instiution** in the is **$25000** USD.
        - The median cost of attendance for one year at an institution that **primarily awards graduate degrees** is **$29000** USD.
        - On average, a first year Title IV student will spend **24000 USD** more per year in total costs (Books, tuition, etc) to go to a private institution that primarily award graduate degrees (Such as Universtiy of Southern California) that a public institution that primarily awards bachelors degrees (such as Cental Washington University)
        - Just under **half** of the schools in the U.S. that have an annual cost of attendance between **20000** and **25000** USD are public schools.
        '''
        )
        st.subheader("Key Takeaways")
        st.write('''
        To minimze the cost of attending a 4-year institution in the U.S., attend a public university that primarily awards Bachelors
        degrees.

        This analysis did not factor in future earnings, for those data checkout Georgetown Universities interactive web tool. 
        ''')
        st.write("[Georgetown Interactive Web Tool>](https://cew.georgetown.edu/cew-reports/college-rankings/)")
        st.write("---")

        # ------------------------------------- Key Visualizations -------------------------------------------------------------
        # Insert dataframes
        df = pd.read_csv('https://raw.githubusercontent.com/jonathjd/webapp/main/state_df.csv', index_col='STABBR')
        df_display = pd.read_csv('https://raw.githubusercontent.com/jonathjd/Education-Project/main/data/processed/web_app_data.csv')
        
        # Aggregate visualization subheader
        with st.container():
            st.subheader("Aggregate Visualizations")
            st.write('''
            First, we will look at some aggregate visualizations of the cost of attending post-secondary school in the U.S.

            A quick note about this metric- The cost of attendance incorporates the annual average cost of tuition, fees, books, supplies, and living expenses for a full time, first-time, degree-seeking undergraduate who
            recieves title IV aid.
            ''')

            st.write("---")

        # create columns for plotly histogram
        ed_left_column1, ed_right_column1 = st.columns((2,2))

################################### Plotly  Histogram ############################################################
        with ed_left_column1:
            # insert plotly histogram
            fig = px.histogram(df_display, x="Cost of Attendance",
                labels ={
                "count": "Number of Universities"
            },
            template="simple_white" 
            )
            
            st.plotly_chart(fig, use_container_width=True)

################################### Histogram Description ############################################################
        with ed_right_column1:
            # Header
            st.subheader("Histogram of the U.S. annual cost of attendance")

            st.write('''
            As we can see from the histogram to the left, this dataset is positively skewed to the right. What this means is that
            there are more universities that have an annual cost of attendance that is **higher** than the national average. As we will
            see in a bit, many of the universities on the right side of the graph (the more expensive universities) are either private,
            or primarily award **graduate** degrees.
            ''')

            st.markdown("Next, let's see where these expensive universities are primarily located using a US map.")

################################################ Divisor ########################################################
        with st.container():
            st.write("---")
        
######################################## Plotly Chloropleth map ################################################
        # Define columns
        ed_left_column2, ed_right_column2 = st.columns((2,2))

        with ed_right_column2:
            # Chloropleth map data
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
            fig = go.Figure(data=[data], layout=layout)
            st.plotly_chart(fig, use_container_width=True)

######################################## Chloropleth map description ###############################################
        with ed_left_column2:
            # Chloropleth map header
            st.subheader("Median Cost of Attendance Map")
            st.write('''
                The figure to the right is an interative map that allows you to hover over the state of interest and observe the median
                value of the average cost of attendance for each state. We are using the **median** and not the **average** because the data
                is positively skewed (to the right). The median will give us a more robust estimate of the central value.
                ''')

################################################ Divisor ########################################################
        with st.container():
            st.write("---")
        
############################################ Control box plot ###################################################        
        ed_left_column3, ed_right_column3 = st.columns((2,2))
        
        with ed_left_column3:

            # Display control bar plot
            st.image('https://github.com/jonathjd/Education-Project/blob/main/reports/figures/control_barplot.png?raw=true')
    
        with ed_right_column3:

            # Subheader
            st.subheader("Private vs. Public Barplot")

            # Description
            st.write('''
            The following barplot shows the cost of attendance between 3 different types of institutions:
            1. Public schools that mainly award **bachelors** degrees.
                - An example of this would be Central Washington University. The majority of the degrees conferred each quarter are undergraduate degrees, as there are few graduate programs.
            2. Private non-profit schools that mainly award **graduate** degrees.
                - An example would be the University of Southern California.
            3. Private for-profit schools that primarily award graduate degrees.
            ''')
            st.write('##')
            st.write("We can see that private non-profit schools are clearly more expensive, on average, but if we want to take a deeper look we can use a **swarm plot**.")


################################################ Divisor ########################################################
        with st.container():
            st.write("---")


################################################ Swarm Plot #######################################################
        # Make columns
        ed_left_column4, ed_right_column4 = st.columns((2,2))

        with ed_right_column4:

            # swarmplot image
            st.image('https://github.com/jonathjd/Education-Project/blob/main/reports/figures/swarm_plot.png?raw=true')

        with ed_left_column4:

            # header
            st.subheader("Public vs. Private non-profit vs. Private for-profit")

            # description
            st.write('''
            A swarm plot allows us to get a better idea of the distribution of points that are contributing to the average.

            - The most expensive **public** university seems to be about as expensive as a private university in the 50th percentile (~45,000/yr).
            - Theres more variance in the cost of attending a **private** university.
            - There is an absolute **higher** number of private non-profit universities than both public and private for-profit universities.
            ''')
            st.write('##')
            st.write("We can overlay the swarm plot onto a box and whisker plot to see minimum, lower quartile, median, upper quartile, and maximum.")
        
################################################ Divisor ########################################################
        with st.container():
            st.write("---")

########################################### Swarm plot over Box plot ###################################################        
        ed_left_column5, ed_right_column5 = st.columns((2,2))

        with ed_left_column5:

            # swarm and box plot
            st.image('https://github.com/jonathjd/Education-Project/blob/main/reports/figures/swarm_plot_boxplot.png?raw=true')

        with ed_right_column5:

            # subheader
            st.subheader("Swarm/Box Plot")

            st.write('''
            In an effort to be more precise:
            - The two most expensive public universities in the U.S. are less expensive that just about half of the private universities in the U.S.
            - These two universities are **The University of New Hampshire** and **The University Texas Houston Health Science**.
            ''')


############################################### University Dataframe #################################################
        with st.container():

            #subheader
            st.subheader("University DataFrame")
            st.write("If you would like to see a specific attribute of any individual institution (such as in-state tuition, location, etc) please refer to the dataframe below!")

            #--- Display dataframe---
            st.subheader("Institutional Data")
            st.write(df_display)