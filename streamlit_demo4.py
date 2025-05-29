'''
面简单介绍一下 streamlit 是如何渲染出这个页面的。当我们运行 streamlit run app.py 时，主程序并不是我们的 app.py，
而是 streamlit 启动脚本，它负责读取我们的 app.py，然后根据其中的内容渲染出页面（HTML）和对应的逻辑（JavaScript）
'''

import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 设置全局属性
st.set_page_config(
    page_title='我是标题',
    page_icon=' ',
    layout='wide'
)

# 正文
st.title('hello world')
st.markdown('> Streamlit 支持通过 st.markdown 直接渲染 markdown')


#侧边栏 sidebar
## st.sidebar 下的内容会被渲染到侧边栏
with st.sidebar:
    st.title('欢迎来到我的应用')
    st.markdown('---')
    st.markdown('这是它的特性：\n- feature 1\n- feature 2\n- feature 3')

## 默认渲染到主界面
st.title('这是主界面')
st.info('这是主界面内容')

## st.sidebar 下的内容会被渲染到侧边栏
sidebar = st.sidebar
sidebar.title('欢迎来到我的应用')
sidebar.markdown('---')
sidebar.markdown('这是它的特性：\n- feature 1\n- feature 2\n- feature 3')

## 默认渲染到主界面
st.title('这是主界面')
st.info('这是主界面内容')

'''
列 columns
构建应用时，我们总喜欢让想要展示的数据分成两栏，columns 就能实现这一点
'''

c1, c2 = st.columns(spec=2)

c1.title('This is Column Ⅰ')
c2.title('This is Column Ⅱ')


'''
标签页 tabs
标签页 tabs 可以用于在小空间内展示若干个平级的事物，比如我们可以展示一下不同 API 读取图像的方法：
'''

st.title('Python 不同的库实现图像读入成 numpy 数组')
tab1, tab2, tab3 = st.tabs(['opencv', 'pillow', 'imageio'])

with tab1:
    '''
    ```python
    import cv2
    image = cv2.imread('image.png')
    ```
    '''

with tab2:
    '''
    ```python
    from PIL import Image
    image = Image.open('image.png')
    ```
    '''

with tab3:
    '''
    ```python
    import imageio
    image = imageio.imread('image.png')
    ```
    '''

'''
折叠布局 expander
expander 会创建一个可被折叠的布局，用于隐藏一些不太重要的信息。
'''

st.title('猜猜我在哪里？')
expander_1 = st.expander('region 1')
expander_2 = st.expander('region 2')

expander_1.warning('不在这里！')
expander_1.image('https://pica.zhimg.com/80/v2-5e767eeed478fc195d5df472db538640_1440w.png')

expander_2.warning('也不在这里！')
expander_2.image('https://pic1.zhimg.com/80/v2-79ba9b4bee266815fb4069a5de5afea7_1440w.png')

#单元素容器 empty
import time
placeholder = st.empty()

with placeholder:
    for i in range(10):
        st.write(i, ' s')
        # time.sleep(1.)

# 清空 empty 内的元素
placeholder.empty()


#嵌套布局
c1, c2 = st.columns(spec=2)

with c2:
    st.title('column Ⅱ')
    st.info('content in column Ⅱ')

with c1:
    st.title('column Ⅰ')
    c_1_1, c_1_2 = c1.columns(spec=2)

    with c_1_1:
        st.info('sub column 1 in column Ⅰ')

    with c_1_2:
        st.info('sub column 2 in column Ⅱ')

#组件被渲染的先后顺序是由他们的父组件被定义的先后顺序决定的
c1, c2 = st.columns(spec=2)
# 将被渲染在最下方
st.title('hello')
st.write('this is a simple python code')
with st.echo():
    foo_dict = { i : i for i in range(10)}
    
with c2:
    st.title('column Ⅱ')
    st.info('content in column Ⅱ')

with c1:
    st.title('column Ⅰ')
    c_1_1, c_1_2 = c1.columns(spec=2)

    with c_1_1:
        st.info('sub column 1 in column Ⅰ')

    with c_1_2:
        st.info('sub column 2 in column Ⅱ')


