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
st.title('**TENTANG SAYA**')
st.info('**NAMA** : YOEL PRAMUDITYA')
st.info('**TTL** : JAKARTA,21 JUNI 2003')
st.info('**AGAMA** : KRISTEN')
st.info('**JENIS KELAMIN** : LAKI-LAKI')
st.info('**PEKERJAAN** : MAHASISWA')
st.info('**HOBI** : \n\n• OLAHRAGA\n\n• MEMBACA BUKU\n\n• BERNYANYI')

col1, col2, col3 = st.columns(3)
with col1:
      st.info('**KEMAMPUAN**')
      st.write('• Mampu Menganalisis Data Kesehatan.\n\n• Mampu Mengcoding Diagnosa Penyakit.\n\n• Mampu Membuat Laporan Rekan Medis')
with col2:
      st.info('**RIWAYAT PENDIDIKAN**')
      st.write('• SDN PETOJO UTARA 01 PAGI.\n\n• SMPN 31 SEMARANG.\n\n• SMKN 3 SEMARANG')
with col3:
      st.info('**PENGALAMAN KERJA**')
      st.write('• Pernah Bekerja Dibagian Rekam Medis.\n\n• Pernah Bekerja Dianalisi Data Kesehatan.')
st.info('**KENALI LEBIH JAUH**')
col1, col2, col3 = st.columns(3)
with col1:
      st.info('**TENTANG SAYA**')
      st.write('saya adalah seorang yang bergerak dibidang analisi data kesehatan dimana saya mempelajari semua yang berkaitan dengan data kesehatan.')
with col2:
      st.info('**KONTAK PERSON**')
      st.write(':phone: call center [whatshap](https://wa.me/6283182905546)')
      st.write(':coffee: social media [instagram](https://instagram.com/pramuditya.yoel)')
with col3:
      st.info('**SARAN DAN MASUKAN**')
      st.write(':mailbox: masukan dan saran [Disini](https://forms.gle/8AE7shhhMDdEh1iH9)')
