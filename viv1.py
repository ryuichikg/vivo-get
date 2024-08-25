# ＣＳＶやエクセルを表示させるコード

import streamlit as st
import pandas as pd
import datetime
from PIL import Image

#pd.set_option('display.unicode.east_asian_width', True)
st.title('現物株・先物オプション戦略')
#color = st.color_picker('summer sales contest', '#87ceeb')

#txt0 = '<p style="color:red;">※8月12日は先物オプション休場。海外は通常取引のため8月13日窓開け注意！</p>'
#st.write(txt0, unsafe_allow_html=True)


st.write('テスト版')

st.text('更新日8月25日')
st.text(datetime.date.today())

"""
##### ⚠️今週のロング銘柄ショート銘柄
###### 
"""

df1 = pd.DataFrame({

     '買い銘柄':['ENEOS','オリエンタル白石','五洋建設','ヤマダHD','住石HD'],
     '現在価格':['760.4','385','647.6','447.1','983'],
     '目標価格':['810','410','680','460','1100']
 })
df1

df2 = pd.DataFrame({
     '売り銘柄':['筑波銀行','ワタミ','グリー','北海道電力','マネックスG'],
     '現在価格':['267','893','450','1002','679'],
     '目標価格':['240','850','415','900','640']
 })
df2

#st.dataframe(df)
st.write('１．プライム市場の主要銘柄を選定。一部例外有り。')
st.write('２．各々３銘柄を売買い保有')
st.write('３．一定の利益または損失がでたら一括決済')
txt1 = '<p style="color:blue;">先週の実績 買い推奨５銘柄計 +16.82%</p>'
st.write(txt1, unsafe_allow_html=True)
txt2 = '<p style="color:red;">先週の実績 売り推奨５銘柄計 -18.33%</p>'
st.write(txt2, unsafe_allow_html=True)


"""
#####  ✅ＮＴ倍率
"""
df3 = pd.DataFrame({
    '指数':['日経平均225'],
    '現在価格':['38255'],
    '上値抵抗':['38750'],
    '下値支持':['36700']
})
df3

df4 = pd.DataFrame({
    '指数':['TOPIX'],
    '現在価格':['2681'],
    '上値抵抗':['2720'],
    '下値支持':['2593']
})
df4

data = pd.DataFrame({
    'NT':['上値抵抗','現在','下値支持'],
    'レシオ':['14.40','14.26','13.85']
    })
data

st.write('14.36まで上昇。上値重く逆張り戦略。')
"""
##### ✅ＮＴレシオグラフ
"""
submit = st.button('押して会員登録確定 　●万/月')
if submit == True:
    st.bar_chart(data.set_index('NT'))
    # plt.bar(df)
st.write("投資の判断は自己責任で")

image1 = Image.open('nt01.jpg')
st.image(image1, caption='NTチャート',use_column_width=True)

"""
 ### 225日足チャート 
 ##### ※8/23のジャクソンホールにてFRBが利下げ告知。ドル円下へ。
 ##### ※円高方向へシフトしたため、日本株は円高メリット株以外は重い展開予想。
 ##### ※過去の出来高からみて、38,000円からの上値追いは厳しいとみます。
"""
Image2 = Image.open('bt1.jpg')
st.image(Image2,caption='225チャート日足',use_column_width=True)

# Image3 = Image.open('bt2.jpg')
# st.image(Image3,caption='XAUUSDチャート日足',use_column_width=True)

# Image4 = Image.open('bt3.jpg')
# st.image(Image4,caption='NAS100チャート日足',use_column_width=True)

"""
##### ✅先物・オプション：シュミレーション
"""
"""
##### ⚠️先週のOP戦略は「⓵プロテクティブ・プット」又は「⓶ベア・シンセティック」
###### ⏹ベア・シンセティック（カバード・コールとプロティクティブ・プットの合成）
######
##### ⓵プロティクティブ・プット
##### micro225先物9限 37,620 2枚買い
#####
##### ミニプットオプション 9月限
###### 権利行使価格35,000
###### プット1枚買い@250
#####
##### 結果　micro先物+12,700円
#####      プットOP  -12,000円
###### 手数料負け 
"""
"""
###
"""
"""
##### ⓶ベア・シンセティック
##### micro225先物9限 37,620 3枚買い
#####
##### ミニプットオプション 9月限
###### 権利行使価格34,000
###### プット1枚買い@165
#####
##### ミニコールオプション 9月限
###### 権利行使価格41,000
###### コール1枚売り@75
#####
##### 結果　micro先物+19,050円
#####      プットOP  -7,300円
#####      コールOP売り+200円
###### 差引+11,950円
###
###
##### ⚠️今週のOP戦略はプロテクティブ・プット
###### ⏹下落に比重を置いた戦略。上昇でも一定の利益。
######
##### プロティクティブ・プット
##### micro225先物9限 38,2900 2枚買い
#####
##### ミニプットオプション 9月限
###### 権利行使価格35,000
###### プット1枚買い@130 2枚買い
"""

Image5 = Image.open('oct.jpg')
st.image(Image5,caption='プロテクティブ・プット損益図',use_column_width=True)


st.write('ご訪問ありがとうございます')

