import numpy as np
import pandas as pd

from sklearn import metrics

vals = pd.read_csv("spam_test.csv")["label_num"].astype(int).to_numpy()
vals[vals == 0] = -1
with open("predictions.txt") as fh:
    pred = np.array([int(val.strip()) for val in fh])

tp = ((vals == 1) & (pred == 1)).sum()
tn = ((vals == -1) & (pred == -1)).sum()
fp = ((vals == -1) & (pred == 1)).sum()
fn = ((vals == 1) & (pred == -1)).sum()

print(f"Accuracy = {(vals == pred).sum() / len(pred)}")
print(f"Precision = {tp / (tp + fp)}")
print(f"Recall = {tp / (tp + fn)}")
