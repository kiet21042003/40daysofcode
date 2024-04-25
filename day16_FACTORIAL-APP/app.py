import streamlit as st
import factorial as fact

def main():
    st.title("Factorial App")
    n = st.number_input("Enter a number:", min_value=0, max_value=90, step=1)
    if st.button("Calculate"):
        result = fact.factorial(n)
        st.write(f"The factorial of {n} is {result}")
        st.balloons()

if __name__ == "__main__":
    main()