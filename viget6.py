import streamlit as st

st.markdown(':green[プレミアム価格シミュレーション]')

#nop1 = st.number_input('現在の日経225平均値',min_value=30000,max_value=45000,value=38000,step=10)

nop3 = st.number_input('日経225値幅予測',min_value=-2000,max_value=3000,value=200,step=10)


nop2 = st.number_input('現在のプレミアム価格',min_value=1,max_value=3000,value=100,step=5)

nop4 = st.selectbox('日数',[1,2,3])

# 小数点以下を含む負の値を入力
val1 = st.number_input(
    label="デルタ値",
    min_value=-1.0,  # 最小値
    max_value=1.0,     # 最大値
    step=0.001,          # 増減のステップ
    format="%.4f"      # 小数点以下2桁まで表示
)

val2 = st.number_input(
    label="ガンマ",
    min_value=0.00001,  # 最小値
    max_value=0.00060,     # 最大値
    step=0.00001,          # 増減のステップ
    format="%.5f"      # 小数点以下2桁まで表示
)

val3 = st.number_input(
    label="ベガ値",
    min_value=0.000,  # 最小値
    max_value=50.000,     # 最大値
    step=0.010,          # 増減のステップ
    format="%.3f"      # 小数点以下2桁まで表示
)

val4 = st.number_input(
    label="IV変動率（1% = 0.01)",
    min_value=0.000,  # 最小値
    max_value=100.000,     # 最大値
    step=0.100,          # 増減のステップ
    format="%.3f"      # 小数点以下2桁まで表示
)

val5 = st.number_input(
    label="セータ",
    min_value=-100.000,  # 最小値
    max_value=50.000,     # 最大値
    step=0.010,          # 増減のステップ
    format="%.3f"      # 小数点以下2桁まで表示
)

#slider=st.slider('範囲指定',min_value=0,max_value=100,step=5)

de1 = nop3 * val1
ga1 = (nop3*nop3) *val2/2
be1 = nop3 * val4
se1 = nop4 * val5

st.markdown(':blue[プレミアム価格]')
st.subheader(de1 + ga1  + be1  + se1  + nop2)

