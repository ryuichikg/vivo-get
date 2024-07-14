# ＣＳＶやエクセルを表示させるコード

import streamlit as st
import pandas as pd
import datetime
from PIL import Image

#pd.set_option('display.unicode.east_asian_width', True)
st.title('ロング・ショート戦略')
#color = st.color_picker('summer sales contest', '#87ceeb')

txt0 = '<p style="color:red;">※7月14日に米国にて暗殺未遂事件発生のため要注意</p>'
st.write(txt0, unsafe_allow_html=True)


st.write('テスト版')

st.text('更新日7月14日')
st.text(datetime.date.today())

"""
## 今週のロング銘柄ショート銘柄
"""
df1 = pd.DataFrame({
    '買い銘柄':['インフォマート','日東精工','東海東京','シャープ','鎌倉新書'],
    '現在価格':['337','641','580','968.8','438'],
    '目標価格':['370','700','600','1000','515']
})
df1

df2 = pd.DataFrame({
    '売り銘柄':['ダブルスコープ','三協立山','三菱製紙','ユニチカ','ENEOS'],
    '現在価格':['517','780','741','301','813.7'],
    '目標価格':['500','740','710','280','800']
})
df2

#st.dataframe(df)
st.write('１．プライム市場で取引量のある主要銘柄を選定')
st.write('２．各々３銘柄を売買い保有')
st.write('３．一定の利益または損失がでたら一括決済')
txt1 = '<p style="color:red;">先週の実績 買い推奨５銘柄計 +3.01%</p>'
st.write(txt1, unsafe_allow_html=True)
txt2 = '<p style="color:blue;">先週の実績 売り推奨５銘柄計 -14.82%</p>'
st.write(txt2, unsafe_allow_html=True)

"""
##  ＮＴ倍率
"""
df3 = pd.DataFrame({
    '指数':['日経平均225'],
    '現在価格':['41190'],
    '上値抵抗':['42500'],
    '下値支持':['39450']
})
df3

df4 = pd.DataFrame({
    '指数':['TOPIX'],
    '現在価格':['2894.56'],
    '上値抵抗':['2950'],
    '下値支持':['2830']
})
df4

data = pd.DataFrame({
    'NT':['上値抵抗','現在','下値支持'],
    'レシオ':['14.45','14.23','14.20']
    })
data

st.write('14.20上抜け。上昇できるか。 :+1:')
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
## 225:15足/1H足 XAUチャート 
"""
Image2 = Image.open('bt1.jpg')
st.image(Image2,caption='225チャート15M足',use_column_width=True)

Image3 = Image.open('bt2.jpg')
st.image(Image3,caption='225チャート1H足',use_column_width=True)

Image4 = Image.open('bt3.jpg')
st.image(Image4,caption='XAUチャート日足',use_column_width=True)

"""
## 先物・オプション：シュミレーション
"""
"""
### 日経平均先物7月限マイクロ1枚買い41000
### 日経平均ミニオプション7月限 39000プット買い10円
### 7月限(SQ7月12日)での短期決戦。結果は？

### 先物 SQ 41531  +5310円
### オプション -1000円

## 今週のオプション戦略はロングストラドル
### 7月3週SQ
###・権利行使価格41500
###・コール@190買い  プット@500買い
###・合計69000円

"""



st.write('ご訪問ありがとうございます')

