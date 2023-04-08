import streamlit as st
from predict import pred

def main():
    st.title("Prediksi Diabetes")

    # Create input fields for all 11 features
    input_values = {}
    input_labels = {
        'Pregnancies': 'Pregnancies',
        'Glucose': 'Glucose',
        'BloodPressure': 'BloodPressure',
        'SkinThickness': 'SkinThickness',
        'Insulin': 'Insulin',
        'BMI': 'BMI',
        'DiabetesPedigreeFunction': 'DiabetesPedigreeFunction',
        'Age': 'Age'
    }
    with st.form("Cek Data"):
        for feature_name, feature_label in input_labels.items():
            input_values[feature_name] = st.text_input(feature_label)
        
        # Check if all inputs have been filled
        all_filled = all(input_values.values())
        submitted = st.form_submit_button("Submit")

        # Create submit button if all inputs have been filled
        if all_filled and submitted:
            # Convert input values to floats
            input_array = [[float(value) for value in input_values.values()]]

            # Make prediction and display result
            value = pred(input_array)
            if value>=0.5:
                diabet='(Terkena Diabetes)'
            else:
                diabet='(Tidak Diabetes)'
            st.write(f"Prediksi Diabetes : {value:.3f}\n{diabet}")

if __name__ == "__main__":
    main()
