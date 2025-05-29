import gradio as gr
import pandas as pd
from PIL import Image

# 加载数据
df = pd.read_csv(r"D:\pycharmdemo\shujukanban\image_tags.csv")

def filter_images(start_date, end_date, locations):
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date) & (df['location'].isin(locations))]
    grouped = filtered_df.groupby(['date', 'location'])
    
    # 生成图像网格
    output = []
    for (date, loc), group in grouped:
        output.append(f"## {date} - {loc}")
        images = [Image.open(row['image_path']) for _, row in group.iterrows()]
        output.extend(images)
    return output

# 界面设计
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=1):
            date_range = gr.DatePicker(label="日期范围", type="date")
            locations = gr.Dropdown(label="点位", choices=df['location'].unique().tolist(), multiselect=True)
            filter_btn = gr.Button("筛选")
        with gr.Column(scale=4):
            gallery = gr.Gallery(label="图像矩阵", columns=4)
    
    filter_btn.click(
        fn=filter_images,
        inputs=[date_range, locations],
        outputs=gallery
    )

demo.launch()