#st.markdown()：用于支持Markdown格式的文本，允许你使用Markdown语法来添加样式

st.markdown('''
# 静夜思
床前**明月**光，疑是地上霜。
举头望**明月**，低头思故乡。
''')
 
st.text('''
静夜思
床前明月光，疑是地上霜。
举头望明月，低头思故乡。
''')



#st.write()：是Streamlit中用于在应用程序中展示文本和数据的通用函数
# 字符串
st.write("这是一段文本。")
 
# 数字
st.write(42)
 
# 列表
st.write([1, 2, 3])
 
# 字典
st.write({"key": "value"})
 
# 数据框（DataFrame）
df = pd.DataFrame({"Column 1": [1, 2, 3], "Column 2": ["A", "B", "C"]})
st.write(df)
 
#多参数用法
st.write("这是一个字符串", 42, [1, 2, 3], {"key": "value"})
 
#自定义渲染
fig, ax = plt.subplots()
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax.plot(x, y)
st.write(fig)

##交互
 
if st.button('点我'):
    st.write('今天是个好日子！')

#复选框
 
cb = st.checkbox('确认',value=False)
 
if cb:
    st.write('确认成功')
else:
    st.write('没有确认')    


#单选框
sex = st.radio(
    label = '请输入您的性别',
    options = ('男', '女', '保密'),
    index = 2,
    format_func = str,
    help = '如果您不想透露，可以选择保密'
    )
 
if sex == '男':
    st.write('男士您好!')
elif sex == '女':
    st.write('女士您好!')
else:
    st.write('您好!')    

#下拉框
sex = st.selectbox(
    label = '请输入您的性别',
    options = ('男', '女', '保密'),
    index = 2,
    format_func = str,
    help = '如果您不想透露，可以选择保密'
    )
 
if sex == '男':
    st.write('男士您好!')
elif sex == '女':
    st.write('女士您好!')
else:
    st.write('您好!')


#多选框 
options = st.multiselect(
    label = '请问您喜欢吃什么水果',
    options = ('橘子', '苹果', '香蕉', '草莓', '葡萄'),
    default = None,
    format_func = str,
    help = '选择您喜欢吃的水果'
    )
 
st.write('您喜欢吃的是', options)    

#滑动拉杆
age = st.slider(label='请输入您的年龄', 
                min_value=0, 
                max_value=100, 
                value=0, 
                step=1, 
                help="请输入您的年龄"
               )
 
st.write('您的年龄是', age)

#单行文本输入框
name = st.text_input('请输入用户名',  max_chars=100, help='最大长度为100字符')
 
# 根据用户输入进行操作
st.write('您的用户名是', name)


#数字输入框

age = st.number_input(label = '请输入您的年龄', 
                     min_value=0, 
                     max_value=100, 
                     value=0, 
                     step=1, 
                     help='请输入您的年龄'
                    )
st.write('您的年龄是', age)


#多行文本输入框
text = st.text_area(
    label='请输入文本',
    value='请输入...',
    height=100,
    max_chars=200,
    help='最大长度限制为200'
)

# 将换行符转换为Markdown换行语法
formatted_text = text.replace('\n', '  \n')  # 双空格+换行符是Markdown换行语法
st.markdown(f"**您的输入是**  \n{formatted_text}")


# # 将换行符转换为HTML的<br>标签
# formatted_text = text.replace('\n', '<br>')
# st.markdown(f"**您的输入是**  \n{formatted_text}", unsafe_allow_html=True)

#其他提示信息
st.error('错误信息')
 
st.warning('警告信息')
 
st.info('提示信息')
 
st.success('成功信息')
 
st.exception('异常信息')


#显示执行状态
 
progress_bar = st.empty()
 
for i in range(10):
    progress_bar.progress(i / 10, '进度')
    time.sleep(0.5)
 
with st.spinner('加载中...'):
    time.sleep(2)