import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

data = {
    "Họ tên": [
        "Nguyễn Văn An", "Trần Thị Bình", "Lê Minh Anh",
        "Phạm Hoàng Nam", "Võ Thị Lan", "Đặng Quốc Huy",
        "Nguyễn Thị Mai", "Trần Minh Khang",
        "Lê Hoàng Long", "Phạm Ngọc Hà"
    ],
    "Chuyên cần": [8, 9, 7, 10, 8, 6, 9, 7, 8, 9],
    "Giữa kỳ": [7, 8, 6, 9, 7, 5, 8, 6, 7, 9],
    "Cuối kỳ": [8, 9, 7, 8, 8, 6, 9, 7, 8, 9]
}

df = pd.DataFrame(data)

df["Tổng kết"] = (
    df["Chuyên cần"] * 0.2
    + df["Giữa kỳ"] * 0.3
    + df["Cuối kỳ"] * 0.5
).round(2)

def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

st.subheader("Bảng điểm sinh viên")
st.dataframe(df, use_container_width=True, hide_index=True)

st.subheader("Thống kê lớp")
st.metric("Điểm trung bình", f"{df['Tổng kết'].mean():.2f}")
st.metric("Số sinh viên đạt", f"{(df['Tổng kết'] >= 5).sum()}/10")

cao = df.loc[df["Tổng kết"].idxmax()]
thap = df.loc[df["Tổng kết"].idxmin()]

st.write("**Điểm cao nhất:**", cao["Họ tên"], "-", cao["Tổng kết"])
st.write("**Điểm thấp nhất:**", thap["Họ tên"], "-", thap["Tổng kết"])

st.subheader("Tra cứu sinh viên")
ten = st.selectbox("Chọn sinh viên", df["Họ tên"])
sv = df[df["Họ tên"] == ten].iloc[0]

st.write("Chuyên cần:", sv["Chuyên cần"])
st.write("Giữa kỳ:", sv["Giữa kỳ"])
st.write("Cuối kỳ:", sv["Cuối kỳ"])
st.write("Tổng kết:", sv["Tổng kết"])
st.write("Xếp loại:", sv["Xếp loại"])

st.subheader("Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(df["Họ tên"], df["Tổng kết"])
ax.set_title("ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN")
ax.set_xlabel("Họ tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)
plt.xticks(rotation=45, ha="right")
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

st.markdown("---")
st.caption("Người tạo: Vương Mạnh Tường | MSSV:040208025723")
