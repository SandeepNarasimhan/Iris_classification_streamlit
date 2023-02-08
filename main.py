import requests
import json
import streamlit as st

# Define the title
def run():
    st.title("Iris Classification")
    st.write(
        """The Iris dataset was used in R.A. Fisher's classic 1936 paper, The Use of Multiple Measurements in Taxonomic Problems, and can also be found on the "UCI Machine Learning Repository".
        It includes three iris species with 50 samples each as well as some properties about each flower. One flower species is linearly separable from the other two, but the other two are not linearly separable from each other."""
        #The columns in this dataset are \n
        #Id\n
        #Sepal Length in Cm\n
        #Sepal Width in Cm\n
        #Petal Length in Cm\n
        #Petal Width in Cm and\n
        #Species
        )

    # Input 1
    sepal_length = st.number_input(
        "Sepal Lenght",
        min_value=0.0, max_value=10.0, step=0.1
    )

    # Input 2
    sepal_width = st.number_input(
        "Sepal Width",
        min_value=0.0, max_value=10.0, step=0.1
    )

    # Input 3
    petal_length = st.number_input(
        "Petal Lenght",
        min_value=0.0, max_value=10.0, step=0.1
    )

    # Input 4
    petal_width = st.number_input(
        "Petal Width",
        min_value=0.0, max_value=10.0, step=0.1
    )

     # Inputs to ML model (Localhost)
    #inputs = {
    #            "sepal_length": sepal_length,
    #            "sepal_width": sepal_width,
    #            "petal_length": petal_length,
    #           "petal_width": petal_width
    #        }

    # Inputs to ML model (Cerebrium)
    inputs = [[sepal_length, sepal_width,petal_length,petal_width]]

    # When 'Predict' is selected
    if st.button("Predict"):

        # Class values to be returned by the model
        class_values = {
            0: "Setosa",
            1: "Versicolor",
            2: "Verginica"
            }
        
        # Posting inputs to ML API (Localhost)
       # response = requests.post(f"http://localhost:8080/predict", json=inputs, verify=False)
       # prediction = response.text
        
        # Posting inputs to ML API (Cerebrium)
        response = requests.post(f"https://run.cerebrium.ai/p-7d56f8f3/sklearn-rf-model/predict", json=inputs, verify=False)
        prediction = json.loads(response.text)
        
        prediction = class_values[prediction.get("result")[0]]
        
        st.write(f'Species: **{prediction}**')

if __name__ == '__main__':
    run()