# !/bin/sh
# CSVファイルデータ取得処理起動用シェルスクリプト

echo '処理開始'

# sample_dataフォルダを操作しファイル名を取得
data_folder='C:/Users/yoshi/Documents/01.CodingSpace/08.Python/app/batch/sample_data/'
files=`ls ${data_folder}`

for file in ${files[*]}
do
    # ファイル名を引数としてcsv_import_main.pyを起動
    echo ${file}
    py C:/Users/yoshi/Documents/01.CodingSpace/08.Python/app/batch/csv_import_main.py "${data_folder}/${file}"
done

echo '処理終了'