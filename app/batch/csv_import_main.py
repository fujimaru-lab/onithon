# encoding utf-8
import csv
import re
import psycopg2
import sys
sys.path.append('batch/dao')
import dao.material_dao as m_dao
import os

def import_csv(file_path):
    script_nm = os.path.basename(sys.argv[0])
    with open(file_path, newline='', encoding='utf-8_sig') as csvfile:
        csvreader = csv.reader(csvfile)
        
        # CSVファイルの命名規則 ###############################
        # <テーブル名>-data.csv
        # ####################################################
        filename = re.split('/', re.split('-', file_path)[0])
        tbl_nm = filename[len(filename) - 1]
        for record in csvfile:
            if tbl_nm == "material":
                m_dao.reg_material_data(re.split(',', record), script_nm)
            elif tbl_nm == "material_set":
                pass
            elif tbl_nm == "prsv_method":
                pass
            elif tbl_nm == "maker_comp":
                pass
            elif tbl_nm == "prod_base":
                pass
            elif tbl_nm == "prod_sale":
                pass
            else:
                print("no match")

    csvfile.close()

if __name__ == "__main__":
    filepath = sys.argv[1]
    import_csv(filepath)
