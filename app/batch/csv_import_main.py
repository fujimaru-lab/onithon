# encoding utf-8
import csv
import re
import sys
sys.path.append('batch')
import dao.material_dao as m_dao
import dao.prsv_method_dao as pm_dao
import dao.maker_comp_dao as mc_dao
import dao.maker_base_dao as mb_dao
import os


def import_csv(file_path):
    """
    所定のフォルダに配置されたCSVファイルから原材料情報、原材料セット情報、保存方法情報、製造会社情報、製造会社製造拠点情報、商品基本情報を
    取り込みデータベースに登録する
    商品販売情報は取り込み対象外
    """ 
    script_nm = os.path.basename(sys.argv[0])
    try:
        with open(file_path, newline='', encoding='utf-8_sig') as csvfile:
            csvreader = csv.reader(csvfile)
            
            # CSVファイルの命名規則 ###############################
            # <テーブル名>-data.csv
            # ####################################################
            filename = re.split('/', re.split('-', file_path)[0])
            tbl_nm = filename[len(filename) - 1]
            for record in csvfile:
                if tbl_nm == "material":
                    # 原材料情報、原材料セット情報取り込み
                    m_dao.reg_material_data(re.split(',', record), script_nm)
                elif tbl_nm == "prsv_method":
                    # 保存方法情報取り込み
                    pm_dao.reg_prsv_method_data(re.split(',', record), script_nm)
                elif tbl_nm == "maker_comp":
                    # 製造会社情報取り込み
                    mc_dao.reg_maker_comp_data(re.split(',', record), script_nm)
                elif tbl_nm == "maker_base":
                    # 製造会社製造拠点情報取り込み
                    mb_dao.reg_maker_base_data(re.split(',', record), script_nm)
                elif tbl_nm == "prod_base":
                    # 商品基本情報取り込み
                    pass
                else:
                    print(filename, "is not subject to csv-import")
                    break
            
    except Exception as e:
        print(e)
    finally:
        csvfile.close()


if __name__ == "__main__":
    filepath = sys.argv[1]
    import_csv(filepath)
