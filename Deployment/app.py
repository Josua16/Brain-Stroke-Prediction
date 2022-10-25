from codecs import latin_1_decode
import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('pipe_stroke.pkl', 'rb'))

st.header('Selamat Datang di Rumah Sakit INI')
st.write('Kesehatan anda menjadi prioritas bagi kami, \n pastikan anda menginput data dengan benar')

age = st.number_input('Masukkan Umur Anda (ihh takut ketahuan sudah tua yaa)')
avg_glucose_level = st.number_input('Masukkan Kadar Gula (input berdasarkan hasil pemeriksaan RS INI)')
bmi = st.number_input('Masukkan Berat Badan Anda (jangan takut gemuk yaaa)')

st.write('Silakan Menjawab Beberapa pertanyaan berikut:')
hypertension = st.selectbox('Apakah Anda memiliki riwayat hypertensi (darah tinggi)?', ['NO', 'Yes'])
heart_disease = st.selectbox('Apakah Anda punya riat penyakit jantung?', ['NO', 'Yes'])
ever_married = st.selectbox('Apakah Anda sudah Menikah?', ['Yes', 'No'])
work_type = st.selectbox('Pilih Jenis Pekerjaan Anda (Jika tidak ada, pilih yang mengambarkan pekerjaan anda)', ['Self-employed', 'Private', 'Govt_job', 'children'])


if st.button('submit'):
    num_inf = dict()
    cat_inf = dict()

    num_cols = ['age', 'avg_glucose_level', 'bmi']
    cat_cols = ['hypertension','heart_disease','ever_married','work_type']

    num_df = pd.DataFrame([[age, avg_glucose_level, bmi]], columns=num_cols)
    cat_df = pd.DataFrame([[hypertension, heart_disease, ever_married, work_type]], columns=cat_cols)

    X = pd.concat([num_df, cat_df], axis=1)

    #st.write(encoded_dat)
    #st.write(X)
    pred = model.predict(X)


    if pred[0] == 1:
        st.text('ANDA BERPOTENSI TERKENA BRAIN STROKE, \n Disarankan Anda untuk segera berkonsultasi dengan dokter atau melakukan  saran dari kami, \n 1. berolahraga secara teratur, \n 2. hindari makan - makan yang memicu brain stroke sepert gula, lemak, daging, dan garam, \n 3. berhenti merokok, dan minum alkohol , \n 4. beristirahat yang cukup dan banyak minum air putih, \n Terima kasih telah berobat di Rumah Sakit INI')
    else:
        st.text('SELAMAT ANDA TIDAK BERPOTENSI TERKENA BRAIN STROKE, \n jangan lupa tetap jaga kesehatan yaaa...., \n Terima Kasih telah Berobat di Rumah Sakit INI')

  
