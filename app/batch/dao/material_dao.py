# encoding utf-8
from dao import psgr_db_conn

def reg_material_data(record, scpt_nm):
    material_id = record[0]
    material_name = record[1]

    try:
        conn = psgr_db_conn.Connection()
        cursor = conn.cursor()
        
        # キーに対応するレコードを(削除)
        sql01 = """
            delete from material
            where
                material_id = '%s'
            ;
            """
        cursor.execute(sql01 % material_id)
        
        # 引数として受け取ったレコードを登録
        sql02 = """
            insert into material
            values (%s, %s, %s, now(), %s, now())
            ;
            """
        params = (material_id, material_name, scpt_nm, scpt_nm)
        cursor.execute(sql02, params)
        conn.commit()
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()
