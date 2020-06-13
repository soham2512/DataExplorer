import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import numpy as np
import os




def main():
    html_head = """
        	<div style="background-color:#554dff;">
        	<p style="color:white;font-size:50px;padding:20px;padding-bottom:0px;font-weight:bold">
        	 THE DATA-EXPLORER
        	</p>
        	<p style="color:white;font-size:20px;margin-left:20px;padding-bottom:10px" >
        	&nbsp&nbsp&nbsp&nbsp- An Data Analytics WEB-APP</p>
        	</div>"""

    st.markdown(html_head, unsafe_allow_html=True)

    st.subheader("An Web-App for Data Analysts "
                 "& Data Explorers !!")

    st.subheader("Made with ❤️ For Data Science Community !!! ")

    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")

    # ------sidebar-header parrt----------

    html_head = """
        	<div style="background-color:#00b3ff;">
        	<p style="color:white;font-size:20px;padding:7px; text-align:Center;font-weight:bold;">
        	Hello, Welcome to<br>
        	The DATA-EXPLORER  
        	Web App
        	</p></div>
        	"""

    st.sidebar.markdown(html_head, unsafe_allow_html=True)

    # -----side-bar harder over-----------

    # ----introduction-------------


    st.subheader(" About DATA-EXPLORER WEB-APP :")

    whatis = """
                	<div style="background-color:#ff7817;">
                	<p style="color:white;font-size:20px;padding:15px; text-align:justify;">
                	DATA-Explorer is a webapp which allows you to explore through 
                	the data of your CSV Files and gain valuable insights through it .  
                	</p>

                	</div>

                	"""

    st.markdown(whatis, unsafe_allow_html=True)

    st.markdown("")

    selectservices = """              	
                        <p style="background-color:#ff7817;color:white;font-size:30px;padding:15px; text-align:justify;">
                	    👈  Select the services from the side-bar menu.</p>

                	    """
    st.markdown(selectservices, unsafe_allow_html=True)

    st.markdown("")
    st.markdown("")
    st.markdown("")

    # ------introduction over---------



    # ------Services sidebar----------------


    st.sidebar.markdown("")
    st.sidebar.markdown("")

    # html_head = """
    #        	<div style="background-color:#8800ff;">
    #        	<p style="color:white;font-size:15px;padding:5px; text-align:left;font-weight:bold;">
    #        	Select from the below Services :
    #        	</p></div>
    #        	"""
    #
    # st.sidebar.markdown(html_head, unsafe_allow_html=True)

    st.sidebar.header("SELECT BELOW SERVICES")

    selectactivity = ["Data-exploration & Insights", "Plotting and Graphing - Analytics"]

    choice = st.sidebar.selectbox("AVAILABLE SERVICES :", selectactivity)

    # ------services sidebar over-----------


    # ---------Data-exploration & Information------
    if choice == 'Data-exploration & Insights':

        dropdown = """
                                    	<div style="background-color:#ff0073;">
                                    	<p style="color:white;font-size:20px;padding:10px; text-align:Center;font-weight:bold;">
                                    	Upload Your Dataset 👉 

                                    	</p></div>

                                    	"""

        st.sidebar.markdown(dropdown, unsafe_allow_html=True)

        dataexplore = """
                	<div style="background-color:#0800ff;">
                	<p style="color:white;font-size:30px;padding:10px; text-align:Center;font-weight:bold;">
                    The Data-exploration & Insights
                    <br> 
                    <p style="color:white;font-size:20px;padding:10px;padding-top:0px; text-align:Center;font-weight:bold;">
                    Upload Your Dataset Below
                    </p></p>
                    </div>
                	"""

        st.markdown(dataexplore, unsafe_allow_html=True)

        st.markdown("")

        st.header("Data insights and operations to get valuable insights.")
        # st.subheader("Upload your Dataset Below.")


        data = st.file_uploader("Upload a Dataset in [ CSV ] format to explore.", type=["csv", "txt"])
        if data is not None:
            df = pd.read_csv(data)
            if st.checkbox("Show the DATASET :"):
                st.dataframe(df)

            dataexploration = ["Operations on Dataset", "Plotting"]

            one = st.selectbox("select from below :", dataexploration)

            if one == 'Operations on Dataset':

                if st.checkbox("Show Shape ( Rows,Columns )"):
                    st.write(df.shape)

                if st.checkbox("Show Columns ( List of Columns :)"):
                    all_columns = df.columns.to_list()
                    st.write(all_columns)

                if st.checkbox("Summary of the dataset"):
                    st.write(df.describe())

                if st.checkbox("Show Selected Columns"):
                    selected_columns = st.multiselect("Select Columns", all_columns)
                    new_df = df[selected_columns]
                    st.dataframe(new_df)

                if st.checkbox("Show Value Counts"):
                    st.write(df.iloc[:, -1].value_counts())

            if one == 'Plotting':

                st.warning("WARNING : This Data Exploration service of graphing "
                           "and plotting will "
                           "work well if you upload datasets "
                           "with single label and all other numerical values. "
                           "\n Numerical values are must Required. ")

                if st.checkbox("Correlation Plot(Matplotlib)"):
                    plt.matshow(df.corr())
                    st.pyplot()

                if st.checkbox("Correlation Plot(Seaborn)"):
                    st.write(sns.heatmap(df.corr(), annot=True))
                    st.pyplot()

                if st.checkbox("Pie Plot"):
                    all_columns = df.columns.to_list()
                    column_to_plot = st.selectbox("Select 1 Column", all_columns)
                    pie_plot = df[column_to_plot].value_counts().plot.pie(autopct="%1.1f%%")
                    st.write(pie_plot)
                    st.pyplot()

    # ---------Data-exploration & Information over------



    # -------------plotting and graphing , data-visulization----
    elif choice == 'Plotting and Graphing - Analytics':

        dropdown = """
                            	<div style="background-color:#ff0073;">
                            	<p style="color:white;font-size:20px;padding:10px; text-align:Center;font-weight:bold;">
                            	Upload Your Dataset 👉 
                            	
                            	</p></div>

                            	"""

        st.sidebar.markdown(dropdown, unsafe_allow_html=True)

        analytics = """
                	<div style="background-color:#0800ff;">
                	<p style="color:white;font-size:30px;padding:10px; text-align:Center;font-weight:bold;">
                    The Data Analytics
                    <p style="color:white;font-size:20px;padding:10px;padding-top:0px; text-align:Center;font-weight:bold;">
                    Upload Your Dataset Below
                    </p>
                	"""

        st.markdown(analytics, unsafe_allow_html=True)

        st.markdown("")

        st.subheader("Data plotting and visulizations by  Analytics")

        data = st.file_uploader("Upload a Dataset in [ CSV ] format to explore.", type=["csv", "txt"])

        if data is not None:
            df = pd.read_csv(data)
            if st.checkbox("Show the DATASET :"):
                st.dataframe(df)

            if st.checkbox("Show Value Counts : "):
                st.write(df.iloc[:, -1].value_counts().plot(kind='bar'))
                st.pyplot()

            # Customizable Plot
            st.markdown("")

            customize = """
                    	<div style="background-color:#ff0073;">
                    	<p style="color:white;font-size:20px;padding:10px;padding-bottom:0px; text-align:Center;font-weight:bold;">
                    	Customized plotting of your choice
                    	<p style="color:white;font-size:15px;padding:10px;padding-top:0px; text-align:left;font-weight:bold;">
                    	&nbsp &nbsp &nbsp👉 &nbsp select type of plot and columns of your choice enjoy real time analytics of your dataset
                        </p></p>
                        </div>

                    	"""

            st.markdown(customize, unsafe_allow_html=True)

            st.markdown("")

            all_columns_names = df.columns.tolist()
            type_of_plot = st.selectbox("Select Type of Plot",
                                        ["area", "bar", "line", "histogram", "box", "kde"])
            selected_columns_names = st.multiselect("Select Columns To Plot", all_columns_names)

            if st.button("Generate Plot"):
                st.success("Generating Customizable Plot of {} for {}".format(type_of_plot, selected_columns_names))
                # Plot By Streamlit
                if type_of_plot == 'area':
                    cust_data = df[selected_columns_names]
                    st.area_chart(cust_data)

                elif type_of_plot == 'bar':
                    cust_data = df[selected_columns_names]
                    st.bar_chart(cust_data)

                elif type_of_plot == 'line':
                    cust_data = df[selected_columns_names]
                    st.line_chart(cust_data)

                # Custom Plot
                elif type_of_plot:
                    cust_plot = df[selected_columns_names].plot(kind=type_of_plot)
                    st.write(cust_plot)
                    st.pyplot()

                # -------------plotting and graphing , data-visulization over----

    #------------credentials--------------

    st.sidebar.markdown("")
    st.sidebar.markdown("")
    st.sidebar.markdown("")
    st.sidebar.markdown("")
    st.sidebar.markdown("")
    st.sidebar.markdown("")
    st.sidebar.markdown("")
    st.sidebar.markdown("")

    st.sidebar.markdown("")
    st.sidebar.markdown("")
    st.sidebar.markdown("")

    customize = """
                        	<div style="background-color:#ff3b3b;">
                        	<p style="color:white;font-size:15px;padding:10px;text-align:Center;font-weight:bold;">
                        	Made with by SOHAM SHAH
                        	<br>
                        	<a href="https://github.com/soham2512">Visit my Github !!</a>
                        	</p></div>
                        	
                        	<p style=";font-size:20px;text-align:Center;font-weight:bold;">
                        	
                        	</p>
                        	


                        	"""

    st.sidebar.markdown(customize, unsafe_allow_html=True)

    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")

    st.markdown("")
    st.markdown("")
    st.markdown("")

    customize = """
                            	<div style="background-color:#ff3b3b;">
                            	<p style="color:white;font-size:25px;padding:10px;text-align:Center;font-weight:bold;">
                            	Made by SOHAM SHAH
                            	<br>
                            	<a href="https://github.com/soham2512">Visit my Github !!</a>
                            	</p></div>

                            	<p style=";font-size:20px;text-align:Center;font-weight:bold;">

                            	</p>



                            	"""

    st.markdown(customize, unsafe_allow_html=True)


if __name__ == '__main__':
	main()
