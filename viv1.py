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
## 今週のロング銘柄・ショート銘柄
"""
df1 = pd.read_csv('https://github.com/ryuichikg/vivo-get/blob/main/KS211.csv', encoding='shift_jis', index_col=0)
df3 = pd.read_csv('https://github.com/ryuichikg/vivo-get/blob/main/KS212.csv', encoding='shift_jis', index_col=0)
df2 = pd.read_csv('https://github.com/ryuichikg/vivo-get/blob/main/KS22.csv', encoding='shift_jis', index_col=0)
#st.dataframe(df)
df1
df3
st.write('１．日経プライム市場で大型中型かつ低予算で組める銘柄を選出')
st.write('２．各々３銘柄を売買い保有')
st.write('３．一定の利益または損失がでたら一括決済')

"""
##  ＮＴ倍率
"""
df2
st.write('もみ合い続く :lightning:')
"""
## 日経平均とTOPIXグラフ
"""
submit = st.button('会員登録はこちら')
if submit == True:
    st.bar_chart(df2)
    # plt.bar(df)
st.write("投資のご判断は自己責任で")
