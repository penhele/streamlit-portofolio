import streamlit as st

st.set_page_config(page_title="Portofolio Stephen", page_icon="🙍🏻", layout="wide")

# function css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

with st.container():
    st.subheader("Hi, Saya Stephen Helenus :wave:")
    st.title("Mahasiswa Gunadarma - Angkatan 2022")
    st.write("Seorang manusia yang setiap hari duduk di depan laptop dan mengetik sebuah kode.")

with st.container():
    st.divider()
    st.header("Tentang Stephen")

    left_column, right_column = st.columns(2)

    with left_column:
        st.subheader("Universitas Gunadarma")
        st.write('''
            - Asisten Laboratorium Komputer (LePKom)
            - Anggota Komunitas KSPM (Kelompok Studi Pasar Modal)
            - Finalis Kategori Live Coding Kompetisi Kreativitas Pembuatan Software (KOMPRES 15)
            - Finalis divisi Competitive Programming yang diadakan Gunadarma I/O
            - Pecinta Android 
        ''')

    with right_column:
        st.subheader('Cerita Singkat')
        st.write('''
            Saya adalah mahasiswa aktif Universitas Gunadarma, jurusan Informatika angkatan 2022. 
            Setelah 2 tahun berkuliah, saya menemukan tujuan saya mengetik kode program selama ini, yaitu berminat karir sebagai Android Developer. 
            \n\n
            Saya tidak hanya aktif di kuliah, saya juga aktif dalam komunitas gereja, contohnya menjadi panitia acara besar gereja (Natal, Paskah, dll).
        ''')


with st.container():
    st.divider()

    st.title('Informasi')
    st.subheader('Hubungi saya melalui:')

    st.write("""
        - [Linkedin](https://www.linkedin.com/in/stephen-helenus-ruswanto-kaawoan-09907023b/)
        - [Instagram](https://www.instagram.com/stephenhelenus)
    """)

    st.subheader('Terima kasih :wave:')
