import streamlit as st
from calculator import Calculator

calc = Calculator()

st.set_page_config(page_title='AI Finance Calculator', layout='wide')

st.title('🚀 AI Finance & Scientific Calculator')
st.markdown('### Modern Neon Finance Dashboard')

menu = st.sidebar.selectbox('Choose Calculator', [
    'EMI Calculator',
    'SIP Calculator',
    'CAGR Calculator',
    'Scientific Calculator'
])

if menu == 'EMI Calculator':
    st.header('EMI Calculator')
    principal = st.number_input('Loan Amount', value=500000)
    rate = st.number_input('Interest Rate', value=8.5)
    years = st.number_input('Tenure (Years)', value=10)

    if st.button('Calculate EMI'):
        result = calc.emi(principal, rate, years)
        st.success(f'Monthly EMI: ₹{result}')

elif menu == 'SIP Calculator':
    st.header('SIP Returns Calculator')
    monthly = st.number_input('Monthly Investment', value=5000)
    rate = st.number_input('Expected Return (%)', value=12)
    years = st.number_input('Years', value=10)

    if st.button('Calculate SIP Returns'):
        result = calc.sip_returns(monthly, rate, years)
        st.success(f'Future Value: ₹{result}')

elif menu == 'CAGR Calculator':
    st.header('CAGR Calculator')
    beginning = st.number_input('Beginning Value', value=1000)
    ending = st.number_input('Ending Value', value=2000)
    years = st.number_input('Years', value=5)

    if st.button('Calculate CAGR'):
        result = calc.cagr(beginning, ending, years)
        st.success(f'CAGR: {result}%')

elif menu == 'Scientific Calculator':
    st.header('Scientific Calculator')
    number = st.number_input('Enter Number', value=64)

    if st.button('Square Root'):
        st.success(f'Square Root: {calc.square_root(number)}')
