from werkzeug.security import generate_password_hash, check_password_hash
import myconnutils

# my_db = myconnutils.my_db_connection()
# my_cursor = my_db.cursor()


class app_user:

    def user_add(self, app_user_pass):
        app_user_login = self
        sql_formula = "INSERT INTO invent_system_users(User_Name, Pass) Values(%s,%s)"
        if app_user_login == '':
            return 'input user login'
        else:
            my_db = myconnutils.my_db_connection()
            my_cursor = my_db.cursor()
            my_cursor.execute("SELECT COUNT(1) FROM invent_system_users WHERE User_Name = %s;", [app_user_login])
            if my_cursor.fetchone()[0]:
                my_cursor.close()
                my_db.close()
                return 'User ' + app_user_login + ' is already on the List'
            else:
                app_user_pass_hash = generate_password_hash(app_user_pass, 'sha256')
                user_credentials = (app_user_login, app_user_pass_hash)
                app_user.query_execute(sql_formula, user_credentials)
                my_cursor.close()
                my_db.close()
                return 'Successfully Added!'

    def user_pass_check(self, app_user_pass):
        app_user_login = self
        if app_user_pass == '' or app_user_login == '':
            return 'input user password and login'
        else:
            app_user_pass_hash = app_user.user_pass_hash(app_user_login)
            app_user_pass_hash_check = check_password_hash(app_user_pass_hash, app_user_pass)
            if app_user_pass_hash_check is True:
                return True
            else:
                return False

    def user_pass_hash(self):
        app_user_login = self
        sql_formula = 'SELECT Pass FROM invent_system_users WHERE User_Name= %s;'
        my_db = myconnutils.my_db_connection()
        my_cursor = my_db.cursor()
        my_cursor.execute(sql_formula, [app_user_login])
        app_user_pass_hash = my_cursor.fetchone()[0]
        my_cursor.close()
        my_db.close()
        return app_user_pass_hash

    def user_delete(self):
        del_user_login = self
        sql_formula = "DELETE FROM invent_system_users WHERE User_Name = %s;"
        if del_user_login == '':
            return 'input user login to delete'
        else:
            my_db = myconnutils.my_db_connection()
            my_cursor = my_db.cursor()
            my_cursor.execute("SELECT COUNT(1) FROM invent_system_users WHERE User_Name = %s;", [del_user_login])
            if my_cursor.fetchone()[0]:
                my_cursor.close()
                my_db.close()
                app_user.query_execute(sql_formula, del_user_login)
                return 'Successfully Deleted!'
            else:
                return 'User ' + del_user_login + ' is not on the List'

    def user_change_password(self, user_credentials):
        pass

    def query_execute(self, user_credentials):
        if self != '' and user_credentials != '':
            my_db = myconnutils.my_db_connection()
            my_cursor = my_db.cursor()
            my_cursor.execute(self, user_credentials)
            my_db.commit()
            my_cursor.close()
            my_db.close()


class books:

    def books_insert(self):
        pass


# my_cursor.close()
# my_db.close()

# app_user.user_delete('JakubK')
# app_user.user_add('admin', 'admin')

# app_user.user_pass_hash('qbek')
