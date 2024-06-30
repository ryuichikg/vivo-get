# ＣＳＶやエクセルを表示させるコード

import streamlit as st
import pandas as pd
import datetime
from PIL import Image

#pd.set_option('display.unicode.east_asian_width', True)
st.title('ロング・ショート戦略')
#color = st.color_picker('summer sales contest', '#87ceeb')

st.write('テスト版')

st.text('更新日6月30日')
st.text(datetime.date.today())

"""
## 今週のロング銘柄ショート銘柄
"""
df1 = pd.DataFrame({
    '買い銘柄':['住友化学','千代田化工建設','住友ファーマ','ソースネクスト','日産自動車'],
    '現在価格':['344.7','302','405','212','545.9'],
    '目標価格':['367','346','460','240','573']
})
df1

df2 = pd.DataFrame({
    '売り銘柄':['ディスコ','メルカリ','JT','SUMCO','東急不動産'],
    '現在価格':['61040','1997.5','4348','2315.5','1073.5'],
    '目標価格':['57300','1900','4335','2280','1025']
})
df2

#st.dataframe(df)
st.write('１．プライム市場で取引量のある主要銘柄を選定')
st.write('２．各々３銘柄を売買い保有')
st.write('３．一定の利益または損失がでたら一括決済')
txt1 = '<p style="color:red;">先週の実績 買い推奨５銘柄計 +280.9円</p>'
st.write(txt1, unsafe_allow_html=True)
txt2 = '<p style="color:red;">先週の実績 売り推奨５銘柄計 +504.5円</p>'
st.write(txt2, unsafe_allow_html=True)

"""
##  ＮＴ倍率
"""
df3 = pd.DataFrame({
    '指数':['日経平均225'],
    '現在価格':['39583.08'],
    '上値抵抗':['40000'],
    '下値支持':['39200']
})
df3

df4 = pd.DataFrame({
    '指数':['TOPIX'],
    '現在価格':['2809.63'],
    '上値抵抗':['2820'],
    '下値支持':['2780']
})
df4

data = pd.DataFrame({
    'NT':['上値抵抗','現在','下値支持'],
    'レシオ':['14.250','14.088','13.850']
    })
data

st.write('もみ合い続く :lightning:')
"""
## ＮＴレシオグラフ
"""
submit = st.button('押して会員登録確定 　●万/月')
if submit == True:
    st.bar_chart(data.set_index('NT'))
    # plt.bar(df)
st.write("投資の判断は自己責任で")

image1 = Image.open('nt01.jpg')
st.image(image1, caption='NTチャート',use_column_width=True)

"""
## 225/DOW/XAUチャート (上 1H足 下 日足)
"""
Image2 = Image.open('bt1.jpg')
st.image(Image2,caption='225チャート',use_column_width=True)

Image3 = Image.open('bt2.jpg')
st.image(Image3,caption='DOWチャート',use_column_width=True)

Image4 = Image.open('bt3.jpg')
st.image(Image4,caption='XAUチャート',use_column_width=True)

st.write('ご訪問ありがとうございます')

