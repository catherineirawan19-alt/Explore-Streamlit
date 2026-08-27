import streamlit as st

st.title("First Project")
st.header("Catherine")
st.subheader("26/08/2026")
st.text("Testing")
st.markdown("**Tebal**, *miring*, dan [link](https://streamlit.io)")
st.caption("Teks kecil, biasanya untuk keterangan")
st.code("print('Hello World')", language="python")
st.latex(r"E = mc^2")

# Menampilkan alert/status
st.success("Berhasil!")
st.info("Informasi")
st.warning("Peringatan")
st.error("Terjadi kesalahan")

# Menampilkan objek apa pun secara otomatis
st.write("Bisa teks, angka, dict, dataframe, dll:", {"a": 1, "b": 2})

st.markdown("==================================================================")

st.info("Please fill in the below form.")

nama = st.text_input("Masukkan nama")
umur = st.number_input("Umur", min_value=0, max_value=120, value=20)
tanggal = st.date_input("Pilih tanggal")
waktu = st.time_input("Pilih waktu")

setuju = st.checkbox("Saya setuju")
gender = st.radio("Jenis kelamin", ["Laki-laki", "Perempuan"])
kota = st.selectbox("Pilih kota", ["Jakarta", "Bandung", "Surabaya"])
hobi = st.multiselect("Pilih hobi", ["Membaca", "Olahraga", "Musik","Main Game"])
skor = st.slider("Skor kepuasan", 0, 100, 50)
rentang = st.slider("Rentang harga", 0, 1000, (200, 800))

tombol = st.button("Kirim")
if tombol:
    st.write(f"Halo {nama}, umur kamu {umur} tahun")

teks_panjang = st.text_area("Tulis pesan panjang")
file = st.file_uploader("Upload file")
warna = st.color_picker("Pilih warna", "#00f900")

st.markdown("=======================================================================")

st.title("Contoh Layout Streamlit")

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Produk A")
    st.write("Harga: Rp75.000")
    st.button("Beli A")
with col2:
    st.subheader("Produk B")
    st.write("Harga: Rp83.000")
    st.button("Beli B")
with col3:
    st.subheader("Produk C")
    st.write("Harga: Rp46.000")
    st.button("Beli C")

# Lebar kolom bisa diatur proporsinya
col1, col2 = st.columns([2, 1])  # kolom 1 dua kali lebih lebar


tab1, tab2 = st.tabs(["Ringkasan", "Detail"])
with tab1:
    st.write("Isi ringkasan")
with tab2:
    st.write("Isi detail")

with st.expander("Lihat detail lebih lanjut"):
    st.write("Ini konten yang tersembunyi secara default")

placeholder = st.empty()
placeholder.write("Ini akan diganti nanti")
placeholder.write("Sudah diganti!")

tombol1 = st.button("Klik")
if tombol1:
    placeholder.write("Sudah diklik!")

with st.container():
    st.write("Elemen dikelompokkan dalam satu container")

st.sidebar.title("Menu")
pilihan = st.sidebar.selectbox("Navigasi", ["Home", "About"])