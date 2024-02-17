#library yang dibutuhkan
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.cache_data


seller_df = pd.read_csv('sellers_dataset.csv') #seller dataset
items_df = pd.read_csv('order_items_dataset.csv') #items dataset
produk_df = pd.read_csv('products_dataset.csv') #produk dataset
review_df = pd.read_csv('order_reviews_dataset.csv') #reviews dataset
payment_df = pd.read_csv('order_payments_dataset.csv') #payment dataset
customer_df = pd.read_csv('customers_dataset.csv') #customer dataset
order_df = pd.read_csv('orders_dataset.csv') #order dataset

st.title("IF8-NUMPY")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Analisis Jumlah Seller","Analisis Kinerja Logistik","Analisis Kepuasan Produk","Analisis Preferensi Pembayaran","Analisis Kinerja Produk","Analisis Segmentasi Pelanggan"])
      
with tab1:
   st.header('Analisis Jumlah Seller') 
   st.write('10122295 - Dimas Adhi Negoro')
   with st.expander("Alasan Stretegis"):
      st.write("""
         - Pasar Potensial: Memperluas jangkauan konsumen dan meningkatkan penjualan.
         - Analisis Persaingan: Memahami tingkat persaingan dan merencanakan strategi pemasaran.
         - Tren Produk: Mengidentifikasi tren produk yang sedang populer di pasar.
         - Analisis Lokasi: Menentukan lokasi toko atau pusat distribusi yang strategis.
         - Peluang Kerja Sama: Membuka peluang kerja sama dengan penjual lokal dan mengembangkan jaringan bisnis yang lebih luas.  
            """)
   #---------------------------------------------------------------SOURCE CODE--------------------------------------------------------------------------------- 
   jumlah_seller = seller_df['seller_city'].value_counts()
   top5 = jumlah_seller.head(5)
   st.dataframe(top5)
   #--------------------------------------------------------------- VISUALISASI--------------------------------------------------------------------------------- 
   fig, ax = plt.subplots()
   ax.pie(x = top5.values, labels = top5.index, autopct= '%1.1f%%')
   ax.set_title('Top 5 Kota dengan Jumlah Sellers Terbanyak')
   st.pyplot(fig)
   with st.expander("Kesimpulan"):
      st.write("""
Mencari 5 kota dengan jumlah penjual terbanyak penting untuk memahami potensi pasar, tingkat persaingan, tren produk, analisis lokasi, dan peluang kerja sama. Informasi ini membantu bisnis untuk merancang strategi pemasaran yang efektif, menjangkau lebih banyak konsumen, dan mengembangkan bisnis dengan lebih baik. Dengan demikian, analisis ini dapat menjadi langkah strategis dalam pengembangan bisnis yang sukses.
      """)

with tab2:
   st.header('Alisis Kinerja Logistik') 
   st.write('10122277 - Sheli Maulida Salsiah')
   with st.expander("Alasan Strategis"):
      st.write("""
               Untuk memantau kinerja logistik mereka dari waktu ke waktu.
               Dengan melacak perubahan dalam rata rata freight value,
               perusahaan dapat mengidentifikasi tren atau pola yang mungkin 
               mempengaruhi efisiensi operasional mereka. 
            """) 
   #---------------------------------------------------------------SOURCE CODE---------------------------------------------------------------------------------
   #merge file item dataset dengan produk dataset untuk menemukan jumlah freight value serta produk yang diinginkan
   merge1 = pd.merge(items_df, produk_df,
                  on = 'product_id',
                  how = 'inner')
   #filter untuk kategori produk perfumaria
   hasil1 = merge1[merge1["product_category_name"] == 'perfumaria']
   #lakukan mean untuk mencari rata-rata freight value
   result1 = hasil1["freight_value"].mean(numeric_only = True)
   data = [[result1]]
   df1 = pd.DataFrame(data, columns=["hasil rata-rata freight value untuk produk parfum"], index=[""])
   #show
   st.dataframe(df1)
   #--------------------------------------------------------------- VISUALISASI--------------------------------------------------------------------------------- 
   dataframe1 = hasil1["freight_value"]
   fig, ax = plt.subplots()
   ax.hist(dataframe1, bins=20)
   ax.set_title('Perbandingan Freight Value')
   st.pyplot(fig)
   with st.expander("Kesimpulan"):
      st.write("""
Informasi ini memungkinkan perusahaan untuk beradaptasi dengan perubahan dalam biaya logistik, menyesuaikan strategi distribusi, dan mencari efisiensi dalam rantai pasok mereka. pentingnya analisis data dan pengambilan keputusan yang berbasis informasi dalam menjalankan bisnis yang sukses dan berkelanjutan.
      """)

