import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- 1. ページ基本設定 & カスタムCSS（洗練されたダークテーマ） ---
st.set_page_config(page_title="AlphaPosition Pro", layout="wide")

st.markdown("""
    <style>
    /* 全体のバックグラウンドとフォント */
    .main {
        background-color: #0e1117;
        color: #e0e6ed;
    }
    /* ヘッダーのスタイル */
    .main-header {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #f39c12; /* ゴールドアクセント */
        font-weight: 700;
        text-align: center;
        margin-bottom: 30px;
    }
    /* カード風のコンテナ */
    .metric-card {
        background-color: #1a1c23;
        border: 1px solid #2d3139;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>📊 AlphaPosition Pro <span style='font-size:0.5em; color:#888;'>| FX & CFD Position Analyzer</span></h1>", unsafe_allow_html=True)

# --- 2. 定数・仕様設定 ---
LEVERAGE = 2000
SYMBOLS = [
    "USD/JPY", "EUR/USD", "GBP/USD", "AUD/USD", "USD/CHF",
    "EUR/JPY", "GBP/JPY", "AUD/JPY", "EUR/GBP", "NZD/USD",
    "XAU/USD (Gold)", "XAG/USD (Silver)", "WTI_Oil", "BRENT_Oil",
    "US30 (Dow)", "US500 (S&P500)", "NAS100 (Nasdaq)", "JP225 (Nikkei)",
    "UK100", "DE40"
]

# --- 3. サイドバー：ポジション入力 ---
st.sidebar.header("🛠️ ポジション入力")
selected_symbol = st.sidebar.selectbox("対象銘柄を選択", SYMBOLS)
current_price = st.sidebar.number_input("現在の市場価格 (参考)", value=150.000, format="%.3f", step=0.001)

st.sidebar.markdown("---")
st.sidebar.subheader("➕ 新規ポジション追加")

# セッション状態の初期化（複数ポジション保持用）
if "positions" not in st.session_state:
    st.session_state.positions = []

with st.sidebar.form(key="position_form", clear_on_submit=True):
    pos_type = st.selectbox("売買", ["BUY", "SELL"])
    entry_price = st.number_input("エントリー価格", value=current_price, format="%.3f", step=0.001)
    lots = st.number_input("ロット数 (1ロット=100,000通貨想定 / Goldは100オンス想定)", value=0.1, format="%.3f", step=0.01)
    contract_size = st.number_input("契約サイズ (1ロットあたりの通貨数/単位)", value=100000 if "XAU" not in selected_symbol else 100, step=100)
    
    submit_button = st.form_submit_button(label="ポジションを追加")
    
    if submit_button:
        st.session_state.positions.append({
            "ID": len(st.session_state.positions) + 1,
            "TYPE": pos_type,
            "ENTRY": round(entry_price, 3),
            "LOTS": round(lots, 3),
            "SIZE": contract_size
        })

# ポジション全削除ボタン
if st.sidebar.button("全ポジションをクリア"):
    st.session_state.positions = []
    st.rerun()

# --- 4. メインコンテンツ：データ処理 ---
df = pd.DataFrame(st.session_state.positions)

if not df.empty:
    # 損益計算ロジック (簡易版: 買いは (現在-エントリー)*ロット*サイズ, 売りは逆)
    def calc_pnl(row, price):
        if row["TYPE"] == "BUY":
            return (price - row["ENTRY"]) * row["LOTS"] * row["SIZE"]
        else:
            return (row["ENTRY"] - price) * row["LOTS"] * row["SIZE"]

    # 必要証拠金計算 (レバレッジ2000倍)
    # 証拠金 = (エントリー価格 * ロット数 * 契約サイズ) / レバレッジ
    def calc_margin(row):
        return (row["ENTRY"] * row["LOTS"] * row["SIZE"]) / LEVERAGE

    df["現在の損益"] = df.apply(lambda r: calc_pnl(r, current_price), axis=1)
    df["必要証拠金 (推定)"] = df.apply(calc_margin, axis=1)

    # 1. サマリーメトリクスの計算
    total_buy_lots = df[df["TYPE"] == "BUY"]["LOTS"].sum()
    total_sell_lots = df[df["TYPE"] == "SELL"]["LOTS"].sum()
    net_pnl = df["現在の損益"].sum()
    total_margin = df["必要証拠金 (推定)"].sum()

    # 損益分岐点 (BEP) の計算
    # ネットのロット方向と必要総額からブレイクイーブンを算出
    bep = 0.0
    net_lots = total_buy_lots - total_sell_lots
    
    # 全ポジションのエントリーに必要な総対価の差分から計算
    buy_value = sum(r["ENTRY"] * r["LOTS"] * r["SIZE"] for _, r in df[df["TYPE"] == "BUY"].iterrows())
    sell_value = sum(r["ENTRY"] * r["LOTS"] * r["SIZE"] for _, r in df[df["TYPE"] == "SELL"].iterrows())
    
    # 加重平均的なアプローチ（簡易的に同一契約サイズを想定）
    # 両建てが完全に相殺されている(net_lots=0)場合は損益が固定されるためBEPは存在しない
    if abs(net_lots) > 0.0001:
        # 損益が0になる価格 P を求める方程式: ∑PnL = 0
        # Buy_Lots * (P - Entry) * Size - Sell_Lots * (P - Entry) * Size = 0 的な総和
        # 簡易計算のため、同一サイズ前提、またはサイズ考慮の加重
        total_buy_unit = sum(r["LOTS"] * r["SIZE"] for _, r in df[df["TYPE"] == "BUY"].iterrows())
        total_sell_unit = sum(r["LOTS"] * r["SIZE"] for _, r in df[df["TYPE"] == "SELL"].iterrows())
        
        bep = (buy_value - sell_value) / (total_buy_unit - total_sell_unit)
    else:
        bep = None

    # --- 5. UIレイアウト: ダッシュボードメトリクス ---
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"<div class='metric-card'><h5>現在の合計損益</h5><h2 style='color: {'#2ecc71' if net_pnl >= 0 else '#e74c3c'};'>{net_pnl:+,.3f}</h2></div>", unsafe_allow_html=True)
    with col2:
        bep_text = f"{bep:.3f}" if bep is not None else "両建て相殺中"
        st.markdown(f"<div class='metric-card'><h5>全体損益分岐点 (BEP)</h5><h2 style='color: #f1c40f;'>{bep_text}</h2></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='metric-card'><h5>保有ロット (BUY / SELL)</h5><h2 style='color: #3498db;'>{total_buy_lots:.3f} / {total_sell_lots:.3f}</h2></div>", unsafe_allow_html=True)
    with col4:
        st.markdown(f"<div class='metric-card'><h5>総必要証拠金 (Lev 2000)</h5><h2>{total_margin:,.3f}</h2></div>", unsafe_allow_html=True)

    st.markdown("---")

    # --- 6. 損益図 (Payoff Diagram) の描画 ---
    st.subheader("📈 総ポジションの損益ダイアグラム")
    
    # グラフの価格範囲（エントリー価格の最小〜最大、±α）
    min_entry = df["ENTRY"].min()
    max_entry = df["ENTRY"].max()
    padding = (max_entry - min_entry) * 0.5 if min_entry != max_entry else min_entry * 0.05
    if padding == 0: padding = 1.0
    
    price_range = np.linspace(min_entry - padding, max_entry + padding, 200)
    
    # 各価格時点での総損益を計算
    total_pnl_range = []
    for p in price_range:
        pnl_sum = sum(calc_pnl(row, p) for _, row in df.iterrows())
        total_pnl_range.append(pnl_sum)
        
    fig = go.Figure()
    # 損益曲線
    fig.add_trace(go.Scatter(x=price_range, y=total_pnl_range, mode='lines', name='総損益', line=dict(color='#f39c12', width=3)))
    # 現在価格の垂直線
    fig.add_vline(x=current_price, line_dash="dash", line_color="#3498db", annotation_text=f"現在価格: {current_price:.3f}", annotation_position="top left")
    # 損益分岐点の垂直線
    if bep is not None and min_entry - padding <= bep <= max_entry + padding:
        fig.add_vline(x=bep, line_dash="dot", line_color="#2ecc71", annotation_text=f"BEP: {bep:.3f}", annotation_position="bottom right")
    # 損益0の水平線
    fig.add_hline(y=0, line_color="#7f8c8d", line_width=1)

    fig.update_layout(
        title=f"{selected_symbol} 評価損益シミュレーション",
        xaxis_title="市場価格",
        yaxis_title="損益",
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='#1a1c23',
        font=dict(color="#e0e6ed")
    )
    st.plotly_chart(fig, use_container_width=True)

    # --- 7. 保有ポジション一覧テーブル ---
    st.subheader("📋 現在の保有ポジション一覧")
    
    # 表示用にフォーマット
    disp_df = df.copy()
    disp_df["ENTRY"] = disp_df["ENTRY"].map(lambda x: f"{x:.3f}")
    disp_df["LOTS"] = disp_df["LOTS"].map(lambda x: f"{x:.3f}")
    disp_df["現在の損益"] = disp_df["現在の損益"].map(lambda x: f"{x:+.3f}")
    disp_df["必要証拠金 (推定)"] = disp_df["必要証拠金 (推定)"].map(lambda x: f"{x:,.3f}")
    
    st.dataframe(disp_df[["ID", "TYPE", "ENTRY", "LOTS", "SIZE", "現在の損益", "必要証拠金 (推定)"]], use_container_width=True)

else:
    # ポジションが空の時の案内
    st.info("👈 左側のサイドバーからポジションを入力して追加してください。ゴールドや為替など主要20銘柄に対応しています。")
    
    # デザイン確認用のモック背景画像代わりとしてプレースホルダーを表示
    st.markdown("""
    <div style='text-align: center; padding: 100px; color: #555;'>
        <h3>No Active Positions</h3>
        <p>ポジションを追加すると、ここにリアルタイムな損益分岐点分析とペイオフダイアグラムが表示されます。</p>
    </div>
    """, unsafe_allow_html=True)