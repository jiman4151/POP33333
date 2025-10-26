import streamlit as st
import pandas as pd

st.title("POP 변환기 (엑셀 업로드)")

uploaded_file = st.file_uploader("엑셀 파일을 업로드하세요", type=["xlsx", "xls"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("📊 업로드된 데이터 미리보기:")
    st.dataframe(df.head())

    df["결과"] = "OK"

    csv = df.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        label="💾 변환된 CSV 다운로드",
        data=csv,
        file_name="converted_pop.csv",
        mime="text/csv"
    )
else:
    st.info("엑셀 파일을 업로드하면 변환이 시작됩니다.")
