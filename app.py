import streamlit as st

st.title("Tính lãi đơn và lãi kép")

# Nhập dữ liệu
C = st.number_input("Số tiền gốc (VND)", value=500000000.0)
i = st.number_input("Lãi suất năm", value=0.06, format="%.4f")
n = st.number_input("Số tháng", value=4, step=1)

# Tính toán
A = C * (1 + i * n / 12)      # Lãi đơn
B = C * (1 + i / 12) ** n     # Lãi kép

# Hiển thị kết quả
st.subheader("Kết quả")
st.write(f"Tổng tiền nhận được theo lãi đơn: {A:,.0f} VND")
st.write(f"Tổng tiền nhận được theo lãi kép: {B:,.0f} VND")

# Chênh lệch
st.write(f"Chênh lệch: {B - A:,.0f} VND")
