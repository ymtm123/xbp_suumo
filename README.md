# xbp_suumo

## 分析手法の種類
- 分析手法は3つ
- それぞれにおいて特定の路線でも分析可能

## 細かい設定
- 全ての関数
  - graph_widthでグラフの横幅を設定可能
  - graph_heightでグラフの縦幅を設定可能
- scatter_line()とscatter_station()
  - xlimで横軸の目盛の範囲を設定可能
  - ylimで横軸の目盛の範囲を設定可能
    - 例：df.scatter_line("面積", "家賃", xlim=(20, 40), ylim=(6, 10))
