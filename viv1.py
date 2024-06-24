# ＣＳＶやエクセルを表示させるコード

import streamlit as st
import pandas as pd
import datetime

#pd.set_option('display.unicode.east_asian_width', True)
st.title('ロング・ショート戦略')
#color = st.color_picker('summer sales contest', '#87ceeb')

st.write('テスト版')

st.text(datetime.date.today())

"""
## 今週のロング銘柄ショート銘柄
"""
df1 = pd.DataFrame({
    '買い銘柄':['三菱重工','村田製作所','りそな','トヨタ自動車','日本電信電話'],
    '現在価格':['1613.5','3345','1012.5','3150','149.4'],
    '目標価格':['1645','3400','1050','3350','155']
})
df1

df2 = pd.DataFrame({
    '売り銘柄':['住友不動産','パナソニック','日本製鉄','SUBARU','浜松ホトニクス'],
    '現在価格':['5190','1303.5','3343','3354','4471'],
    '目標価格':['5100','1260','3250','3330','4450']
})
df2

#st.dataframe(df)
st.write('１．日経プライム市場で取引量のある主要銘柄を選定')
st.write('２．各々３銘柄を売買い保有')
st.write('３．一定の利益または損失がでたら一括決済')

"""
##  ＮＴ倍率
"""
df3 = pd.DataFrame({
    '指数':['日経平均225'],
    '現在価格':['38804.65'],
    '上値抵抗':['39500'],
    '下値支持':['38000']
})
df3

df4 = pd.DataFrame({
    '指数':['TOPIX'],
    '現在価格':['2740.19'],
    '上値抵抗':['2800'],
    '下値支持':['2700']
})
df4

data = pd.DataFrame({
    'NT':['上値抵抗','現在','下値支持'],
    'レシオ':['14.250','14.161','13.850']
    })
data

st.write('もみ合い続く :lightning:')
"""
## ＮＴレシオグラフ
"""
submit = st.button('押して会員登録確定 　98万/月')
if submit == True:
    st.bar_chart(data.set_index('NT'))
    # plt.bar(df)
st.write("投資のご判断は自己責任で")
