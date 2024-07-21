# ＣＳＶやエクセルを表示させるコード

import streamlit as st
import pandas as pd
import datetime
from PIL import Image

#pd.set_option('display.unicode.east_asian_width', True)
st.title('ロング・ショート戦略')
#color = st.color_picker('summer sales contest', '#87ceeb')

#txt0 = '<p style="color:red;">※7月14日に米国にて暗殺未遂事件発生のため大荒れ要注意</p>'
#st.write(txt0, unsafe_allow_html=True)


st.write('テスト版')

st.text('更新日7月21日')
st.text(datetime.date.today())

"""
## 今週のロング銘柄ショート銘柄
"""
df1 = pd.DataFrame({
    '買い銘柄':['日野自動車','タツタ電線','王子ＨＤ','ユーグレナ','三菱ケミカルＧ'],
    '現在価格':['437','730','635.3','545','907.8'],
    '目標価格':['450','755','655','570','930']
})
df1

df2 = pd.DataFrame({
    '売り銘柄':['サイバーエージェント','日本板硝子','アイモバイル','マネックスＧ','東京電力ＨＤ'],
    '現在価格':['955.1','416','500','701','796.6'],
    '目標価格':['925','400','460','660','750']
})
df2

#st.dataframe(df)
st.write('１．プライム市場の主要銘柄を選定')
st.write('２．各々３銘柄を売買い保有')
st.write('３．一定の利益または損失がでたら一括決済')
txt1 = '<p style="color:blue;">先週の実績 買い推奨５銘柄計 -6.88%</p>'
st.write(txt1, unsafe_allow_html=True)
txt2 = '<p style="color:red;">先週の実績 売り推奨５銘柄計 +11.68%</p>'
st.write(txt2, unsafe_allow_html=True)

"""
##  ＮＴ倍率
"""
df3 = pd.DataFrame({
    '指数':['日経平均225'],
    '現在価格':['39590'],
    '上値抵抗':['40300'],
    '下値支持':['39000']
})
df3

df4 = pd.DataFrame({
    '指数':['TOPIX'],
    '現在価格':['2841.5'],
    '上値抵抗':['2900'],
    '下値支持':['2800']
})
df4

data = pd.DataFrame({
    'NT':['上値抵抗','現在','下値支持'],
    'レシオ':['14.45','14.00','13.85']
    })
data

st.write('14.20上抜け後いってこい。レンジ続く。 :+1:')
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
## 225・XAU・USDチャート 
"""
Image2 = Image.open('bt1.jpg')
st.image(Image2,caption='225チャート4H足',use_column_width=True)

Image3 = Image.open('bt2.jpg')
st.image(Image3,caption='XAUUSDチャート4H足',use_column_width=True)

Image4 = Image.open('bt3.jpg')
st.image(Image4,caption='USDJPYチャート4H足',use_column_width=True)

"""
## 先物・オプション：シュミレーション
"""
"""
## 先週のOP戦略はロングストラドル
### 7月3週SQ
### 権利行使価格41500
### コール@190買い
### プット@500買い
### 購入費用69000円
## 結果7/19のSQ値40003.75
## 差引+80,652円

"""
"""
## 今週のOP戦略はプロティクティブプット
## （225が上に行っても下に行っても利益）
### マイクロ先物8限 39,590 2枚買い
### ミニプットオプション 7/4W
### 権利行使価格39,000
### プット1枚買い@140
### 想定証拠金43,000円
## SQ持込せずに一定の利益で決済予定

"""


st.write('ご訪問ありがとうございます')