with tab3:
   st.header('Analisis Kepuasan Produk') 
   st.write('10122306 - Natasya Farahdiva')
   with st.expander("Alasan Strategis"):
      st.write("""
         Mengetahui pemahaman tentang kepuasan pelanggan, Jumlah rating bintang 3 bisa 
         memberikan gambaran tentang kepuasan pelanggan. Ini mungkin menunjukkan bahwa 
         meskipun produk tersebut tidak dianggap sempurna, 
         masih ada kepuasan yang cukup signifikan. Jika banyak pelanggan memberi rating bintang 3,
         ini bisa menjadi pertanda bahwa ada ruang untuk perbaikan kualitas produk.
         Informasi ini dapat membantu dalam pengambilan keputusan, baik bagi pelanggan yang ingin membeli
         parfum maupun bagi pemilik bisnis yang ingin memperbaiki atau memperluas lini produk mereka.
          """)
   #---------------------------------------------------------------SOURCE CODE---------------------------------------------------------------------------------   
   #merge file item dataset dengan produk dataset untuk mengetahui kategori produk yang diingikan
   merge1 = pd.merge(items_df, produk_df,
                   on='product_id',
                   how='inner')
   #filter untuk kategori produk parfumaria
   hasil1 = merge1[merge1["product_category_name"]=="perfumaria"]
   #setelah itu merge hasil1 dengan review dataset
   merge2 = pd.merge(hasil1, review_df,
                   on='order_id',
                   how='inner')
   #setelah merge2 dilakukan, kita mencari rata-rata atau mean untuk produk parfum
   result2 = merge2["review_score"].mean(numeric_only=True)
   data = [[result2]]
   df2 = pd.DataFrame(data, columns=["Rata-rata score yang diberikan untuk product parfum"], index=[""])
   #show
   st.dataframe(df2)
   #--------------------------------------------------------------- VISUALISASI--------------------------------------------------------------------------------- 
   dataframe2 = merge2["review_score"]
   fig, ax = plt.subplots()
   ax.hist(dataframe2, bins=20)
   ax.set_title('Perbandingan Review Score')
   st.pyplot(fig)
   with st.expander("Kesimpulan"):
      st.write("""
Jadi, kesimpulannya, mengetahui jumlah rating bintang 3 pada penjualan parfum memberikan wawasan yang berharga tentang kepuasan pelanggan, kualitas produk, perbandingan dengan pesaing, dan membantu dalam pengambilan keputusan baik bagi pelanggan maupun pemilik bisnis.
      """)

