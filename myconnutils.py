import pymysql
import constants


def my_db_connection():
    user_login = constants.DB_USER_LOGIN
    user_pass = constants.DB_USER_PASS
    s_host = constants.S_HOST
    s_db = constants.S_DB

    my_db = pymysql.connect(
        user=user_login,
        passwd=user_pass,
        host=s_host,
        database=s_db
    )
    return my_db
