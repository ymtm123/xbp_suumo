import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager


class SuumoDataFrame(pd.DataFrame):

    # 日本語の設定
    font_manager.fontManager.addfont("./fonts/ipaexg.ttf")
    matplotlib.rc("font", family="IPAexGothic")

    def n_rooms(self, factor, graph_width=12, graph_height=3):
        # 指定された列のカウント取得
        df_count = self[factor].value_counts()

        # グラフのサイズなどの指定
        fig, ax = plt.subplots(figsize=(graph_width, graph_height), nrows=1, ncols=1)

        # 棒グラフの表示
        ax.bar(df_count.index, df_count.values)
        _ = plt.xticks(rotation=90)
        _ = plt.title(f"{factor}別物件数")

        # グラフの調整
        fig.subplots_adjust(wspace=0.1, top=0.96)
        # fig.patch.set_alpha(0)  # 余白を透明にする場合
        # ax.patch.set_alpha(0)  # プロット部分を透明にする場合

        # グラフの保存
        plt.savefig(
            "./graph/{}.png".format(f"{factor}別物件数"),
            bbox_inches="tight",
            pad_inches=0.1,
            dpi=200,
        )

    def average_bar(self, factor_1, factor_2, graph_width=12, graph_height=3):
        numeric_df = self.select_dtypes(include='number')  # 数値の列のみを抽出

        # 指定された列における各項目の平均値の取得
        # df_group = self.groupby([factor_1]).mean().sort_values(factor_2, ascending=False)
        df_group = numeric_df.groupby(self[factor_1]).mean().sort_values(by=factor_2, ascending=False)

        # グラフのサイズなどの指定
        fig, ax = plt.subplots(figsize=(graph_width, graph_height), nrows=1, ncols=1)

        # 棒グラフの表示
        ax.bar(df_group.index, df_group[factor_2])

        # グラフの調整
        _ = plt.xticks(rotation=90)
        _ = plt.title(f"{factor_1}別の平均{factor_2}")
        fig.subplots_adjust(wspace=0.1, top=0.96)
        # fig.patch.set_alpha(0)  # 余白を透明にする場合
        # ax.patch.set_alpha(0)  # プロット部分を透明にする場合

        # グラフの保存
        plt.savefig(
            "./graph/{}.png".format(f"{factor_1}別の平均{factor_2}"),
            bbox_inches="tight",
            pad_inches=0.1,
            dpi=200,
        )

    def scatter_line(self, factor_1, factor_2, graph_width=6.4, graph_height=4.8, xlim=None, ylim=None):
        numeric_df = self.select_dtypes(include='number')  # 数値の列のみを抽出

        # 指定された列における駅ごとの各項目の平均値の取得
        # df_group = self.groupby(["路線"]).mean()
        df_group = numeric_df.groupby(self["路線"]).mean()
        X = df_group.loc[:, factor_1]
        Y = df_group.loc[:, factor_2]
        T = df_group.index

        # グラフのサイズなどの指定
        fig, ax = plt.subplots(figsize=(graph_width, graph_height), nrows=1, ncols=1)

        # 散布図の表示
        ax.scatter(X, Y)

        # グラフの軸の調整
        if xlim is not None:
            ax.set_xlim(xlim)
        if ylim is not None:
            ax.set_ylim(ylim)

        # グラフの調整
        ax.set_xlabel(factor_1)
        ax.set_ylabel(factor_2)
        for x, y, t in zip(X, Y, T):
            ax.annotate(t, xy=(x, y), size=10)
        plt.title(f"{factor_1}と{factor_2}")
        fig.subplots_adjust(wspace=0.1, top=0.96)
        # fig.patch.set_alpha(0)  # 余白を透明にする場合
        # ax.patch.set_alpha(0)  # プロット部分を透明にする場合

        # グラフの保存
        plt.savefig(
            "./graph/{}.png".format(f"{factor_1}と{factor_2}"),
            bbox_inches="tight",
            pad_inches=0.1,
            dpi=200,
        )

    def n_rooms_by_line(self, targets, factor, graph_width=12, graph_height=3):
        # ある路線の指定された列のカウント取得
        df = self[self["路線"].isin(targets)]
        df_count = df[factor].value_counts()

        # グラフのサイズなどの指定
        fig, ax = plt.subplots(figsize=(graph_width, graph_height), nrows=1, ncols=1)

        # 棒グラフの表示
        ax.bar(df_count.index, df_count.values)

        # グラフの調整
        _ = plt.xticks(rotation=90)
        _ = plt.title("と".join(targets) + f"の{factor}別物件数")
        fig.subplots_adjust(wspace=0.1, top=0.96)
        # fig.patch.set_alpha(0)  # 余白を透明にする場合
        # ax.patch.set_alpha(0)  # プロット部分を透明にする場合

        # グラフの保存
        plt.savefig(
            "./graph/{}.png".format("と".join(targets) + f"の{factor}別物件数"),
            bbox_inches="tight",
            pad_inches=0.1,
            dpi=200,
        )

    def average_bar_by_line(self, targets, factor_1, factor_2, graph_width=12, graph_height=3):
        # ある路線の指定された列における各項目の平均値の取得
        df = self[self["路線"].isin(targets)]
        numeric_df = self.select_dtypes(include='number')  # 数値の列のみを抽出
        # df_group = df.groupby([factor_1]).mean().sort_values(factor_2, ascending=False)
        df_group = numeric_df.groupby(df[factor_1]).mean().sort_values(factor_2, ascending=False)

        # グラフのサイズなどの指定
        fig, ax = plt.subplots(figsize=(graph_width, graph_height), nrows=1, ncols=1)

        # 棒グラフの表示
        ax.bar(df_group.index, df_group[factor_2])

        # グラフの調整
        _ = plt.xticks(rotation=90)
        _ = plt.title("と".join(targets) + f"の{factor_1}別の平均{factor_2}")
        fig.subplots_adjust(wspace=0.1, top=0.96)
        # fig.patch.set_alpha(0)  # 余白を透明にする場合
        # ax.patch.set_alpha(0)  # プロット部分を透明にする場合

        # グラフの保存
        plt.savefig(
            "./graph/{}.png".format("と".join(targets) + f"の{factor_1}別の平均{factor_2}"),
            bbox_inches="tight",
            pad_inches=0.1,
            dpi=200,
        )

    def scatter_station(self, targets, factor_1, factor_2, graph_width=6.4, graph_height=4.8, xlim=None, ylim=None):
        # ある路線の指定された列における駅ごとの各項目の平均値の取得
        df = self[self["路線"].isin(targets)]
        numeric_df = self.select_dtypes(include='number')
        # df_group = df.groupby(["駅"]).mean()
        df_group = numeric_df.groupby(df["駅"]).mean()
        X = df_group.loc[:, factor_1]
        Y = df_group.loc[:, factor_2]
        T = df_group.index

        # グラフのサイズなどの指定
        fig, ax = plt.subplots(figsize=(graph_width, graph_height), nrows=1, ncols=1)

        # 散布図の表示
        ax.scatter(X, Y)

        # グラフの軸の調整
        if xlim is not None:
            ax.set_xlim(xlim)
        if ylim is not None:
            ax.set_ylim(ylim)

        # グラフの調整
        ax.set_xlabel(factor_1)
        ax.set_ylabel(factor_2)
        for x, y, t in zip(X, Y, T):
            ax.annotate(t, xy=(x, y), size=10)
        plt.title("と".join(targets) + f"の{factor_1}と{factor_2}")
        fig.subplots_adjust(wspace=0.1, top=0.96)
        # fig.patch.set_alpha(0)  # 余白を透明にする場合
        # ax.patch.set_alpha(0)  # プロット部分を透明にする場合

        # グラフの保存
        plt.savefig(
            "./graph/{}.png".format("と".join(targets) + f"の{factor_1}と{factor_2}"),
            bbox_inches="tight",
            pad_inches=0.1,
            dpi=200,
        )


def read_csv(*args, **kwargs):
    df = pd.read_csv(*args, **kwargs)  # pandasのread_csvを使ってDataFrameを取得
    return SuumoDataFrame(df)  # 取得したDataFrameをSuumoDataFrameに変換して返す
