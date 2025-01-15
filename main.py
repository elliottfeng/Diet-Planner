import streamlit as st
from planner import planner  # 确保导入你的 planner 函数

# 设置页面标题
st.title("体脂率和基础代谢值计算器")

# 侧边栏输入 API 密钥
api_key = st.sidebar.text_input("请输入你的 API 密钥", type="password", value="sk-9e93c5fca1a1419eb749550a65940b55")

# 主页面输入框
st.header("用户信息输入")
sex = st.selectbox("性别", ["男", "女"])
age = st.number_input("年龄", min_value=0, max_value=120, value=0)
height = st.number_input("身高 (cm)", min_value=0, value=0)
weight = st.number_input("体重 (kg)", min_value=0, value=0)
waistline = st.number_input("腰围 (cm)", min_value=0, value=0)
neckline = st.number_input("颈围 (cm)", min_value=0, value=0)
target = st.selectbox("身体管理目标", ["增肌", "减脂", "保持"])

# 上传按钮
if st.button("上传"):
    # 输入验证
    if not api_key or age <= 0 or height <= 0 or weight <= 0 or waistline <= 0 or neckline <= 0:
        st.error("请正确填写信息")
    else:
        # 显示等待提示
        with st.spinner("请耐心等待...不要重复上传"):
            body_info, request = planner(sex, age, height, weight, waistline, neckline, "body_info", target, api_key)

        # 显示结果
        st.success("计算完成！")
        st.subheader("体脂率和基础代谢值:")
        st.text(body_info)
        st.subheader("定制的每日营养摄入量:")
        st.text(request)

