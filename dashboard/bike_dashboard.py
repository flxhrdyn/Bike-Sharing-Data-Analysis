# import library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set_theme(style='dark')

# function untuk menyiapkan dataframe weathersit_max
def create_weathermax(df):
    weathersit_max = df.groupby(by="weathersit_d").agg({
    "cnt_d": "max",
    })
    return weathersit_max

# function untuk menyiapkan dataframe holiday_max
def create_holidaymax(df):
    holiday_max = df.groupby(by="holiday_d").agg({
    "cnt_d": "max",
    })
    return holiday_max

# function untuk menyiapkan dataframe reg_hour
def create_reghour(df):
    reg_hour = df.groupby(by="hr").agg({
    "registered_h": "mean",
    })
    return reg_hour

# read file csv
all_df = pd.read_csv("alldf_clean.csv")

# memanggil helper function
weathersit_max = create_weathermax(all_df)
holiday_max = create_holidaymax(all_df)
reg_hour = create_reghour(all_df)

# Judul Web app
st.title("Bike Sharing Dashboard :bike:")

# Judul chart cuaca
st.subheader("Dampak Cuaca Terhadap Sepeda yang Dipinjam")

# Metric berisi count max tiap cuaca
col1, col2, col3= st.columns(3)
with col1:
    st.metric(label="Cerah", value=weathersit_max.cnt_d[1].max())
with col2:
    st.metric(label="Berawan/Berkabut", value=weathersit_max.cnt_d[2].max())
with col3:
    st.metric(label="Hujan Gerimis", value=weathersit_max.cnt_d[3].max())

# Membuat chart Cuaca
fig = plt.figure(figsize=(10, 8))
colors = ["#526D82", "#9DB2BF", "#9DB2BF"]
sns.barplot(
    y="weathersit_d",
    x="cnt_d",
    orient="h",
    data=weathersit_max,
    palette=colors
)
plt.xlabel("Jumlah sepeda yang dipinjam")
plt.ylabel("Cuaca")
plt.title("Dampak Cuaca Terhadap Jumlah Sepeda Yang Dipinjam")
plt.yticks([0, 1, 2], ["Cerah", "Berawan/Berkabut", "Hujan Gerimis"])
st.pyplot(fig)

# Judul chart holiday
st.subheader("Sepeda yang Dipinjam Antara Hari Biasa dan Hari Libur")

# Metric count max holiday
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Hari Biasa", value=holiday_max.cnt_d[0].mean())
with col2:
    st.metric(label="Hari Libur", value=holiday_max.cnt_d[1].mean())

fig = plt.figure(figsize=(10, 7))
colors = ["#526D82", "#9DB2BF"]
sns.barplot(
    x="holiday_d",
    y="cnt_d",
    data=holiday_max,
    palette=colors
)
plt.xlabel("Hari")
plt.ylabel("Jumlah Sepeda yang dipinjam")
plt.title("Volume Maks Sepeda yang Dipinjam Antara Hari Biasa dan Hari Libur")
plt.xticks([0, 1], ["Hari biasa", "Hari libur"])
st.pyplot(fig)

# Judul rata-rata pengguna terdaftar
st.subheader("Rata-rata Pengguna Sepeda yang terdaftar Setiap Jamnya")

# Chart rata-rata pengguna terdaftar
fig = plt.figure(figsize=(8, 5.5))
colors = ["#526D82"]
sns.barplot(
    x="hr",
    y="registered_h",
    data=reg_hour,
    hue="hr",
    palette=colors*24,
    legend=False
)
plt.xlabel("Jam")
plt.ylabel("Jumlah pengguna yang mendaftar")
plt.title("Rata-rata Pengguna Sepeda yang terdaftar Setiap Jamnya")
st.pyplot(fig)