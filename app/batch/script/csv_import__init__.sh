# !/bin/sh
# CSVファイルデータ取得処理起動用シェルスクリプト

echo 'CSVファイルデータ取得処理起動用シェルスクリプト：処理開始'

# 設定ファイルの読み込み
source ./onithon_conf.sh

# sample_dataフォルダを操作しファイル名を取得
files=`ls ${CSV_DATA_DIR}`

for file in ${files[*]}
do
    # ファイル名を引数としてcsv_import_main.pyを起動
    echo "${file} を処理開始"
    py ${PY_CSV_IMPORT} "${CSV_DATA_DIR}/${file}"
done

echo 'CSVファイルデータ取得処理起動用シェルスクリプト：処理終了'