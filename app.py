import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import catboost
import warnings
warnings.filterwarnings('ignore')

file = open('model.joblib','rb')
model = joblib.load(file)

st.title('Loan Default Prediction')
st.subheader('Predicting Loan Defaulters')
st.write('SuperLender is a local digital lending company, which prides itself in its effective use of credit risk models to deliver profitable and high-impact loan alternative. Its assessment approach is based on two main risk drivers of loan default prediction:. 1) willingness to pay and 2) ability to pay. Since not all customers pay back, the company invests in experienced data scientist to build robust models to effectively predict the odds of repayment.')

html_temp = """
    <div style ='background-color: blue; padding:10px'>
    <h1><font color=red> Streamlit ML Web App </font></h1>
    </div>
    """

st.markdown(html_temp, unsafe_allow_html=True)

st.write('Please provide the following details for customers')

loannumber_x = st.slider('The number of loan collected recently',1,30)
loanamount_x = st.slider('The amount of loan collected recently in naira',4000,60000)
totaldue_x = st.slider('The total amount of recent loan paid with interest in naira',5000,70000)
termdays_x = st.slider('The duration of payment for recent loan',15,90)
bank_account_type = st.selectbox('Bank Account Type of Clients',(1,2,3))#('Savings','Current','Others'))
employment_status_clients = st.selectbox('Employment Status of Clients',(1,2,3,4,5,6))#('Permanent','Self-employed','Retired','Contract','Umemployed','Student'))
loannumber_y = st.slider('The number of loan collected previously',1,30)
loanamount_y = st.slider('The amount of loan collected previously in naira',4000,60000)
totaldue_y = st.slider('The total amount of previous loan paid with interest in naira',5000,70000)
termdays_y = st.slider('The duration of payment for previous loan',15,90)


features = {'loannumber_x':loannumber_x,
'loanamount_x' : loanamount_x,
'totaldue_x' : totaldue_x,
'termdays_x' : termdays_x,
'bank_account_type' : bank_account_type,
'employment_status_clients' : employment_status_clients, 
'loannumber_y' :loannumber_y,
'loanamount_y' : loanamount_y,
'totaldue_y' : totaldue_y,
'termdays_y' : termdays_y
}

if st.button('Submit'):
    data = pd.DataFrame(features,index=[0,1])
    st.write(data)

    prediction = model.predict(data)
    proba = model.predict_proba(data)[1]

    if prediction[0] == 0:
        st.success('The customer paid back the loan')
    else:
        st.error('The Customer did not pay back the loan')

    proba_df = pd.DataFrame(proba,columns=['Probability'],index=['Paid','Unpaid'])
    proba_df.plot(kind='barh')
    st.pyplot()