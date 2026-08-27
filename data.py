import streamlit as st
import pandas as pd
import numpy as np

st.title("Latihan Streamlit: Data Display")

df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["A", "B", "C"]
)

st.subheader("1. Interactive Dataframe")
st.dataframe(df, use_container_width=True)

st.subheader("2. Static Table")
st.table(df)

st.subheader("3. JSON")
st.json({
    "nama": "Budi",
    "umur": 25
})

# Metric untuk KPI

st.subheader("4. KPI Metrics")

col1, col2, col3 = st.columns(3)
col1.metric("Penjualan", "Rp 12jt", "+8%")
col2.metric("Pengguna Aktif", "1.204", "-2%")
col3.metric("Konversi", "3.2%", "0.1%")

# Styling dataframe
st.subheader("5. Styled Dataframe")
st.write("Nilai terbesar pada setiap kolom ditandai.")

st.dataframe(df.style.highlight_max(axis=0),
use_container_width=True)

st.subheader("6. Visualisasi Data")

st.write("Grafik garis")
st.line_chart(df)

st.write("Grafik batang")
st.bar_chart(df)

st.write("Grafik area")
st.area_chart(df)

st.write("Scatter plot: Kolom A vs B")
st.scatter_chart(df, x="A", y="B")

st.subheader("7. Matplotlib")
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.hist(df["A"], bins=20)

st.pyplot(fig)

st.subheader("8. Plotly (interaktif, direkomendasikan untuk dashboard)")

import plotly.express as px

fig = px.scatter(df, x="A", y="B", color="C", title="Contoh Scatter Plot")
st.plotly_chart(fig, use_container_width=True)

st.subheader("9. Peta (map)")

peta_df = pd.DataFrame({
    "kota": ["Jakarta","Bandung","Yogyakarta"],
    "lat": [-6.2, -6.9, -7.8],
    "lon": [106.8, 107.6, 110.4]
})

st.dataframe(peta_df)

st.map(peta_df)

st.subheader("10. session state")

if "counter" not in st.session_state:
    st.session_state.counter = 0

def tambah():
    st.session_state.counter += 1

st.button("Tambah", on_click=tambah)
st.write("Nilai counter:", st.session_state.counter)

st.write("Contoh: To-do list sederhana")
if "tasks" not in st.session_state:
    st.session_state.tasks = []

tugas_baru = st.text_input("Tugas baru")
if st.button("Tambah Tugas") and tugas_baru:
    st.session_state.tasks.append(tugas_baru)

for i, t in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([4, 1])
    col1.write(f"{i+1}. {t}")
    if col2.button("Hapus", key=f"hapus_{i}"):
        st.session_state.tasks.pop(i)
        st.rerun()

st.subheader("11. FORM & VALIDASI INPUT")

with st.form("form_registrasi"):
    nama = st.text_input("Nama Lengkap")
    email = st.text_input("Email")
    umur = st.number_input("Umur", min_value=0)
    submit = st.form_submit_button("Daftar")

if submit:
    if not nama or not email:
        st.error("Nama dan email wajib diisi")
    elif "@" not in email:
        st.error("Format email tidak valid")
    else:
        st.success(f"Pendaftaran berhasil untuk {nama}")

st.subheader("12. UPLOAD & DOWNLOAD FILE")


# Upload
file = st.file_uploader("Upload CSV", type=["csv"])
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df)

# Upload banyak file
files = st.file_uploader("Upload beberapa gambar", type=["png", "jpg"], accept_multiple_files=True)
for f in files or []:
    st.image(f)

# Download
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download CSV",
    data=csv,
    file_name="hasil.csv",
    mime="text/csv"
)
