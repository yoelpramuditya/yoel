import streamlit as st
import pandas as pd
col1, col2, col3 = st.columns(3)
with col1:
      st.write('')
with col2:
      st.title('WELCOME TO MY BIO')
with col3:
      st.write('')
st.image('foto/9.jpg', width=200)
st.title('PROFIL')
st.info('NAMA : YOEL PRAMUDITYA')
st.info('TTL : JAKARTA,21 JUNI 2003')
st.info('AGAMA : KRISTEN')
st.info('JENIS KELAMIN : LAKI-LAKI')
st.info('PEKERJAAN : MAHASISWA')

st.title('')