with tab4:
   st.header('Analisis Preferensi Pembayaran') 
   st.write('10122310 - M.Fajar Satria Pamungkas')
   with st.expander("Alasan Strategis"):
      st.write("""
            Dengan memahami payment_type yang paling umum digunakan untuk membeli produk aksesoris, penjual dapat mengidentifikasi preferensi pembayaran pelanggan. Apakah mereka lebih suka menggunakan dompet digital, transfer antarbank, atau metode lainnya? Informasi ini membantu penjual mengarahkan upaya pemasaran dan mengoptimalkan pengalaman pembayaran.
                """)
   #---------------------------------------------------------------SOURCE CODE---------------------------------------------------------------------------------  
   #merge produk dataset dengan items dataset untuk mengetahui kategori produk yang diingikan
   merge1 = pd.merge(produk_df, items_df,
                  on = 'product_id',
                  how = 'inner')
   #filter untuk kategori produk informatica_acessorios
   hasil1 = merge1[merge1["product_category_name"]=='informatica_acessorios']
   #merge hasil1 dengan payment dataset 
   merge2 = pd.merge(hasil1, payment_df,
                     on = 'order_id',
                     how = 'inner')
   #bautkan group untuk kolom payment_type
   group_make = merge2.groupby('payment_type').size()
   #buatkan dataframe baru
   df_tot = pd.DataFrame(group_make).reset_index()
   df_tot = df_tot.rename(columns={0: 'total'})
   st.dataframe(df_tot)
   #--------------------------------------------------------------- VISUALISASI--------------------------------------------------------------------------------- 
   total = df_tot["total"]
   payment_type = df_tot["payment_type"]
   fig, ax = plt.subplots()
   ax.pie(total, labels=payment_type, autopct='%1.1f%%')
   ax.set_title('Perbandingan Payment_type untuk Produk Kategori Aksesoris Komputer')
   st.pyplot(fig)
   with st.expander("Kesimpulan"):
      st.write("""
Berdasarkan analisis data, mayoritas pembeli produk aksesoris komputer menggunakan credit card sebagai metode pembayaran. boleto juga populer. Penjual dapat memanfaatkan informasi ini untuk mengoptimalkan strategi pemasaran dan pengelolaan pembayaran. Namun, perlu diingat bahwa data lebih lanjut dan analisis mendalam diperlukan untuk mengambil keputusan yang lebih akurat. 
      """)

with tab5:
   st.header('Alisisis Kinerja Produk') 
   st.write('10122297 - Dewa Ayu Sekar Purnama Devi')
   with st.expander("Alasan Strategis"):
      st.write("""
- Pengambilan Keputusan Bisnis yang Lebih Baik: Informasi tentang kategori-kategori teratas pembayaran dengan kartu kredit dapat membantu pemilik atau manajer toko membuat keputusan yang lebih baik dalam merencanakan stok barang dan strategi pemasaran
- Penyesuaian Penawaran dan Promosi: Dengan mengetahui kategori-kategori pembelian yang paling umum dilakukan dengan kartu kredit, toko dapat menyesuaikan penawaran, diskon, dan promosi untuk mencocokkan preferensi pembelian pelanggan.
- Analisis Kinerja Produk: Data tentang kategori-kategori pembelian tertinggi dapat memberikan wawasan tentang kinerja produk tertentu di toko tersebut.⁠
- Optimalisasi Program Penghargaan: Jika toko tersebut memiliki program loyalitas atau program penghargaan untuk pelanggan yang menggunakan kartu kredit tertentu, mengetahui kategori-kategori pembelian yang paling umum dapat membantu mereka mengoptimalkan program tersebut.
- ⁠Peningkatan Pengalaman Pelanggan: Dengan memahami preferensi pembelian pelanggan, toko dapat meningkatkan pengalaman belanja mereka dengan menyediakan produk dan layanan yang lebih sesuai dengan kebutuhan dan keinginan mereka.
                  """) 
   #---------------------------------------------------------------SOURCE CODE---------------------------------------------------------------------------------  
   #merge payment dataset dengan items dataset untuk mengetahui produk id yang menggunakan payment_type tertentu
   merge1 = pd.merge(payment_df, items_df,
                     on = 'order_id',
                     how = 'inner')
   #filter kolom payment_type dengan hasil credit card
   hasil1 = merge1[merge1["payment_type"]=='credit_card']
   #merge hasil1 dan produk dataset untuk mengetahui kategori produk apa saja yang melakukan transaksi menggunakan credit card
   #proses merge
   merge2 = pd.merge(hasil1, produk_df,
                     on = 'product_id',
                     how = 'inner')
   #menghitung jumlah setiap kategori produk yang melakukan pembayaran menggunakan credit card
   df = merge2["product_category_name"].value_counts()
   #tampilkan 5 teratas
   top_5 = df.head(5)
   st.dataframe(top_5)
   #--------------------------------------------------------------- VISUALISASI--------------------------------------------------------------------------------- 
   fig, ax = plt.subplots()
   ax.pie(x = top_5.values, labels= top_5.index, autopct= '%1.1f%%')
   ax.set_title('5 Kategori Teratas Dengan Payments Credit Cards')
   st.pyplot(fig)
   with st.expander("Kesimpulan"):
      st.write("""
Secara keseluruhan, mencari tahu lima kategori teratas yang mendapatkan pembayaran dengan kartu kredit dalam sebuah toko memberikan manfaat besar bagi pemilik atau manajer toko dalam mengelola bisnis mereka dengan lebih efektif. Dengan pemahaman yang lebih baik tentang preferensi pembelian pelanggan, mereka dapat mengambil keputusan bisnis yang lebih cerdas, menyesuaikan penawaran dan promosi, menganalisis kinerja produk, mengoptimalkan program loyalitas, dan meningkatkan pengalaman pelanggan secara keseluruhan. Ini semua bertujuan untuk meningkatkan penjualan, membangun loyalitas pelanggan, dan memperkuat posisi toko dalam pasar.
      """)

