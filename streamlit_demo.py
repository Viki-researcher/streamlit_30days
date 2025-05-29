import streamlit as st
import pandas as pd
from PIL import Image
import os

# 数据加载
@st.cache_data
def load_data():
    df = pd.read_csv(r"D:\pycharmdemo\shujukanban\image_tags.csv")
    df["date"] = pd.to_datetime(df["date"])  # 确保日期格式统一
    return df

df = load_data()

# 侧边栏筛选控件
st.sidebar.header("筛选条件")
date_range = st.sidebar.date_input("选择日期范围", [df["date"].min(), df["date"].max()])
locations = st.sidebar.multiselect("选择点位", df["location"].unique())
additional_tags = st.sidebar.multiselect("附加标签", df["additional_tag1"].unique())

# 数据过滤
filtered_df = df[
    (df["date"].between(*date_range)) &
    (df["location"].isin(locations)) &
    (df["additional_tag1"].isin(additional_tags))
]

# 主界面：二维矩阵视图
st.header("图像看板：时间 X 点位")

# 按日期和点位分组
grouped = filtered_df.groupby(["date", "location"])

# 生成矩阵布局
for (date, location), group in grouped:
    # 显示日期和点位作为单元格标题
    st.subheader(f"{date.strftime('%Y-%m-%d')} - {location}")
    
    # 平铺图片缩略图
    cols = st.columns(4)  # 每行4列
    for idx, row in group.iterrows():
        img = Image.open(row["image_path"])
        cols[idx % 4].image(img, caption=row["additional_tag1"], width=150)
        cols[idx % 4].button("查看详情", key=f"btn_{idx}")

# 点击按钮后的回调（需结合Session State实现）
# 此处需自定义逻辑，例如弹出对话框显示大图