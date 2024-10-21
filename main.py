import streamlit as st
import webbrowser

st.set_page_config(page_title="Portofolio Stephen", page_icon="🙍🏻", layout="wide")

# function css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

with st.container():
    left_column, right_column = st.columns(2)

    with left_column:
        st.subheader("Hi, Saya Stephen Helenus :wave:")
        st.title("Mahasiswa Gunadarma - Angkatan 2022")
        st.write("Seorang manusia yang setiap hari duduk di depan laptop dan mengetik sebuah kode.")

    with right_column:
        st.image('image/stephen.jpg')

with st.container():
    st.divider()
    st.header("Tentang Stephen")

    st.write('''
        Saya adalah mahasiswa aktif Universitas Gunadarma, jurusan Informatika angkatan 2022. 
        Setelah 2 tahun berkuliah, saya menemukan tujuan saya mengetik kode program selama ini, yaitu berminat karir sebagai Android Developer. 
        Saya tidak hanya aktif di kuliah, saya juga aktif dalam komunitas gereja, contohnya menjadi panitia acara besar gereja (Natal, Paskah, dll).
    ''')

with st.container():
    st.divider()
    left_column, right_column = st.columns(2)

    with left_column:
        st.header("Edukasi")

        st.subheader('SMA (Katolik) Paskalis')
        st.write('2019 - 2022')
        st.write('Pernah menjadi anggota OSIS (Organisasi Siswa Intra Sekolah) bagian Kesegaran Jasmani dan Data Kreasi.')

        st.subheader('Universitas Gunadarma')
        st.write('2022 - Sekarang')

    with right_column:
        st.header('Pengalaman')

        st.write('''
            - Asisten Laboratorium LePKom | 2023 - Sekarang
            - Tim inti Kelompok Studi Pasar Modal (KSPM) | 2023 - 2024
            - Asisten Research Doctoral - Gunadarma | 2024
            - Partisipan lomba Hackfest - GDSC | 2024
            - Partisipan lomba Gemastik (Div. Competitive Programming) | 2023
            - Partisipan lomba Gemastik (Div. UX) | 2024 
            - Partisipan Samsung Innovation Campus | 2024
            - Partisipan lomba Infinity (HIMTI UG) | 2024
            - Finalis Comp. Programming - Kompress | 2024
            - Finalis Comp. Programming - Gunadarma I/O | 2024
            - Pembicara Sosialisasi KSPM di PKKMB | 2024
            - Volunteer - Bazaar Mupel Jakarta Pusat | 2024
        ''')

with st.container():
    st.divider()

    st.header('Projek')

    # 7MinutesWorkout
    st.write('- [7MinutesWorkout](minutesworkout)')
    st.write('7MinutesWorkout adalah aplikasi Android yang saya buat. Meski saya dipandu dalam kursus yang saya beli di platform kursus berbayar, yaitu Udemy, saya sangat banyak belajar dari kursus tersebut.')
    st.write('7MinutesWorkout adalah aplikasi workout yang di mana hanya dilakukan selama 7 menit saja. Terdapat 12 gerakan yang tersedia dan masing-masing gerakan hanya diwaktui selama 30 detik.')

    # TeNaR
    st.write('- [TeNaR](https://tenar.vercel.app)')
    st.write('TeNaR adalah singkatan dari Teruna Maranatha Bersinar. TeNaR adalah sebutan untuk remaja di dalam Gereja GPIB Maranatha Jakarta. Tujuan saya membuat website tersebut adalah memudahkan pengguna (TeNaR maupun orang tua) mendapatkan informasi tanpa berinteraksi dengan pengurus remaja.')

    if st.button('TeNaR'):
        webbrowser.open_new_tab('https://tenar.vercel.app')

    # neTure
    st.write('- [neTure](neture)')
    st.write('neTure adalah aplikasi yang kami buat untuk lomba Gemastik Div. UX dan Hackfest 2024. Kami beranggotakan 4 orang, yaitu: Zaki, Felix, Wiefran, dan Stephen. Aplikasi ini masih berbasis UI/UX, belum diimplementasikan ke dalam mobile maupun web. Meski belum berhasil lolos, kami tetap konsisten mengembangkan aplikasi kami.')




with st.container():
    st.divider()

    st.title('Informasi')
    st.subheader('Hubungi saya melalui:')

    st.write("""
        - [Linkedin](https://www.linkedin.com/in/stephen-helenus-ruswanto-kaawoan-09907023b/)
        - [Instagram](https://www.instagram.com/stephenhelenus)
        - [Github](https://github.com/penhele)
    """)

    st.subheader('Terima kasih :wave:')
