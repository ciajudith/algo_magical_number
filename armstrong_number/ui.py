import streamlit as st

from armstrong_number_function import is_an_armstrong_number

st.set_page_config("Armstrong Number checker")
st.title("Armstrong Number Checker")
st.write("This tool checks if the given number is an Armstrong number.")
st.info("An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of the digits.")

number = int(st.number_input("Enter a number: ", min_value=1))

if st.button("Check"):
    is_armstrong, list_of_remainders, calculate, power = is_an_armstrong_number(number)
    st.subheader(f"Result for {number}")
    expression = " + ".join(f"{i}^{power}" for i in list_of_remainders)
    values = " + ".join(str(i ** power) for i in list_of_remainders)
    if is_armstrong:
        st.latex(f"{expression} = {values} = {calculate}")
        st.success(f"{number} is an Armstrong number.")
    else:
        st.latex(f"{expression} = {values} = {calculate}.")
        st.error(f" {number} is not an Armstrong number.")
