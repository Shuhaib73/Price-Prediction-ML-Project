# Import necessary libraries.
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import time as t
import base64

# Function to customize the web layout by hiding certain elements
def web_customes():                                                                         
    hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """
    return st.markdown(hide_st_style, unsafe_allow_html=True)

# Function to create the top navigation bar
def tool_bar():
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

    st.markdown("""
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #151314;">
    <div class="navbar-collapse collapse w-100 order-1 order-md-0 dual-collapse2">
        <ul class="navbar-nav ml-auto">
            <li class="nav-item active">
                <a class="nav-link" href="https://github.com/Shuhaib73/Price-Prediction-ML-Project.git">GitHub<span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="https://www.linkedin.com/in/mohamedshuhaib/" target="_blank">LinkedIn</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="https://www.carmagazine.co.uk/car-news/motoring-issues/" target="_blank">Monitoring Issues</a>
            </li>
        </ul>
    </div>
    </nav>
    """, unsafe_allow_html=True)

# Function to get background image for Streamlit app
def get_background(file_name):

    main_bg_ext = "png"

    with open(file_name, 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()

    return st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/{main_bg_ext};base64,{encoded_image});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )



# Main application function
def app():
    
    # Set page configuration for the app
    st.set_page_config(page_title="Car Price Prediction", page_icon=":info", layout="centered")
    
    web_customes()                              # Calling web-customized Function
    tool_bar()                                  # Calling tool bar Function
    get_background("images/bg_mn.png")          # Set background image

    # Create an option menu for navigation
    selected = option_menu(
        menu_title=None,
        options=['Home', 'Predictor', 'Project Info', 'Contact'],
        icons=['house', 'robot', 'book', 'envelope'],
        menu_icon='cast',
        default_index=0,
        orientation='horizontal'
    )
    
    
    if selected == 'Home':

        # Use CSS styling to adjust the position of the button
        st.markdown(
            """
            <style>
                .button-container {
                    display: flex;
                    justify-content: center;
                    margin-top: 100px; /* Adjust the margin to change the vertical position */
                    margin-right: 50px;;
                }
                .custom-button {
                    padding: 10px;
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                    cursor: pointer;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Create a button inside a container div
        button_container = st.container()
        with button_container:
            st.markdown('<div class="button-container">', unsafe_allow_html=True)
            st.markdown('<a href="https://www.topgear.com/car-news/top-gear-magazine-0" target="_blank">Car Magazine</a>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)


    # Function to get data from a CSV file 
    @st.cache_data
    def get_data():
        df = pd.read_csv('scaled_data.csv', index_col=0)

        return df
    
    df = get_data()


    if selected == 'Predictor':
        
        get_background('images/pred_bg.png')       # Set background image for the Predictor section

        # Create a form with two columns
        with st.form(key='form', clear_on_submit=False):
            
            # Split the form into two columns
            col1, col2 = st.columns(2)

            Brand = col1.selectbox("Brand", df['Make'].sort_values(ascending=True).unique())
            Model = col2.selectbox("Model", df['Model'].sort_values(ascending=True).unique())
            Year = col1.text_input("Year of Manufacture")
            Fuel_type = col2.selectbox("Fuel Type", df['Engine Fuel Type'].sort_values(ascending=True).unique())
            Engine_hp = col1.text_input("Engine HP")
            Cylinders = col2.selectbox("Engine Cylinders", df['Engine Cylinders'].sort_values(ascending=True).unique())
            Trans_type = col1.selectbox("Transmission Type", df['Transmission Type'].sort_values(ascending=True).unique())
            Wheel = col2.selectbox("Driven Wheel", df['Driven_Wheels'].sort_values(ascending=True).unique())
            Doors = col1.selectbox("Number of Doors", df['Number of Doors'].sort_values(ascending=True).unique())
            Size = col2.selectbox("Vehicle Size", df['Vehicle Size'].sort_values(ascending=True).unique())
            Style = col1.selectbox("Vehicle Style", df['Vehicle Style'].sort_values(ascending=True).unique())
            Pop = col2.text_input("Popularity")
            Mileage = col1.text_input("Mileage")

            # Form submission button
            Submit = st.form_submit_button("Predict the Selling Price")
     

            if Submit:
                # Check if any feature is missing
                if any([not Brand, not Model, not Year, not Fuel_type, not Engine_hp, not Cylinders, not Trans_type, not Wheel, not Doors, not Size, not Style, not Pop, not Mileage]):
                    st.warning("Please fill in all the Car details")

                else:
                    # Load the pre-trained machine learning model
                    with open('Car_Model1.pkl', 'rb') as f:
                        model = pickle.load(f)

                    # Create a DataFrame with the input features
                    features = [Brand, Model, Year, Fuel_type, Engine_hp, Cylinders, Trans_type, Wheel, Doors, Size, Style, Pop, Mileage]
                    feature_df = pd.DataFrame([features], columns=['Make', 'Model', 'Year', 'Engine Fuel Type', 'Engine HP', 'Engine Cylinders', 'Transmission Type', 'Driven_Wheels', 'Number of Doors', 'Vehicle Size', 'Vehicle Style', 'Popularity', 'Avg Mileage'])

                    # Convert selected columns to the appropriate data types
                    feature_df['Year'] = feature_df['Year'].astype(int)
                    feature_df['Engine HP'] = feature_df['Engine HP'].astype(int)
                    feature_df['Engine Cylinders'] = feature_df['Engine Cylinders'].astype(int)
                    feature_df['Number of Doors'] = feature_df['Number of Doors'].astype(int)
                    feature_df['Popularity'] = feature_df['Popularity'].astype(int)
                    feature_df['Avg Mileage'] = feature_df['Avg Mileage'].astype(int)

                    cols = feature_df.select_dtypes('object').columns

                    # Encode categorical columns using Label Encoding
                    encoder = LabelEncoder()
                    for col in cols:
                        feature_df[col] = encoder.fit_transform(feature_df[col])

                    # Make predictions using the machine learning model
                    predicted_price = model.predict(feature_df)

                    # Display the predicted price with formatting
                    st.markdown(f"<p style='font-size: 26px; font-weight: bold; text-align: center; color: #03045e; background-color: #4cc9f0;'>{str(predicted_price).split('.')[0].replace('[', '')} $</p>", unsafe_allow_html=True)
                    st.balloons()


    if selected == 'Project Info':
        
        get_background('images/info_bg.png')

        # Diplay optoins for the Info section
        options = st.selectbox(
            'Would you like to know more about this project?',
            (' ', 'Description')
        )

        if options == 'Description':
            with open('Description.html', 'r', encoding='utf-8') as f:
                data = f.read()
                st.markdown(f"<div style='background-color:black; '>{data}</div>", unsafe_allow_html=True)     
        else:
            pass

        # Display information about the data
        if 'number_of_rows' not in st.session_state:
            st.session_state['number_of_rows'] = 5

        # Input the number of rows to be displayed
        increment = st.text_input('Specify the number of rows to be displayed')
        
        if increment:
            increment = int(increment)
            st.session_state['number_of_rows'] = increment

        # Input the Brands in the sidebar
        st.sidebar.markdown("<h2 style='text-align: center; color: #ff758f; font-size: 18px;'>Please Filter Here:</h2>", unsafe_allow_html=True)

        Brands = st.sidebar.multiselect(
            "Select the Brands: ",
            options=df['Make'].unique(),
            default=['BMW', 'Audi', 'Volvo', 'Ferrari', 'Mercedes-Benz']
        )

        # Apply the filters on the Dataframe
        filtered_df = df[df['Make'].isin(Brands)].head(st.session_state['number_of_rows'])

        # Display the filtered Dataframe
        st.dataframe(filtered_df)


    if selected == 'Contact':

        get_background("images/con_bg1.png")

        # Display the heading for the contact Section
        st.markdown("<h2 style='text-align: center; color: #ced4da; font-size: 18px;'><span style='margin-right: 10px;'>📬</span>Get In Touch with us!</h2>", unsafe_allow_html=True)

        # Contact form HTML Code
        contact_form= """
        <form action="https://formsubmit.co/bursins77@gmail.com" method='POST'>
            <input type='hidden' name='_captcha' value='false'>
            <input type='text' name='name' placeholder='Name' required style='color: #001d3d;'>
            <input type='email', name='email' placeholder='Email' pattern='[a-zA-Z]+[0-9]*@[a-zA-Z]+\.[a-zA-Z]{2,}' required style='color: #001d3d;'>
            <textarea name='Message' placeholder='Your message here'></textarea>
            <button type='Submit'>Send</button>
        </form>
        """

        # Display the contact form
        st.markdown(contact_form, unsafe_allow_html=True)

        # Apply css style
        def Style_css(file_name):
            with open(file_name) as f:
                st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

        Style_css('Style_css.css')


# Main function to run the app
def main():
    app()


# Run the main function if the script is executed directly
if __name__ == '__main__':
    main()
