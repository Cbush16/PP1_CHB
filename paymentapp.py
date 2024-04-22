# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:38:57 2024

@author: bushc
"""
import streamlit as st
import payment as pa

st.title("Payment Calculator")
st.divider()

with st.sidebar:
    st.subheader("Options")
    option = st.radio("Choose an option", ["Use Calculators", "View Payment Functions"])

if option == "View Payment Functions":
    with open("payment.py", "r") as file:
        payment_functions = file.read()

    st.write("Payment functions in payment.py:")
    st.code(payment_functions, language="python")
else:
    with st.sidebar:
        st.subheader("Calculators")
        scale = st.radio("What payment calculator?",
                         ["***MP***", "***IP***", "***PP***"],
                         captions= ["Monthly Payment",
                                    "Interest Payment",
                                    "Principal Payment"])
    if scale == "***MP***":
        p = 'Enter the principal'
        r = 'Enter the monthly interest rate in decimal form'
        n = 'Enter the number of payments'
        P = st.number_input(p, step=1.0, value=0.0)
        R = st.number_input(r, step=0.001, value=0.000)
        N = st.number_input(n, step=1.0, value=0.0)
        if st.button('Calculate'):
            Mp = pa.mp(P, R, N)
            st.metric("Monthly payment", f'${Mp:.2f}')
    
    elif scale == "***IP***":
        p = 'Enter the principal'
        r = 'Enter the monthly interest rate in decimal form'
        n = 'Enter the number of payments'
        c = 'Enter the current payment month'
        P = st.number_input(p, step=1.0, value=0.0)
        R = st.number_input(r, step=0.01, value=0.0)
        N = st.number_input(n, step=1.0, value=0.0)
        C = st.number_input(c, step=1.0, value=0.0)
        if st.button('Calculate'):
            Ip = pa.ip(P, R, N, C)
            st.metric("Interest payment", f'${Ip:.2f}')
    
    else:
        a = 'Enter the total loan amount'
        r = 'Enter the interest rate in decimal form'
        n = 'Enter the number of payments'
        c = 'Enter the current payment month'
        A = st.number_input(a, step=1.0, value=0.0)
        R = st.number_input(r, step=0.01, value=0.0)
        N = st.number_input(n, step=1.0, value=0.0)
        C = st.number_input(c, step=1.0, value=0.0)
        if st.button('Calculate'):
            Pp = pa.pp(A, R, N, C)
            st.metric("Principal payment", f'${Pp:.2f}')

