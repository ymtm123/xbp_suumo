# xbp_suumo

## 分析手法の種類
- 分析手法は3つ
- それぞれにおいて特定の路線でも分析可能

## 細かい設定
- 全ての関数において
  - graph_widthでグラフの横幅を設定可能
  - graph_heightでグラフの縦幅を設定可能
    - 例：df.average_bar("間取り", "面積", graph_width=8, graph_height=6)
- scatter_line()とscatter_station()において
  - xlimで横軸の目盛の範囲を設定可能
  - ylimで横軸の目盛の範囲を設定可能
    - 例：df.scatter_line("面積", "家賃", xlim=(20, 40), ylim=(6, 10))
