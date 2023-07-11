import streamlit as st
import pandas as pd

def main():
    st.write("*:black[Terimakasih sudah berkunjung]*")
st.sidebar.header(':rocket: Menu')
menu = st.sidebar.radio('Navigasi', ['Wellcome', 'Biodata', 'Tentang', 'Kontak', 'Kotak Saran'])