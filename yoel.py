import streamlit as st
import pandas as pd
col1, col2, col3 = st.columns(3)
with col1:
      st.write('')
with col2:
      st.title('WELCOME')
with col3:
      st.write('')
st.image('foto/9.jpg', width=200)
st.title('TENTANG SAYA')
st.info('NAMA : YOEL PRAMUDITYA')
st.info('TTL : JAKARTA,21 JUNI 2003')
st.info('AGAMA : KRISTEN')
st.info('JENIS KELAMIN : LAKI-LAKI')
st.info('PEKERJAAN : MAHASISWA')
st.info('HOBI : \n\n• OLAHRAGA\n\n• MEMBACA BUKU\n\n• BERNYANYI')

col1, col2, col3 = st.columns(3)
with col1:
      st.info('KEMAMPUAN')
      st.write('• Mampu Menganalisis Data Kesehatan.\n\n• Mampu Mengcoding Diagnosa Penyakit.\n\n• Mampu Membuat Laporan Rekan Medis')
with col2:
      st.info('RIWAYAT PENDIDIKAN')
      st.write('• SDN PETOJO UTARA 01 PAGI.\n\n• SMPN 31 SEMARANG.\n\n• SMKN 3 SEMARANG')
with col3:
      st.info('PENGALAMAN KERJA')
      st.write('• Pernah Bekerja Dibagian Rekam Medis.\n\n• Pernah Bekerja Dianalisi Data Kesehatan.')
st.header(":mailbox: Masukan saran!")

contact_form = """
<form action="https://formsubmit.co/yoel.pramuditya@gmail.com" method="POST">
     <input type="text" name="name" required>
     <input type="email" name="email" required>
     <button type="submit">Kirim</button>
</form>
st.markdown(contact_form, unsafe_allow_html=True)

