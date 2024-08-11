# ＣＳＶやエクセルを表示させるコード

import streamlit as st
import pandas as pd
import datetime
from PIL import Image

#pd.set_option('display.unicode.east_asian_width', True)
st.title('ロング・ショート戦略')
#color = st.color_picker('summer sales contest', '#87ceeb')

txt0 = '<p style="color:red;">※8月12日は先物オプション休場。海外は通常取引のため8月13日窓開け注意！</p>'
st.write(txt0, unsafe_allow_html=True)


st.write('テスト版')

st.text('更新日8月11日')
st.text(datetime.date.today())

"""
##### ⚠️今週のロング銘柄ショート銘柄
###### 今週も個別銘柄は見合せます
"""

# df1 = pd.DataFrame({

#     '買い銘柄':['日野自動車','ラウンドワン','メドピア','コシダHD','システナ'],
#     '現在価格':['453.4','894','618','966','339'],
#     '目標価格':['460','900','650','1000','350']
# })
# df1

# df2 = pd.DataFrame({
#     '売り銘柄':['出光興産','ヤマシンフィルタ','富士石油','日産自動車','東レ'],
#     '現在価格':['960.3','440','451','466.2','767'],
#     '目標価格':['930','420','412','425','742']
# })
# df2

# #st.dataframe(df)
# st.write('１．プライム市場の主要銘柄を選定')
# st.write('２．各々３銘柄を売買い保有')
# st.write('３．一定の利益または損失がでたら一括決済')
#txt1 = '<p style="color:blue;">先週の実績 買い推奨５銘柄計 -28.53%</p>'
#st.write(txt1, unsafe_allow_html=True)
#txt2 = '<p style="color:red;">先週の実績 売り推奨５銘柄計 +28.80%</p>'
#st.write(txt2, unsafe_allow_html=True)


"""
###  ⚠️ＮＴ倍率
"""
"""
###### ⭕8/5の日経225急落でもNTレシオ取引では上昇。NT取引の優位性が見られた。
"""
df3 = pd.DataFrame({
    '指数':['日経平均225'],
    '現在価格':['35300'],
    '上値抵抗':['36000'],
    '下値支持':['33700']
})
df3

df4 = pd.DataFrame({
    '指数':['TOPIX'],
    '現在価格':['2489'],
    '上値抵抗':['2520'],
    '下値支持':['2440']
})
df4

data = pd.DataFrame({
    'NT':['上値抵抗','現在','下値支持'],
    'レシオ':['14.40','14.18','13.85']
    })
data

st.write('14.00付近でレンジ。上下バックに逆張り戦略。')
"""
### ⚠️ＮＴレシオグラフ
"""
submit = st.button('押して会員登録確定 　●万/月')
if submit == True:
    st.bar_chart(data.set_index('NT'))
    # plt.bar(df)
st.write("投資の判断は自己責任で")

image1 = Image.open('nt01.jpg')
st.image(image1, caption='NTチャート',use_column_width=True)

# """
# ### 225・XAU・NAS100チャート 
# """
# Image2 = Image.open('bt1.jpg')
# st.image(Image2,caption='225チャート日足',use_column_width=True)

# Image3 = Image.open('bt2.jpg')
# st.image(Image3,caption='XAUUSDチャート日足',use_column_width=True)

# Image4 = Image.open('bt3.jpg')
# st.image(Image4,caption='NAS100チャート日足',use_column_width=True)

"""
#### 先物・オプション：シュミレーション
"""
"""
#### ⚠️先週のOP戦略は「プロテクティブ・コール」又は「コール裸買い」
###### （プットOPは高IVで売買が厳しい為、安くなったコールで短期反発狙い）
##### マイクロ先物8限 34,800 2枚売り
##### ミニコールオプション 8月限
##### 権利行使価格37,000
##### コール1枚買い@120
##### 想定証拠金48,000円
###### SQ持込せずに一定の利益で決済予定
##### 結果 SQ値 35,661円
##### 先物-17,220円 オプション-12,000円　計-29,220円

"""
"""
##
"""
"""
#### ⚠️今週のOP戦略は「プロテクティブ・プット」又は「NTレシオの短期トレード」
###### ⏹NTレシオ 13.95～14.10でmicro2257枚BUY,miniTOPIX1枚SELL。
###### ⏹NTレシオ上記ポジションで、0.1ポイント約17,000円の±となる。
######
##### micro225先物9限 35,300 2枚買い
##### ミニコールオプション 8月3W限
##### 権利行使価格32,000
##### コール1枚買い@110
##### 想定証拠金40,000円
###### SQ持込せずに一定の利益で決済予定
"""
Image5 = Image.open('oct.jpg')
st.image(Image5,caption='オプション損益図',use_column_width=True)



st.write('ご訪問ありがとうございます')

