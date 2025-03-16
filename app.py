import hehe as st
import numpy as np
import pandas as pd
def read_data():
    return pd.read_csv("score.csv")
def show_data():
    st.dataframe(read_data(),hide_index=True)
    
def main():
    df = read_data()
    show_data(df)
main()
