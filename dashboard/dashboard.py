import streamlit as st 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.write(
    """
    Bike Sharing
    """
)

df = pd.read_csv('../data/day.csv')

df['season'] = df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
df['weathersit'] = df['weathersit'].map({1: 'Clear', 2: 'Cloudy/Mist', 3: 'Light Snow/Rain', 4: 'Heavy Rain/Snow'})

# Menyiapkan halaman utama presentasi
st.sidebar.title("Menu Navigasi")
menu = st.sidebar.radio("Pilih bagian yang ingin ditampilkan:", ["Kesimpulan",
"Rata-Rata Layanan Casual dan Registered", 
"Rata-rata Penggunaan Sepeda Berdasarkan Hari dalam Seminggu",
"Distribusi Cuaca", 
"Distribusi Musim", 
"Rekomendasi Bisnis"])

# Menampilkan kesimpulan analisis di halaman utama
if menu == "Kesimpulan":
    st.title("Hasil Analisis Penggunaan Layanan Peminjaman Sepeda")
    st.header("Kesimpulan")
    st.markdown("""
    1. **Pengaruh Cuaca Terhadap Penggunaan**: Kondisi cuaca cerah mendominasi penggunaan layanan sepeda baik oleh pelanggan casual maupun registered.
    2. **Pengaruh Musim Terhadap Penggunaan**: Musim gugur merupakan musim dengan jumlah pelanggan tertinggi untuk casual dan registered.
    3. **Konsistensi Pengguna Casual**: Pengguna casual menunjukkan pola penggunaan yang tidak konsisten setiap hari di semua kondisi cuaca maupun di semua musim.
    4. **Konsistensi Pengguna Registered**: Pengguna registered menggunakan layanan dengan konsisten setiap hari di berbagai kondisi cuaca dan musim.
    5. **Perbedaan Penggunaan Berdasarkan Hari**: Pengguna casual lebih sering menggunakan sepeda pada akhir pekan, sementara pengguna registered lebih dominan pada hari kerja.
    """)

elif menu == "Rata-Rata Layanan Casual dan Registered":
    st.title("Rata-Rata Layanan Casual dan Registered Berdasarkan Kondisi Cuaca dan Musim ")
    weather_usage = df.groupby('weathersit')[['casual', 'registered']].mean().reset_index()
    weather_usage_melt = weather_usage.melt(id_vars='weathersit', value_vars=['casual', 'registered'], 
                                        var_name='user_type', value_name='usage')
    fig, ax = plt.subplots(1, 2, figsize=(15, 6))
    sns.barplot(x='weathersit', y='usage', hue='user_type', data=weather_usage_melt, palette='coolwarm', ax=ax[0])
    ax[0].set_title("Rata-rata Penggunaan Casual dan Registered Berdasarkan Kondisi Cuaca")
    ax[0].set_xlabel("Kondisi Cuaca")
    ax[0].set_ylabel("Rata-rata Penggunaan")
    ax[0].legend(title="Tipe Pengguna")

    season_usage = df.groupby('season')[['casual', 'registered']].mean().reset_index()

    season_usage_melt = season_usage.melt(id_vars='season', value_vars=['casual', 'registered'], 
                                      var_name='user_type', value_name='usage')
    sns.barplot(x='season', y='usage', hue='user_type', data=season_usage_melt, palette='coolwarm',ax=ax[1])
    ax[1].set_title("Rata-rata Penggunaan Casual dan Registered Berdasarkan Kondisi Musim")
    ax[1].set_xlabel("Musim")
    ax[1].set_ylabel("Rata-rata Penggunaan")
    ax[1].legend(title="Tipe Pengguna")

    st.pyplot(fig)


elif menu == "Rata-rata Penggunaan Sepeda Berdasarkan Hari dalam Seminggu":
    st.title("Rata-rata Penggunaan Sepeda Berdasarkan Hari dalam Seminggu")
    weekday_usage = df.groupby('weekday')[['casual', 'registered']].mean().reset_index()
    fig, ax = plt.subplots(1, 2, figsize=(15, 6))
    sns.barplot(x='weekday', y='casual', data=weekday_usage, hue='weekday', palette='coolwarm', legend=False, ax=ax[0])
    ax[0].set_title('Casual')
    ax[0].set_xlabel('Hari dalam Seminggu')
    ax[0].set_ylabel('Total Penggunaan (Rata-rata)')
    
    sns.barplot(x='weekday', y='registered', data=weekday_usage, hue='weekday', palette='coolwarm', legend=False, ax=ax[1])
    ax[1].set_title('Registered')
    ax[1].set_xlabel('Hari dalam Seminggu')
    ax[1].set_ylabel('Total Penggunaan (Rata-rata)')
    



    st.pyplot(fig)
# Distribusi penggunaan berdasarkan cuaca
elif menu == "Distribusi Cuaca":
    st.title("Distribusi Penggunaan Berdasarkan Cuaca")
    
    # Membuat visualisasi distribusi cuaca
    fig, ax = plt.subplots(1, 2, figsize=(15, 6))
    
    sns.boxplot(x='weathersit', y='casual', data=df, ax=ax[0], palette='Blues')
    ax[0].set_title('Distribusi Penggunaan Casual Berdasarkan Cuaca')
    ax[0].set_xlabel('Kondisi Cuaca')
    ax[0].set_ylabel('Jumlah Penggunaan Casual')
    
    sns.boxplot(x='weathersit', y='registered', data=df, ax=ax[1], palette='Greens')
    ax[1].set_title('Distribusi Penggunaan Registered Berdasarkan Cuaca')
    ax[1].set_xlabel('Kondisi Cuaca')
    ax[1].set_ylabel('Jumlah Penggunaan Registered')
    
    st.pyplot(fig)

# Distribusi penggunaan berdasarkan musim
elif menu == "Distribusi Musim":
    st.title("Distribusi Penggunaan Berdasarkan Musim")
    
    # Membuat visualisasi distribusi musim
    fig, ax = plt.subplots(1, 2, figsize=(15, 6))
    
    sns.boxplot(x='season', y='casual', data=df, ax=ax[0], palette='Blues')
    ax[0].set_title('Distribusi Penggunaan Casual Berdasarkan Musim')
    ax[0].set_xlabel('Musim')
    ax[0].set_ylabel('Jumlah Penggunaan Casual')
    
    sns.boxplot(x='season', y='registered', data=df, ax=ax[1], palette='Greens')
    ax[1].set_title('Distribusi Penggunaan Registered Berdasarkan Musim')
    ax[1].set_xlabel('Musim')
    ax[1].set_ylabel('Jumlah Penggunaan Registered')
    
    st.pyplot(fig)

# Menampilkan rekomendasi bisnis
elif menu == "Rekomendasi Bisnis":
    st.title("Rekomendasi Bisnis")
    st.markdown("""
    - **Promosi Musiman**: Menawarkan promosi spesial selama musim gugur dapat meningkatkan penggunaan lebih lanjut, terutama bagi pengguna casual.
    - **Program Loyalitas**: Untuk meningkatkan konsistensi pengguna casual, program loyalitas atau insentif pada hari kerja atau cuaca yang tidak terlalu cerah dapat merangsang penggunaan yang lebih stabil.
    - **Segmentasi Pengguna**: Menyusun strategi pemasaran yang berbeda untuk pengguna casual dan registered, misalnya promosi akhir pekan untuk casual dan program berlangganan bulanan untuk registered.
    """)