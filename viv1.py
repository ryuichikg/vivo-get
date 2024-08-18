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

st.text('更新日8月18日')
st.text(datetime.date.today())

"""
##### ⚠️今週のロング銘柄ショート銘柄
###### 
"""

df1 = pd.DataFrame({

     '買い銘柄':['KIMOTO','北の達人','ニッスイ','清水建設','リソー教育'],
     '現在価格':['241','171','874.1','916.9','237'],
     '目標価格':['260','200','915','950','275']
 })
df1

df2 = pd.DataFrame({
     '売り銘柄':['スカイマーク','コニカミノルタ','広済堂HD','京都きもの友禅HD','帝国ホテル'],
     '現在価格':['659','396.1','468','103','879'],
     '目標価格':['640','370','425','95','850']
 })
df2

#st.dataframe(df)
st.write('１．プライム市場の主要銘柄を選定。一部例外有り。')
st.write('２．各々３銘柄を売買い保有')
st.write('３．一定の利益または損失がでたら一括決済')
txt1 = '<p style="color:blue;">先週の実績 買い推奨５銘柄計 ---%</p>'
st.write(txt1, unsafe_allow_html=True)
txt2 = '<p style="color:red;">先週の実績 売り推奨５銘柄計 ---%</p>'
st.write(txt2, unsafe_allow_html=True)


"""
#####  ✅ＮＴ倍率
"""
df3 = pd.DataFrame({
    '指数':['日経平均225'],
    '現在価格':['37640'],
    '上値抵抗':['38250'],
    '下値支持':['36700']
})
df3

df4 = pd.DataFrame({
    '指数':['TOPIX'],
    '現在価格':['2696'],
    '上値抵抗':['2720'],
    '下値支持':['2593']
})
df4

data = pd.DataFrame({
    'NT':['上値抵抗','現在','下値支持'],
    'レシオ':['14.40','14.21','13.85']
    })
data

st.write('14.00付近でレンジ。上下バックに逆張り戦略。')
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
 ##### ※7月の高値42,512円から8月の安値30,301円のフィボナッチ61.8%戻し達成。
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
##### ⚠️先週のOP戦略は「プロテクティブ・プット」又は「NTレシオの短期トレード」
##### マイクロ先物9限 35,800 2枚買い
##### ミニプットオプション 8月3W限
##### 権利行使価格32,000
##### プット1枚買い@80
##### 想定証拠金40,000円
###### SQ持込せずに一定の利益で決済予定
##### 結果 SQ値 37,609円
##### 先物+36,180円 オプション-8,000円　計+28,180円

"""
"""
##
"""
"""
##### ⚠️今週のOP戦略は「⓵プロテクティブ・プット」又は「⓶ベア・シンセティック」
###### ⏹ベア・シンセティック（カバード・コールとプロティクティブ・プットの合成）
######
##### ⓵プロティクティブ・プット
##### micro225先物9限 37,620 2枚買い
#####
##### ミニプットオプション 9月限
###### 権利行使価格35,000
###### プット1枚買い@250
#####
##### 想定証拠金80,000円
###### SQ持込せずに一定の利益で決済予定
"""
Image5 = Image.open('oct.jpg')
st.image(Image5,caption='プロティクティブ・プット損益図',use_column_width=True)

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
##### 想定証拠金127,000円
###### 適宜一定の利益で利確・決済予定
"""
Image6 = Image.open('oct2.jpg')
st.image(Image6,caption='ベア・シンセティック損益図',use_column_width=True)


st.write('ご訪問ありがとうございます')

