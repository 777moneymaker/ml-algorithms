import pandas as pd
from sklearn import model_selection

df = pd.read_csv("spam_ham_dataset.csv")
df = df[["text", "label_num"]]
df["text"] = df["text"].astype(str).str.replace("\n", "")
df["text"] = df["text"].astype(str).str.replace("\r", "")
df["text"] = df["text"].astype(str).str.replace("Subject:", "")
df["label_num"] = df["label_num"].astype(int)
df["label_num"] = df["label_num"].replace(0, -1)

df_train, df_test = model_selection.train_test_split(df, test_size=0.1)

df_train.to_csv("spam_train.csv", header=True, index=False)
df_test.to_csv("spam_test.csv", header=True, index=False)
