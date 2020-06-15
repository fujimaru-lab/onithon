# encoding utf-8
from dao import psgr_db_conn
from log import batch_logger

# ロガーの取得
logger = batch_logger.BatchLog(__file__)

def reg_prsv_method_data(record, script_nm):
    """
    保存方法情報をデータベースに取り込む
    """
    prsv_method_id = record[0]
    prsv_text = record[1].rstrip('\r\n')
    logger.debug(logger.create_msg('処理レコード：({0}, {1})', prsv_method_id, prsv_text))
    try:
        conn = psgr_db_conn.Connection()
        cursor = conn.cursor()
        # upsert処理
        upsert = """
            insert into prsv_method
            values (%s, %s, %s, now(), %s, now())
            on conflict (prsv_method_id)
            do update set
                prsv_text = %s,
                upd_user = %s,
                upd_date = now()
            ;
            """
        sql_param = (prsv_method_id, prsv_text, script_nm, script_nm, prsv_text, script_nm)
        cursor.execute(upsert, sql_param)
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()
