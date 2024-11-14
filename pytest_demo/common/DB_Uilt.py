import pymysql


# 创建连接
def db_conn():
    conn = pymysql.connect(host='rm-2ze84b9b42xq1t0owzo.mysql.rds.aliyuncs.com',
                           user='bjlichi',
                           password='XoA^2u$MrXBjpSdoX',
                           database='sh_lichi')
    return conn


def db(orderid):
    try:
        with db_conn() as conn:
            with conn.cursor() as cursor:
                sql = "DELETE FROM t_order_main WHERE user_id = %s AND order_id = %s"
                cursor.execute(sql, ('79490e7fcc7011ed8a0200163e26d3c4', orderid))
                # DELETE 操作不需要 fetchall，因为它不返回结果集
                conn.commit()
                print(f"Order {orderid} deleted successfully.")
    except pymysql.MySQLError as e:
        print(f"Error occurred: {e}")
    finally:
        # 在这个上下文中，不需要显式关闭连接，因为 with 语句会自动处理
        pass

    # 调用函数


db(orderid="SHA240408163051317km")
