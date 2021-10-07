import streamlit as st
import pandas as pd
import numpy as np
import plotly_express as px
from PIL import Image

# load model 
import joblib

def main():
    """App with Streamlit"""
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.set_page_config(layout="wide")
    st.title("PROJECT PJJ DA DJPb BATCH II : Analisis Proyeksi Indikator Makro")
    
    menu = ['Pilih Menu','Model Evaluation','Correlation Matrix','Prediksi Inflasi','Prediksi USD','Prediksi Oil_Price','Prediksi CCI']
    pjjda= Image.open('Projectdaputih1.png')
    data= Image.open('Sidebar_trans.png')
    st.sidebar.image(pjjda)
    st.sidebar.image(data)
    #st.sidebar.image(klp)
    
    choice = st.sidebar.selectbox("Select Menu", menu)
    C1, C2, C3, C4 = st.columns((2,2,2,2))
    if choice == "Pilih Menu":
        st.subheader("Presented by")
        me=Image.open('kelompok.png')
        st.image(me)
    if choice == "Model Evaluation":
        st.subheader("Model Evaluation")
        me=Image.open('Model_Evaluation.png')
        st.image(me)
    if choice == "Correlation Matrix":
        st.subheader("Correlation Matrix")
        cm=Image.open('correlation_matrix.png')
        st.image(cm)
    if choice == "Prediksi Inflasi":
        #df = pd.read_excel('DataFrame_h7.xlsx')
        st.subheader("Prediksi Inflasi")
        model= open("inflasi_model_final_deploy.pkl", "rb")
        inflasi=joblib.load(model)
        with C1 :
            st.subheader("Asumsi Nilai Belanja")
            a = st.number_input(label="5111 Belanja Gaji dan Tunjangan PNS",value=1000000000.0, min_value=0.0)
            b = st.number_input(label="5112 Belanja Gaji dan Tunjangan TNI/Polri",value=1000000000.0, min_value=0.0)
            c = st.number_input(label="5113 Belanja Gaji dan Tunjangan Pejabat Negara",value=1000000000.0, min_value=0.0)
            d = st.number_input(label="5114 Belanja Gaji Dokter PTT",value=1000000000.0, min_value=0.0)
            e = st.number_input(label="5115 Belanja Gaji dan Tunjangan Pegawai Non PNS",value=1000000000.0, min_value=0.0)
            f = st.number_input(label="5121 Belanja Honorarium",value=1000000000.0, min_value=0.0)
            g = st.number_input(label="5122 Belanja Lembur",value=1000000000.0, min_value=0.0)
            h = st.number_input(label="5124 Bel. Tunjangan Khusus & Bel. Pegawai Transito",value=1000000000.0, min_value=0.0)
            i = st.number_input(label="5131 Belanja Pensiun dan Uang Tunggu",value=1000000000.0, min_value=0.0)
        with C2 :   
            st.subheader("")
            st.subheader("")
            j = st.number_input(label="5132 Belanja Program Jaminan Sosial Pegawai",value=1000000000.0, min_value=0.0)
            k = st.number_input(label="5211 Belanja Barang Operasional",value=1000000000.0, min_value=0.0)
            l = st.number_input(label="5212 Belanja Barang Non Operasional",value=1000000000.0, min_value=0.0)
            m = st.number_input(label="5215 Belanja Barang Pengganti Pajak Dalam Rangka Hibah MCC",value=1000000000.0, min_value=0.0)
            n = st.number_input(label="5217 Belanja Kontribusi",value=1000000000.0, min_value=0.0)
            o = st.number_input(label="5218 Belanja Barang Persediaan",value=1000000000.0, min_value=0.0)
            p = st.number_input(label="5221 Belanja Jasa",value=1000000000.0, min_value=0.0)
            q = st.number_input(label="5231 Belanja Pemeliharaan",value=1000000000.0, min_value=0.0)
            r = st.number_input(label="5241 Belanja Perjalanan Dinas Dalam Negeri",value=1000000000.0, min_value=0.0)
        with C3 :   
            st.subheader("")
            st.subheader("")
            s = st.number_input(label="5242 Belanja Perjalanan Dinas Luar Negeri",value=1000000000.0, min_value=0.0)
            t = st.number_input(label="5251 Belanja Barang BLU",value=1000000000.0, min_value=0.0)
            u = st.number_input(label="5261 Belanja Barang untuk Diserahkan kepada Masyarakat/Pemda",value=1000000000.0, min_value=0.0)
            v = st.number_input(label="5262 Belanja Brg Fisik dan Penunjang Dana DK dan TP utk Diserahkan kpd Pemda",value=1000000000.0, min_value=0.0)
            w = st.number_input(label="5263 Belanja Brg Lainnya untuk diserahkan kepada masy./Pemda",value=1000000000.0, min_value=0.0)
            x = st.number_input(label="5271 Belanja Brg utk Diserahkan kpd Mantan Presiden dan/atau Mantan WaPres",value=1000000000.0, min_value=0.0)
            z = st.number_input(label="5311 Belanja Modal Tanah",value=1000000000.0, min_value=0.0)
            aa = st.number_input(label="5321 Belanja Modal Peralatan dan Mesin",value=1000000000.0, min_value=0.0)
            bb = st.number_input(label="5331 Belanja Modal Gedung dan Bangunan",value=1000000000.0, min_value=0.0)
        with C4 :    
            st.subheader("")
            st.subheader("")
            cc = st.number_input(label="5341 Belanja Modal Jalan, Irigasi dan Jaringan",value=1000000000.0, min_value=0.0)
            dd = st.number_input(label="5361 Belanja Modal Lainnya",value=1000000000.0, min_value=0.0)
            ee = st.number_input(label="5371 Belanja Modal BLU",value=1000000000.0, min_value=0.0)
            ff = st.number_input(label="5711 Belanja Bantuan Sosial Untuk Rehabilitasi Sosial",value=1000000000.0, min_value=0.0)
            gg = st.number_input(label="5721 Belanja Bantuan Sosial Untuk Jaminan Sosial",value=1000000000.0, min_value=0.0)
            hh = st.number_input(label="5731 Belanja Bantuan Sosial Untuk Pemberdayaan Sosial",value=1000000000.0, min_value=0.0)
            ii = st.number_input(label="5741 Belanja Bantuan Sosial Untuk Perlindungan Sosial",value=1000000000.0, min_value=0.0)
            jj = st.number_input(label="5751 Belanja Bantuan Sosial Untuk Penanggulangan Kemiskinan",value=1000000000.0, min_value=0.0)
            y = st.number_input(label="5761 Belanja Bantuan Sosial Untuk Penanggulangan Bencana",value=1000000000.0, min_value=0.0)
                
        if st.button("Klik untuk Mendapatkan Prediksi"):
            dfvalues = pd.DataFrame(list(zip([a],[b],[c],[d],[e],[f],[g],[h],[i],[j],[k],[l],[m],[n],[o],[p],[q],[r],[s],[t],[u],[v],[w],[x],[y],[z],[aa],[bb],[cc],[dd],[ee],[ff],[gg],[hh],[ii],[jj])),columns =['5111','5112','5113','5114','5115','5121','5122','5124','5131','5132','5211','5212','5215','5217','5218','5221','5231','5241','5242','5251','5261','5262','5263','5271','5311','5321','5331','5341','5361','5371','5711','5721','5731','5741','5751','5761'])
            input_variables = np.array(dfvalues[['5111','5112','5113','5114','5115','5121','5122','5124','5131','5132','5211','5212','5215','5217','5218','5221','5231','5241','5242','5251','5261','5262','5263','5271','5311','5321','5331','5341','5361','5371','5711','5721','5731','5741','5751','5761']])
            prediction = inflasi.predict(input_variables)
            nilai = np.mean(prediction)
            nilai = (nilai)*100
            st.title(f"Prediksi: {nilai:.2f} Persen")
    if choice == "Prediksi USD":
        st.subheader("Prediksi Kurs USD")
        #df = pd.read_excel('DataFrame_h7.xlsx')

        model= open("USD_model_final_deploy.pkl", "rb")
        USD=joblib.load(model)

        with C1 :
            st.subheader("Asumsi Nilai Belanja")
            a = st.number_input(label="5111 Belanja Gaji dan Tunjangan PNS",value=1000000000.0, min_value=0.0)
            b = st.number_input(label="5112 Belanja Gaji dan Tunjangan TNI/Polri",value=1000000000.0, min_value=0.0)
            c = st.number_input(label="5113 Belanja Gaji dan Tunjangan Pejabat Negara",value=1000000000.0, min_value=0.0)
            d = st.number_input(label="5114 Belanja Gaji Dokter PTT",value=1000000000.0, min_value=0.0)
            e = st.number_input(label="5115 Belanja Gaji dan Tunjangan Pegawai Non PNS",value=1000000000.0, min_value=0.0)
            f = st.number_input(label="5121 Belanja Honorarium",value=1000000000.0, min_value=0.0)
            g = st.number_input(label="5122 Belanja Lembur",value=1000000000.0, min_value=0.0)
            h = st.number_input(label="5124 Bel. Tunjangan Khusus & Bel. Pegawai Transito",value=1000000000.0, min_value=0.0)
            i = st.number_input(label="5131 Belanja Pensiun dan Uang Tunggu",value=1000000000.0, min_value=0.0)
        with C2 :   
            st.subheader("")
            st.subheader("")
            j = st.number_input(label="5132 Belanja Program Jaminan Sosial Pegawai",value=1000000000.0, min_value=0.0)
            k = st.number_input(label="5211 Belanja Barang Operasional",value=1000000000.0, min_value=0.0)
            l = st.number_input(label="5212 Belanja Barang Non Operasional",value=1000000000.0, min_value=0.0)
            m = st.number_input(label="5215 Belanja Barang Pengganti Pajak Dalam Rangka Hibah MCC",value=1000000000.0, min_value=0.0)
            n = st.number_input(label="5217 Belanja Kontribusi",value=1000000000.0, min_value=0.0)
            o = st.number_input(label="5218 Belanja Barang Persediaan",value=1000000000.0, min_value=0.0)
            p = st.number_input(label="5221 Belanja Jasa",value=1000000000.0, min_value=0.0)
            q = st.number_input(label="5231 Belanja Pemeliharaan",value=1000000000.0, min_value=0.0)
            r = st.number_input(label="5241 Belanja Perjalanan Dinas Dalam Negeri",value=1000000000.0, min_value=0.0)
        with C3 :   
            st.subheader("")
            st.subheader("")
            s = st.number_input(label="5242 Belanja Perjalanan Dinas Luar Negeri",value=1000000000.0, min_value=0.0)
            t = st.number_input(label="5251 Belanja Barang BLU",value=1000000000.0, min_value=0.0)
            u = st.number_input(label="5261 Belanja Barang untuk Diserahkan kepada Masyarakat/Pemda",value=1000000000.0, min_value=0.0)
            v = st.number_input(label="5262 Belanja Brg Fisik dan Penunjang Dana DK dan TP utk Diserahkan kpd Pemda",value=1000000000.0, min_value=0.0)
            w = st.number_input(label="5263 Belanja Brg Lainnya untuk diserahkan kepada masy./Pemda",value=1000000000.0, min_value=0.0)
            x = st.number_input(label="5271 Belanja Brg utk Diserahkan kpd Mantan Presiden dan/atau Mantan WaPres",value=1000000000.0, min_value=0.0)
            z = st.number_input(label="5311 Belanja Modal Tanah",value=1000000000.0, min_value=0.0)
            aa = st.number_input(label="5321 Belanja Modal Peralatan dan Mesin",value=1000000000.0, min_value=0.0)
            bb = st.number_input(label="5331 Belanja Modal Gedung dan Bangunan",value=1000000000.0, min_value=0.0)
        with C4 :    
            st.subheader("")
            st.subheader("")
            cc = st.number_input(label="5341 Belanja Modal Jalan, Irigasi dan Jaringan",value=1000000000.0, min_value=0.0)
            dd = st.number_input(label="5361 Belanja Modal Lainnya",value=1000000000.0, min_value=0.0)
            ee = st.number_input(label="5371 Belanja Modal BLU",value=1000000000.0, min_value=0.0)
            ff = st.number_input(label="5711 Belanja Bantuan Sosial Untuk Rehabilitasi Sosial",value=1000000000.0, min_value=0.0)
            gg = st.number_input(label="5721 Belanja Bantuan Sosial Untuk Jaminan Sosial",value=1000000000.0, min_value=0.0)
            hh = st.number_input(label="5731 Belanja Bantuan Sosial Untuk Pemberdayaan Sosial",value=1000000000.0, min_value=0.0)
            ii = st.number_input(label="5741 Belanja Bantuan Sosial Untuk Perlindungan Sosial",value=1000000000.0, min_value=0.0)
            jj = st.number_input(label="5751 Belanja Bantuan Sosial Untuk Penanggulangan Kemiskinan",value=1000000000.0, min_value=0.0)
            y = st.number_input(label="5761 Belanja Bantuan Sosial Untuk Penanggulangan Bencana",value=1000000000.0, min_value=0.0)
        
                
        if st.button("Klik untuk Mendapatkan Prediksi"):
            dfvalues = pd.DataFrame(list(zip([a],[b],[c],[d],[e],[f],[g],[h],[i],[j],[k],[l],[m],[n],[o],[p],[q],[r],[s],[t],[u],[v],[w],[x],[y],[z],[aa],[bb],[cc],[dd],[ee],[ff],[gg],[hh],[ii],[jj])),columns =['5111','5112','5113','5114','5115','5121','5122','5124','5131','5132','5211','5212','5215','5217','5218','5221','5231','5241','5242','5251','5261','5262','5263','5271','5311','5321','5331','5341','5361','5371','5711','5721','5731','5741','5751','5761'])
            input_variables = np.array(dfvalues[['5111','5112','5113','5114','5115','5121','5122','5124','5131','5132','5211','5212','5215','5217','5218','5221','5231','5241','5242','5251','5261','5262','5263','5271','5311','5321','5331','5341','5361','5371','5711','5721','5731','5741','5751','5761']])
            prediction = USD.predict(input_variables)
            nilai = np.mean(prediction)
            nilai = (nilai)
            st.title(f"Prediksi: Rp{nilai:.2f}")
    if choice == "Prediksi Oil_Price":
        st.subheader("Prediksi Harga Minyak")
        #df = pd.read_excel('DataFrame_h7.xlsx')

        model= open("Oil_Brent_model_final.pkl", "rb")
        Oil=joblib.load(model)

        with C1 :
            st.subheader("Asumsi Nilai Belanja")
            a = st.number_input(label="5111 Belanja Gaji dan Tunjangan PNS",value=1000000000.0, min_value=0.0)
            b = st.number_input(label="5112 Belanja Gaji dan Tunjangan TNI/Polri",value=1000000000.0, min_value=0.0)
            c = st.number_input(label="5113 Belanja Gaji dan Tunjangan Pejabat Negara",value=1000000000.0, min_value=0.0)
            d = st.number_input(label="5114 Belanja Gaji Dokter PTT",value=1000000000.0, min_value=0.0)
            e = st.number_input(label="5115 Belanja Gaji dan Tunjangan Pegawai Non PNS",value=1000000000.0, min_value=0.0)
            f = st.number_input(label="5121 Belanja Honorarium",value=1000000000.0, min_value=0.0)
            g = st.number_input(label="5122 Belanja Lembur",value=1000000000.0, min_value=0.0)
            h = st.number_input(label="5124 Bel. Tunjangan Khusus & Bel. Pegawai Transito",value=1000000000.0, min_value=0.0)
            i = st.number_input(label="5131 Belanja Pensiun dan Uang Tunggu",value=1000000000.0, min_value=0.0)
        with C2 :   
            st.subheader("")
            st.subheader("")
            j = st.number_input(label="5132 Belanja Program Jaminan Sosial Pegawai",value=1000000000.0, min_value=0.0)
            k = st.number_input(label="5211 Belanja Barang Operasional",value=1000000000.0, min_value=0.0)
            l = st.number_input(label="5212 Belanja Barang Non Operasional",value=1000000000.0, min_value=0.0)
            m = st.number_input(label="5215 Belanja Barang Pengganti Pajak Dalam Rangka Hibah MCC",value=1000000000.0, min_value=0.0)
            n = st.number_input(label="5217 Belanja Kontribusi",value=1000000000.0, min_value=0.0)
            o = st.number_input(label="5218 Belanja Barang Persediaan",value=1000000000.0, min_value=0.0)
            p = st.number_input(label="5221 Belanja Jasa",value=1000000000.0, min_value=0.0)
            q = st.number_input(label="5231 Belanja Pemeliharaan",value=1000000000.0, min_value=0.0)
            r = st.number_input(label="5241 Belanja Perjalanan Dinas Dalam Negeri",value=1000000000.0, min_value=0.0)
        with C3 :   
            st.subheader("")
            st.subheader("")
            s = st.number_input(label="5242 Belanja Perjalanan Dinas Luar Negeri",value=1000000000.0, min_value=0.0)
            t = st.number_input(label="5251 Belanja Barang BLU",value=1000000000.0, min_value=0.0)
            u = st.number_input(label="5261 Belanja Barang untuk Diserahkan kepada Masyarakat/Pemda",value=1000000000.0, min_value=0.0)
            v = st.number_input(label="5262 Belanja Brg Fisik dan Penunjang Dana DK dan TP utk Diserahkan kpd Pemda",value=1000000000.0, min_value=0.0)
            w = st.number_input(label="5263 Belanja Brg Lainnya untuk diserahkan kepada masy./Pemda",value=1000000000.0, min_value=0.0)
            x = st.number_input(label="5271 Belanja Brg utk Diserahkan kpd Mantan Presiden dan/atau Mantan WaPres",value=1000000000.0, min_value=0.0)
            z = st.number_input(label="5311 Belanja Modal Tanah",value=1000000000.0, min_value=0.0)
            aa = st.number_input(label="5321 Belanja Modal Peralatan dan Mesin",value=1000000000.0, min_value=0.0)
            bb = st.number_input(label="5331 Belanja Modal Gedung dan Bangunan",value=1000000000.0, min_value=0.0)
        with C4 :    
            st.subheader("")
            st.subheader("")
            cc = st.number_input(label="5341 Belanja Modal Jalan, Irigasi dan Jaringan",value=1000000000.0, min_value=0.0)
            dd = st.number_input(label="5361 Belanja Modal Lainnya",value=1000000000.0, min_value=0.0)
            ee = st.number_input(label="5371 Belanja Modal BLU",value=1000000000.0, min_value=0.0)
            ff = st.number_input(label="5711 Belanja Bantuan Sosial Untuk Rehabilitasi Sosial",value=1000000000.0, min_value=0.0)
            gg = st.number_input(label="5721 Belanja Bantuan Sosial Untuk Jaminan Sosial",value=1000000000.0, min_value=0.0)
            hh = st.number_input(label="5731 Belanja Bantuan Sosial Untuk Pemberdayaan Sosial",value=1000000000.0, min_value=0.0)
            ii = st.number_input(label="5741 Belanja Bantuan Sosial Untuk Perlindungan Sosial",value=1000000000.0, min_value=0.0)
            jj = st.number_input(label="5751 Belanja Bantuan Sosial Untuk Penanggulangan Kemiskinan",value=1000000000.0, min_value=0.0)
            y = st.number_input(label="5761 Belanja Bantuan Sosial Untuk Penanggulangan Bencana",value=1000000000.0, min_value=0.0)
        
                
        if st.button("Klik untuk Mendapatkan Prediksi"):
            dfvalues = pd.DataFrame(list(zip([a],[b],[c],[d],[e],[f],[g],[h],[i],[j],[k],[l],[m],[n],[o],[p],[q],[r],[s],[t],[u],[v],[w],[x],[y],[z],[aa],[bb],[cc],[dd],[ee],[ff],[gg],[hh],[ii],[jj])),columns =['5111','5112','5113','5114','5115','5121','5122','5124','5131','5132','5211','5212','5215','5217','5218','5221','5231','5241','5242','5251','5261','5262','5263','5271','5311','5321','5331','5341','5361','5371','5711','5721','5731','5741','5751','5761'])
            input_variables = np.array(dfvalues[['5111','5112','5113','5114','5115','5121','5122','5124','5131','5132','5211','5212','5215','5217','5218','5221','5231','5241','5242','5251','5261','5262','5263','5271','5311','5321','5331','5341','5361','5371','5711','5721','5731','5741','5751','5761']])
            prediction = Oil.predict(input_variables)
            nilai = np.mean(prediction)
            nilai = (nilai)
            st.title(f"Prediksi: USD {nilai:.2f} per Barel")

    if choice == "Prediksi CCI":
        st.subheader("Prediksi Consumer Confidence Index")
        #df = pd.read_excel('DataFrame_h7.xlsx')

        model= open("CCI_model_final.pkl", "rb")
        CCI=joblib.load(model)

        with C1 :
            st.subheader("Asumsi Nilai Belanja")
            a = st.number_input(label="5111 Belanja Gaji dan Tunjangan PNS",value=1000000000.0, min_value=0.0)
            b = st.number_input(label="5112 Belanja Gaji dan Tunjangan TNI/Polri",value=1000000000.0, min_value=0.0)
            c = st.number_input(label="5113 Belanja Gaji dan Tunjangan Pejabat Negara",value=1000000000.0, min_value=0.0)
            d = st.number_input(label="5114 Belanja Gaji Dokter PTT",value=1000000000.0, min_value=0.0)
            e = st.number_input(label="5115 Belanja Gaji dan Tunjangan Pegawai Non PNS",value=1000000000.0, min_value=0.0)
            f = st.number_input(label="5121 Belanja Honorarium",value=1000000000.0, min_value=0.0)
            g = st.number_input(label="5122 Belanja Lembur",value=1000000000.0, min_value=0.0)
            h = st.number_input(label="5124 Bel. Tunjangan Khusus & Bel. Pegawai Transito",value=1000000000.0, min_value=0.0)
            i = st.number_input(label="5131 Belanja Pensiun dan Uang Tunggu",value=1000000000.0, min_value=0.0)
        with C2 :   
            st.subheader("")
            st.subheader("")
            j = st.number_input(label="5132 Belanja Program Jaminan Sosial Pegawai",value=1000000000.0, min_value=0.0)
            k = st.number_input(label="5211 Belanja Barang Operasional",value=1000000000.0, min_value=0.0)
            l = st.number_input(label="5212 Belanja Barang Non Operasional",value=1000000000.0, min_value=0.0)
            m = st.number_input(label="5215 Belanja Barang Pengganti Pajak Dalam Rangka Hibah MCC",value=1000000000.0, min_value=0.0)
            n = st.number_input(label="5217 Belanja Kontribusi",value=1000000000.0, min_value=0.0)
            o = st.number_input(label="5218 Belanja Barang Persediaan",value=1000000000.0, min_value=0.0)
            p = st.number_input(label="5221 Belanja Jasa",value=1000000000.0, min_value=0.0)
            q = st.number_input(label="5231 Belanja Pemeliharaan",value=1000000000.0, min_value=0.0)
            r = st.number_input(label="5241 Belanja Perjalanan Dinas Dalam Negeri",value=1000000000.0, min_value=0.0)
        with C3 :   
            st.subheader("")
            st.subheader("")
            s = st.number_input(label="5242 Belanja Perjalanan Dinas Luar Negeri",value=1000000000.0, min_value=0.0)
            t = st.number_input(label="5251 Belanja Barang BLU",value=1000000000.0, min_value=0.0)
            u = st.number_input(label="5261 Belanja Barang untuk Diserahkan kepada Masyarakat/Pemda",value=1000000000.0, min_value=0.0)
            v = st.number_input(label="5262 Belanja Brg Fisik dan Penunjang Dana DK dan TP utk Diserahkan kpd Pemda",value=1000000000.0, min_value=0.0)
            w = st.number_input(label="5263 Belanja Brg Lainnya untuk diserahkan kepada masy./Pemda",value=1000000000.0, min_value=0.0)
            x = st.number_input(label="5271 Belanja Brg utk Diserahkan kpd Mantan Presiden dan/atau Mantan WaPres",value=1000000000.0, min_value=0.0)
            z = st.number_input(label="5311 Belanja Modal Tanah",value=1000000000.0, min_value=0.0)
            aa = st.number_input(label="5321 Belanja Modal Peralatan dan Mesin",value=1000000000.0, min_value=0.0)
            bb = st.number_input(label="5331 Belanja Modal Gedung dan Bangunan",value=1000000000.0, min_value=0.0)
        with C4 :    
            st.subheader("")
            st.subheader("")
            cc = st.number_input(label="5341 Belanja Modal Jalan, Irigasi dan Jaringan",value=1000000000.0, min_value=0.0)
            dd = st.number_input(label="5361 Belanja Modal Lainnya",value=1000000000.0, min_value=0.0)
            ee = st.number_input(label="5371 Belanja Modal BLU",value=1000000000.0, min_value=0.0)
            ff = st.number_input(label="5711 Belanja Bantuan Sosial Untuk Rehabilitasi Sosial",value=1000000000.0, min_value=0.0)
            gg = st.number_input(label="5721 Belanja Bantuan Sosial Untuk Jaminan Sosial",value=1000000000.0, min_value=0.0)
            hh = st.number_input(label="5731 Belanja Bantuan Sosial Untuk Pemberdayaan Sosial",value=1000000000.0, min_value=0.0)
            ii = st.number_input(label="5741 Belanja Bantuan Sosial Untuk Perlindungan Sosial",value=1000000000.0, min_value=0.0)
            jj = st.number_input(label="5751 Belanja Bantuan Sosial Untuk Penanggulangan Kemiskinan",value=1000000000.0, min_value=0.0)
            y = st.number_input(label="5761 Belanja Bantuan Sosial Untuk Penanggulangan Bencana",value=1000000000.0, min_value=0.0)
        
                
        if st.button("Klik untuk Mendapatkan Prediksi"):
            dfvalues = pd.DataFrame(list(zip([a],[b],[c],[d],[e],[f],[g],[h],[i],[j],[k],[l],[m],[n],[o],[p],[q],[r],[s],[t],[u],[v],[w],[x],[y],[z],[aa],[bb],[cc],[dd],[ee],[ff],[gg],[hh],[ii],[jj])),columns =['5111','5112','5113','5114','5115','5121','5122','5124','5131','5132','5211','5212','5215','5217','5218','5221','5231','5241','5242','5251','5261','5262','5263','5271','5311','5321','5331','5341','5361','5371','5711','5721','5731','5741','5751','5761'])
            input_variables = np.array(dfvalues[['5111','5112','5113','5114','5115','5121','5122','5124','5131','5132','5211','5212','5215','5217','5218','5221','5231','5241','5242','5251','5261','5262','5263','5271','5311','5321','5331','5341','5361','5371','5711','5721','5731','5741','5751','5761']])
            prediction = CCI.predict(input_variables)
            nilai = np.mean(prediction)
            nilai = (nilai)
            st.title(f"Prediksi Indeks: {nilai:.2f}")        
if __name__=='__main__':
    main()
