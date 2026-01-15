import pandas as pd
import uproot
import numpy as np
import awkward as ak

# 入力 CSV ファイル
train_csv = "training.csv"
test_csv  = "test.csv"

# 出力 ROOT ファイル
output_root = "higgs.root"

# ========== CSV 読み込み ==========
df_train = pd.read_csv(train_csv)
df_test  = pd.read_csv(test_csv)

# TTree 名
train_tree_name = "trainingTree"
test_tree_name  = "testTree"

# ========== Pandas → Awkward Array 変換 ==========
def df_to_awkward(df):
    data = {}
    for col in df.columns:
        # ROOT は string を扱えないので、Label などは int に変換する
        if df[col].dtype == object:
            try:
                data[col] = df[col].astype(float).values
            except:
                # 例えば Label: 's'/'b' を 1/0 に変換
                if col.lower() == "label":
                    data[col] = (df[col] == "s").astype(np.int32).values
                else:
                    raise ValueError(f"Cannot convert column {col} to numeric.")
        else:
            data[col] = df[col].values
    return ak.Array(data)

ak_train = df_to_awkward(df_train)
ak_test  = df_to_awkward(df_test)

# ========== ROOT ファイルへ書き込み ==========
with uproot.recreate(output_root) as f:
    f[train_tree_name] = ak_train
    f[test_tree_name]  = ak_test

print(f"ROOT file successfully written to: {output_root}")
print(f"Trees: {train_tree_name}, {test_tree_name}")
