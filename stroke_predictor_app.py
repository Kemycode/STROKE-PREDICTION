{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d248a0ee-f0dc-45e9-8152-dfd578528103",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "630c2816-7b8a-4871-9dae-c059681196b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# Load the trained model\n",
    "model = joblib.load(\"C:/Users/USER/Desktop/MSC DISSERTATION/stroke_prediction_model.pkl\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "5cb04e6f-99ef-4006-b329-9876fc652771",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define the Streamlit app\n",
    "def main():\n",
    "    st.title(\"Stroke Prediction App\")\n",
    "    st.write(\"Enter the patient details below to predict the risk of stroke.\")\n",
    "    # User input fields\n",
    "    age = st.number_input(\"Age\", min_value=1, max_value=120, value=30)\n",
    "    gender = st.selectbox(\"Gender\", [\"Male\", \"Female\", \"Other\"])\n",
    "    hypertension = st.selectbox(\"Hypertension (0 = No, 1 = Yes)\", [0, 1])\n",
    "    heart_disease = st.selectbox(\"Heart Disease (0 = No, 1 = Yes)\", [0, 1])\n",
    "    ever_married = st.selectbox(\"Ever Married\", [\"Yes\", \"No\"])\n",
    "    work_type = st.selectbox(\"Work Type\", [\"Private\", \"Self-employed\", \"Govt_job\", \"Children\", \"Never_worked\"])\n",
    "    residence_type = st.selectbox(\"Residence Type\", [\"Urban\", \"Rural\"])\n",
    "    avg_glucose_level = st.number_input(\"Average Glucose Level\", min_value=0.0, max_value=500.0, value=100.0)\n",
    "    bmi = st.number_input(\"BMI\", min_value=0.0, max_value=100.0, value=25.0)\n",
    "    smoking_status = st.selectbox(\"Smoking Status\", [\"formerly smoked\", \"never smoked\", \"smokes\", \"Unknown\"])\n",
    "\n",
    "     # Create input data DataFrame\n",
    "    input_data = pd.DataFrame({\n",
    "        'age': [age],\n",
    "        'gender': [gender],\n",
    "        'hypertension': [hypertension],\n",
    "        'heart_disease': [heart_disease],\n",
    "        'ever_married': [ever_married],\n",
    "        'work_type': [work_type],\n",
    "        'Residence_type': [residence_type],\n",
    "        'avg_glucose_level': [avg_glucose_level],\n",
    "        'bmi': [bmi],\n",
    "        'smoking_status': [smoking_status]\n",
    "    })"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "5877a710-16b7-43dc-8998-c89c3be3c2de",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-11-27 15:16:46.296 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:46.299 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:46.303 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:46.310 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:46.983 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2024-11-27 15:16:46.986 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "\n",
    "    # Predict stroke risk\n",
    "    if st.button(\"Predict\"):\n",
    "        try:\n",
    "            prediction = model.predict_proba(input_data)[:, 1][0]  # Get stroke risk probability\n",
    "            st.write(f\"Predicted Stroke Risk: {prediction:.2%}\")\n",
    "        except Exception as e:\n",
    "            st.error(f\"An error occurred: {e}\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "146dd60b-1f77-4fcf-876b-8b5c91d0a1af",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-11-27 15:16:51.967 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:51.969 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:51.972 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:51.974 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:51.976 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:51.981 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:51.983 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:51.986 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:51.988 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:51.990 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:51.992 Session state does not function when running a script without `streamlit run`\n",
      "2024-11-27 15:16:51.993 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:51.995 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:51.997 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:51.999 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.001 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.001 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.003 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.006 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.007 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.009 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.011 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.012 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.014 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.014 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.021 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.024 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.026 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.027 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.028 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.036 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.041 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.043 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.051 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.054 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.055 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.056 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.058 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.059 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.068 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.071 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.073 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.075 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.076 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.132 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.135 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.139 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.142 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.144 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.146 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.147 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.149 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.150 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.151 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.152 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.154 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.155 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.157 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.158 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.160 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.161 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.162 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.163 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.165 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.169 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.170 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-11-27 15:16:52.172 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "# Run the app\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "id": "073e6984-ba9d-472d-8278-0ef39716c9d0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
