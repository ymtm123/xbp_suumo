from utils_suumo import suumo
import importlib
importlib.reload(suumo)

text = """
名称、カテゴリー、アドレス、アクセス
路線、駅、バス停、
MMまで、バス、徒歩、車、合計時間
築年数、構造、階数、
家賃、管理費、敷金、礼金
間取り、面積、URL
"""

# データの読み込み
df = suumo.read_csv("./data/yokohama_kawasaki.csv", index_col=0, encoding="utf-8")

# データ分析
# df.n_rooms("駅")
# df.n_rooms_by_line(["京急本線", "京急逗子線"], "駅")
df.n_rooms_by_anything({
                        "路線": ["ＪＲ南武線", "東急東横線"],
                        "カテゴリー": ["賃貸マンション"],
                        "間取り": ["ワンルーム", "1K"],
                        },
                        "駅")

# df.average_bar("駅", "家賃")
# df.average_bar_by_line(["ＪＲ南武線", "東急東横線"], "駅", "家賃")
df.average_bar_by_anything({
                            "路線": ["ＪＲ南武線", "東急東横線"],
                            "カテゴリー": ["賃貸マンション"],
                            "間取り": ["ワンルーム", "1K"],
                            },
                            "駅", "家賃")

# df.scatter_line("面積", "家賃")
df.scatter_line_by_anything({
                            "カテゴリー": ["賃貸マンション"],
                            "間取り": ["ワンルーム", "1K"],
                            },
                            "面積", "家賃")

# df.scatter_station(["京急本線", "京急逗子線"], "面積", "家賃")
df.scatter_station_by_anything({
                                "路線": ["ＪＲ南武線", "東急東横線"],
                                "カテゴリー": ["賃貸マンション"],
                                "間取り": ["ワンルーム", "1K"],
                                },
                                "面積", "家賃")

