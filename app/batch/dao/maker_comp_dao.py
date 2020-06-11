# encoding utf-8
from dao import psgr_db_conn

def reg_maker_comp_data (record, script_nm):
    """
    パースされたCSVレコードをもとに製造会社情報を登録する
    """
    maker_comp_id = record[0]
    maker_name = record[1]

    try:
        conn = psgr_db_conn.Connection()
        cursor = conn.cursor()

        upsrt = """
            insert into maker_comp
            values (%s, %s, %s, now(), %s, now())
            on conflict(maker_comp_id)
            update set
                maker_name = %s
                upd_user = %s,
                upd_date = now()
            ;
            """
        sqlparam = (maker_comp_id, maker_name, script_nm, script_nm, maker_name, script_nm)
        cursor.execute(upsrt, sqlparam)
        conn.commit()
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()
