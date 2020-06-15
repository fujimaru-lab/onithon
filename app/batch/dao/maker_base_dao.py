# encoding utf-8
from dao import psgr_db_conn
from log import batch_logger
# ロガーの取得
logger = batch_logger.BatchLog(__file__)

def reg_maker_base_data(record, scrpt_nm):
    """
    パースされたCSVレコードをもとに製造会社製造拠点情報を登録する
    """
    maker_comp_id = record[0]
    maker_base_id = record[1]
    base_name = record[2]
    base_adrs = record[3]
    base_tel = record[4]
    logger.debug(logger.create_msg('処理レコード：{0}', record))
    try:
        conn = psgr_db_conn.Connection()
        cursor = conn.cursor()

        upsrt = """
            insert into maker_base
            values (%s, %s, %s, %s, %s, %s, now(), %s, now())
            on conflict (maker_comp_id, maker_base_id)
            update set
                base_name = %s,
                base_adrs = %s,
                base_tel = %s,
                upd_user = %s,
                upd_date = now()
            """
        sql_param = (maker_comp_id, maker_base_id, base_name, base_adrs, base_tel, scrpt_nm, scrpt_nm, base_name, base_adrs, base_tel, scrpt_nm)
        cursor.execute(upsrt, sql_param)
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()
