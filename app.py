import streamlit as st
import wbdata
import pandas as pd
import matplotlib.pyplot as plt

st.title("GDP Bình Quân Đầu Người")

country = st.text_input(
    "Nhập tên quốc gia",
    value="Vietnam"
)

try:
    indicator = {
        'NY.GDP.PCAP.CD': 'GDP_PER_CAPITA'
    }

    df = wbdata.get_dataframe(
        indicator,
        country=country,
        date=('2000', '2024')
    )

    df = df.sort_index()

    st.subheader("Dữ liệu")

    st.dataframe(df)

    latest_value = df['GDP_PER_CAPITA'].iloc[-1]

    st.metric(
        "GDP bình quân đầu người gần nhất",
        f"${latest_value:,.0f}"
    )

    fig, ax = plt.subplots(figsize=(10,4))

    ax.plot(
        df.index,
        df['GDP_PER_CAPITA'],
        marker='o',
        linewidth=2
    )

    ax.set_title(
        f'GDP bình quân đầu người - {country}'
    )

    ax.set_xlabel('Năm')
    ax.set_ylabel('USD/người')

    ax.grid(True)

    st.pyplot(fig)

except:
    st.error("Không tìm thấy quốc gia!")
