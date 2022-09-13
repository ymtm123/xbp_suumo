import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

########################
targets = ["京急本線", "京急逗子線"]
factor = "駅"
########################

font_manager.fontManager.addfont("./fonts/ipaexg.ttf")
matplotlib.rc('font', family="IPAexGothic")

df = pd.read_csv("./data/yokohama_kawasaki.csv", encoding='utf-8')
df = df[df["路線"].isin(targets)]
df_count = df[factor].value_counts()

fig, ax = plt.subplots(figsize=(12, 3), nrows=1, ncols=1)

# 棒グラフの表示
ax.bar(df_count.index, df_count.values)
xlabels = plt.xticks(rotation=-90)
title = plt.title("と".join(targets) + f"の{factor}別物件数")

fig.subplots_adjust(wspace=0.1, top=0.96)
# fig.patch.set_alpha(0)  # 余白を透明にする場合
# ax.patch.set_alpha(0)  # プロット部分を透明にする場合
plt.savefig("./graph/{}.png".format("と".join(targets) + f"の{factor}別物件数"), bbox_inches='tight', pad_inches=0.1, dpi=200)
