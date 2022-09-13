import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

"""
名称、カテゴリー、アドレス、アクセス
路線、駅、バス停、
乗換時間、バス、徒歩、車、合計時間（分）
築年数、構造、階数、
家賃、管理費、敷金、礼金（万円）
間取り、面積、URL
"""
########################
targets = ["京急本線", "京急逗子線"]
factor_1 = "築年数"
factor_2 = "家賃"
########################

font_manager.fontManager.addfont("./fonts/ipaexg.ttf")
matplotlib.rc('font', family="IPAexGothic")

df = pd.read_csv("./data/yokohama_kawasaki.csv", encoding='utf-8')
df = df[df["路線"].isin(targets)]
df_group = df.groupby(["駅"]).mean()

X = df_group.loc[:, factor_1]
Y = df_group.loc[:, factor_2]
T = df_group.index

fig, ax = plt.subplots(figsize=(6.4, 4.8), nrows=1, ncols=1)
ax.scatter(X, Y)
ax.set_xlabel(factor_1)
ax.set_ylabel(factor_2)
for x, y, t in zip(X, Y, T):
    ax.annotate(t, xy=(x, y), size=10)
plt.title("と".join(targets) + f"の{factor_1}と{factor_2}")

fig.subplots_adjust(wspace=0.1, top=0.96)
# fig.patch.set_alpha(0)  # 余白を透明にする場合
# ax.patch.set_alpha(0)  # プロット部分を透明にする場合
plt.savefig("./graph/{}.png".format("と".join(targets) + f"の{factor_1}と{factor_2}"), bbox_inches='tight', pad_inches=0.1, dpi=200)
