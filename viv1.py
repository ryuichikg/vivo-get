# ＣＳＶやエクセルを表示させるコード

import streamlit as st
import pandas as pd
import datetime
from PIL import Image

#pd.set_option('display.unicode.east_asian_width', True)
st.title('ロング・ショート戦略')
#color = st.color_picker('summer sales contest', '#87ceeb')

st.write('テスト版')

st.text('更新日7月7日')
st.text(datetime.date.today())

"""
## 今週のロング銘柄ショート銘柄
"""
df1 = pd.DataFrame({
    '買い銘柄':['アニコムHD','三井住友建設','セブン銀行','東レ','日立造船'],
    '現在価格':['680','403','274.4','746.8','1094'],
    '目標価格':['710','420','290','785','1180']
})
df1

df2 = pd.DataFrame({
    '売り銘柄':['杏林製薬','ラウンドワン','旭化成','オンワードHLD','レオパレス２１'],
    '現在価格':['1683','801','1008.5','580','517'],
    '目標価格':['1650','750','980','530','490']
})
df2

#st.dataframe(df)
st.write('１．プライム市場で取引量のある主要銘柄を選定')
st.write('２．各々３銘柄を売買い保有')
st.write('３．一定の利益または損失がでたら一括決済')
txt1 = '<p style="color:red;">先週の実績 買い推奨５銘柄計 +13.48%</p>'
st.write(txt1, unsafe_allow_html=True)
txt2 = '<p style="color:blue;">先週の実績 売り推奨５銘柄計 -32.88%</p>'
st.write(txt2, unsafe_allow_html=True)

"""
##  ＮＴ倍率
"""
df3 = pd.DataFrame({
    '指数':['日経平均225'],
    '現在価格':['41010'],
    '上値抵抗':['41500'],
    '下値支持':['40750']
})
df3

df4 = pd.DataFrame({
    '指数':['TOPIX'],
    '現在価格':['2884.5'],
    '上値抵抗':['2910'],
    '下値支持':['2850']
})
df4

data = pd.DataFrame({
    'NT':['上値抵抗','現在','下値支持'],
    'レシオ':['14.250','14.217','13.850']
    })
data

st.write('もみ合い続く。14.25上抜けできるか。 :lightning:')
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
## 225/DOW/XAUチャート 1時間足
"""
Image2 = Image.open('bt1.jpg')
st.image(Image2,caption='225チャート',use_column_width=True)

Image3 = Image.open('bt2.jpg')
st.image(Image3,caption='DOWチャート',use_column_width=True)

Image4 = Image.open('bt3.jpg')
st.image(Image4,caption='XAUチャート',use_column_width=True)

"""
## 先物・オプション：シュミレーション
"""
"""
### 日経平均先物7月限マイクロ1枚買い41000
### 日経平均ミニオプション7月限 39000プット買い10円
### 7月限(SQ7月12日)での短期決戦。結果は？
"""



st.write('ご訪問ありがとうございます')

