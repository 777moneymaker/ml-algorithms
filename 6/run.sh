python3 csv_split_and_fix.py
python3 csv2vw.py spam_train.csv --label label_num > spam_train.txt
python3 csv2vw.py spam_test.csv --label label_num > spam_test.txt
vw -d spam_train.txt -f model.vw --binary
vw -d spam_test.txt -i model.vw -p predictions.txt
python3 stats.py