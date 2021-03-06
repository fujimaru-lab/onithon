# encoding utf-8
from dao import psgr_db_conn
from log import batch_logger

# ロガーの取得
logger = batch_logger.BatchLog(__file__)

# csvレコードの想定
# 00001,00001,砂糖
# 00001,00002,塩
# 00002,00001,砂糖
# 00002,00003,人参
def reg_material_data(record, scpt_nm):
    '''
    引数として渡されたレコードをもとに、原材料情報を登録・更新、原材料セット情報を登録する
    '''
    material_set_id = record[0]
    material_id = record[1]
    material_name = record[2].rstrip('\r\n')
    logger.debug('処理レコード：({0}, {1}, {2})', material_set_id, material_id, material_name)
    try:
        conn = psgr_db_conn.Connection()
        cursor = conn.cursor()
        
        # 原材料情報の登録・更新
        upsert_material = """
            insert into material
            values (%s, %s, %s, now(), %s, now())
            on conflict (material_id)
            do update set
                material_name = %s,
                upd_user = %s,
                upd_date = now()
            ;
            """
        sql_param01 = (material_id, material_name, scpt_nm, scpt_nm, material_name, scpt_nm)
        cursor.execute(upsert_material, sql_param01)

        # 原材料セット情報の登録
        if not (count_material_set(material_set_id, material_id) > 0):
            insert_material_set = """
                insert into material_set
                values (%s, nextval('material_set_material_seq_no_seq'), %s, %s, now(), %s, now())
                ;
                """
            sql_param02 = (material_set_id, material_id, scpt_nm, scpt_nm)
            cursor.execute(insert_material_set, sql_param02)
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

def count_material_set(material_set_id, material_id):
    count = 0
    try:
        conn = psgr_db_conn.Connection()
        cursor = conn.cursor()

        sql = """
            select * from material_set
            where
                material_set_id = %s
            and material_id = %s
            ;
            """
        cursor.execute(sql, (material_set_id, material_id))
        count = cursor.rowcount
        logger.debug('(material_set_id={0}, material_id={1}):{2}件', material_set_id, material_id, count)
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()
    return count
