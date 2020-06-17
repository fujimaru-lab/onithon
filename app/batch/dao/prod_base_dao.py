# encoding utf-8
from dao import psgr_db_conn
from log import batch_logger

# ロガーの取得
logger = batch_logger.BatchLog(__file__)


def reg_prod_base_data(record, scpt_nm):
    '''
    引数として渡されたレコードをもとに商品基本情報を登録する
    '''
    prod_jan = record[0]
    prod_name = record[1]
    material_set_id = record[2]
    exprat_unit = record[3]
    exprat_term = record[4]
    prsv_method_id = record[5].rstrip('\r\n')

    logger.debug("処理レコード：({0}, {1}, {2}, {3}, {4}, {5})", prod_jan, prod_name, material_set_id, exprat_unit, exprat_term, prsv_method_id)

    try:
        conn = psgr_db_conn.Connection()
        cursor = conn.cursor()

        # 商品基本情報の登録・更新
        upsert_prod_base = """
            insert into prod_base
            values ({0}, {1}, {2}, {3}, {4}, {5}, {6}, now(), {6}, now())
            on conflict(prod_jan)
            do update set
                prod_name = {1},
                material_set_id = {2},
                exprat_unit = {3},
                exprat_tarm = {4},
                prsv_method_id = {5},
                upd_user = {6},
                upd_date = now()
            ;
            """

        sql_param = (prod_jan, prod_name, material_set_id, exprat_unit, exprat_term, prsv_method_id, scpt_nm)
        cursor.execute(upsert_prod_base)
    except Exception as e:
        conn.rollback()
        raise(e)
    finally:
        cursor.close()
        conn.close()