with tab6:
   st.header('Alisisis Segmentasi Pelanggan') 
   st.write('10122287 - Naufal Fahrezi Maulana')
   with st.expander("Alasan Strategis"):
      st.write("""
 Perbandingan ini juga dapat membantu dalam segmentasi pelanggan. Apakah ada perbedaan dalam preferensi produk antara pelanggan dari São Paulo dan Franca? Informasi ini dapat membantu penjual mengarahkan upaya pemasaran dengan lebih efektif.
               """) 
   #---------------------------------------------------------------SOURCE CODE---------------------------------------------------------------------------------
   #Pastikan 'seller_id' ada di seller dataset dan items dataset
   if 'seller_id' in seller_df.columns and 'seller_id' in items_df.columns:
      #Proses merge
      merge1 = pd.merge(seller_df, items_df, on='seller_id', how='inner')
   else:
      print("Kolom 'seller_id' tidak ditemukan di salah satu DataFrame.")   
   #filter untuk seller city berasal dari franca
   hasil1 = merge1[merge1["seller_city"] == 'franca']     
   #merge customer dataset dengan order dataset untuk mengetahui customer city dari sao paulo
   #proses merge
   merge2 = pd.merge(order_df, customer_df,
                     on = 'customer_id',
                     how = 'inner')
   #filtering data by value
   hasil2 = merge2[merge2["customer_city"]=='sao paulo']
   #merge hasil1 dan hasil2 untuk menemukan transaksi yang terjadi dari seller city franca dengan customer city sao paulo
   #proses merge
   merge3 = pd.merge(hasil1, hasil2,
                     on = 'order_id',
                     how = 'inner')
   #merge merge3 dengan product dataset untuk mencari tahu perbandingan barang yg dibeli
   #proses merge
   merge4 = pd.merge(merge3, produk_df,
                     on ='product_id',
                     how = 'inner')
   #hitung jumlah untuk setiap kategori produk
   hasil = merge4['product_category_name'].value_counts()
   st.dataframe(hasil)
   #--------------------------------------------------------------- VISUALISASI--------------------------------------------------------------------------------- 
   fig, ax = plt.subplots()
   ax.pie(x = hasil.values, labels= hasil.index, autopct= '%1.1f%%')
   ax.set_title('Perbandingan Produk per Kategori')
   st.pyplot(fig)
   with st.expander("Kesimpulan"):
      st.write("""
Berdasarkan analisis data, kita dapat menyimpulkan bahwa perbandingan produk antara pelanggan dari São Paulo dan penjual dari Franca memiliki dampak signifikan pada strategi penjualan dan pengelolaan stok. Penjual perlu memahami preferensi pelanggan di kedua lokasi dan menyesuaikan produk serta harga sesuai dengan kebutuhan pasar. 
      """)   
