import streamlit as st

st.set_page_config(
    page_title='7MinutesWorkout'
)

# Corrected CSS for media query
css = '''
    <style>
        [data-testid="stImageContainer"] {
            display: flex;
            justify-content: center;  
        }
        @media (max-width: 640px) {
            img {
                max-width: 130px;
            }
        }
    </style>
'''


st.markdown(css, unsafe_allow_html=True)

with st.container():
    st.title('7MinutesWorkout')

with st.container():
    left_column, right_column = st.columns(2)

    with left_column:
        st.image('image/minute-workout-1.png', width=200, caption='Gambar 1')

    with right_column:
        st.write('Gambar 1 adalah tampilan awal dari aplikasi 7MinutesWorkout. Tertampil tombol start, Calculator, dan History.')

with st.container():
    st.divider()
    left_column, right_column = st.columns(2)

    with left_column:
        st.image('image/minute-workout-2.png', width=200, caption='Gambar 2')

    with right_column:
        st.write('Saat tombol start ditekan, terdapat waktu 10 detik yang berhitung mundur menunjukkan aktivitas akan dimulai beberapa detik lagi.')

        st.write('Aktivitas yang akan datang juga terampil. Pada kondisi ini, yang dimunculkan adalah gerakan pertama, yaitu Jumping Jacks.')

        st.write('Di bagian bawah terdapat angka-angka yang menunjukkan banyaknya gerakan yang akan dilakukan pengguna.')

with st.container():
    st.divider()
    left_column, right_column = st.columns(2)

    with left_column:
        st.image('image/minute-workout-7.png', width=200, caption='Gambar 3')

    with right_column:
        st.write('Saat sudah masuk ke dalam sesi aktivitas, terdapat contoh gerakan yang harus dilakukan pengguna. Pada Gambar 3 ditampilkan gerakan pada nomor 12, yaitu Side Plank.')

        st.write('Pengguna hanya diberi waktu 30 detik selama aktivitas berlangsung.')

        st.write('Ketika aktivitas sudah dijalankan dan sudah melewati beberapa gerakan, maka angka-angka di bagian bawah akan berubah menjadi berwarna hijau.')

with st.container():
    st.divider()
    left_column, right_column = st.columns(2)

    with left_column:
        st.image('image/minute-workout-8.png', width=200, caption='Gambar 4')

    with right_column:
        st.write('Ketika pengguna sudah selesai melakukan aktivitas, kemudian keluar halaman di mana tanda aktivitas tersebut telah selesaai.')

        st.write('Terdapat tombol FINISH. Pengguna bisa keluar melalui tombol FINISH tersebut atau depan tombol kembali yang tersedia di atas kiri.')

with st.container():
    st.divider()
    left_column, right_column = st.columns(2)

    with left_column:
        st.image('image/minute-workout-9.png', width=200, caption='Gambar 5')

    with right_column:
        st.write('Tombol History pada tampilan awal ketika ditekan akan menampilkan riwayat-riwayat aktivitas yang pernah ia mulai/jalankan, seperti yang ditampilkan pada Gambar 5.')

with st.container():
    st.divider()
    left_column, right_column = st.columns(2)

    with left_column:
        st.image('image/minute-workout-10.png', width=265, caption='Gambar 5')
        st.image('image/minute-workout-14.png', width=200, caption='Gambar 6')

    with right_column:
        st.write('Tombol Calculator pada tampilan awal ketika ditekan akan menampilkan kalkulator BMI (Body Mass Index). BMI metode hitung-hitungan mudah yang dapat memberikan informasi dasar terhadap masalah berat badan Anda secara keseluruhan.')

        st.write('Pada Metric Units, yang diminta pengguna adalah berat (kg) dan tinggi (cm). Pada US Units, yang diminta pengguna adalah berat (pounds), tinggi (feet-inch).')

        st.write('Ketika pengguna memasukkan berat dan tinggi, program akan menghitung input lalu mengkalkulasikan input tersebut. Jika hasil yang sudah dihitung adalah hasil normal, makan output yang dikeluarkan adalah "Normal, Congratulations! You are in a good shape!" - Gambar 6')