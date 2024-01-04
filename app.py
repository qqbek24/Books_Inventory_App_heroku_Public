from flask import Flask, render_template, request, redirect, url_for, flash, session, escape

import constants
import myconnutils
import models
import json
from urllib.request import urlopen
import string

# TODO: HTML Error handling (espacially in gglbooks api)
#       unit tests with pytest

app = Flask(__name__)
app.secret_key = constants.SECRET_KEY
# app.permanent_session_lifetime = True


@app.route('/')
def login():
    if 'username' in session:
        username_session = escape(session['username']).capitalize()
        return render_template('index.html', session_user_name=username_session)
    return render_template('login.html')


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    try:
        username_form = request.form['username']
        password_form1 = request.form['password']
        password_form2 = request.form['rep_password']
        if password_form1 != password_form2:
            flash('Incorrect passwords. Password 1 must be equal to Password 2')
        else:
            if username_form == "" and password_form1 == "" or password_form2 == "":
                flash('Please fill out the fields')
            else:
                if request.method == 'POST':
                    db_res_information = models.app_user.user_add(username_form, password_form1)
                    if db_res_information != 'Successfully Added!':
                        flash(db_res_information)
                        return redirect(url_for('registered'))
                    else:
                        flash(db_res_information)
                        return redirect(url_for('logout'))

    except Exception as exc:
        flash('Unexpected error: {}'.format(exc))
        return render_template('register.html')


@app.route('/registered', methods=['GET'])
def registered():
    if request.method == 'GET':
        session.clear()
        return render_template('register.html')


@app.route('/log', methods=['POST'])
def log():
    try:
        username_form = request.form['username']
        password_form = request.form['password']
        if username_form == "" and password_form == "":
            flash('Please fill out the fields')
        else:
            if request.method == 'POST':
                my_db = myconnutils.my_db_connection()
                my_cursor = my_db.cursor()
                if 'username' in session:
                    my_cursor.close()
                    my_db.close()
                    return redirect(url_for('index'))
                if request.method == 'POST':
                    my_cursor.execute("SELECT COUNT(1) FROM invent_system_users WHERE User_Name = %s;", [username_form])
                    if my_cursor.fetchone()[0]:
                        password_form_hash_checked = models.app_user.user_pass_check(username_form, password_form)
                        if password_form_hash_checked is True:
                            session['username'] = request.form['username']
                            my_db.commit()
                            my_cursor.close()
                            my_db.close()
                            flash('Login Successfully')
                            return render_template('index.html')
                        else:
                            my_cursor.close()
                            my_db.close()
                            flash('Either Username or Password is Incorrect')
                            return redirect(url_for('login'))
                    else:
                        my_cursor.close()
                        my_db.close()
                        flash('Either Username or Password is Incorrect')
                        return redirect(url_for('login'))
                else:
                    my_cursor.close()
                    my_db.close()
                    flash('None POST method')
                    return redirect(url_for('login'))

    except Exception as exc:
        flash('Unexpected error: {}'.format(exc))
        return render_template('login.html')


@app.route('/logout', methods=['GET'])
def logout():
    if request.method == 'GET':
        session.clear()
        return render_template('login.html')


@app.route('/insert', methods=['POST'])
def insert():
    try:
        p_title = request.form['addtitle']
        p_author = request.form['addauthor']
        p_date_pub = request.form['adddatepub']
        p_isbn = request.form['addisbn']
        p_pages = request.form['addpages']
        p_cover = request.form['addcover']
        p_lang = request.form['addlang']

        if p_title == "":
            return render_template('index.html')
        elif p_author == "":
            return render_template('index.html')
        elif p_date_pub == "":
            return render_template('index.html')
        elif p_isbn == "":
            return render_template('index.html')
        elif p_pages == "":
            return render_template('index.html')
        elif p_cover == "":
            return render_template('index.html')
        elif p_lang == "":
            return render_template('index.html')
        else:
            if request.method == 'POST':
                my_db = myconnutils.my_db_connection()
                my_cursor = my_db.cursor()
                if request.method == 'POST':
                    my_cursor.execute("SELECT COUNT(1) FROM invent_table_view WHERE title = %s;", [p_title])
                    if my_cursor.fetchone()[0]:
                        flash(p_title + ' is already on the list')
                        return render_template('index.html')
                    else:
                        my_cursor.execute("INSERT INTO invent_table_view(title, author , date_of_publication , isbn" 
                                          ", pages , cover , language) Values(%s,%s,%s,%s,%s,%s,%s)",
                                          (p_title, p_author, p_date_pub, p_isbn, p_pages, p_cover, p_lang))
                        my_db.commit()
                        my_cursor.close()
                        my_db.close()
                        flash(p_title + ', ' + p_author + ', ' + p_date_pub + ', Successfully saved!')
                        return render_template('index.html')
                else:
                    my_cursor.close()
                    my_db.close()
                    return render_template('index.html')

    except Exception as exc:
        flash('Unexpected error: {}'.format(exc))
        return render_template('index.html')


@app.route('/searchall', methods=['POST'])
def searchall():
    try:
        if request.method == 'POST':
            my_db = myconnutils.my_db_connection()
            my_cursor = my_db.cursor()
            my_cursor.execute("SELECT * FROM invent_table_view")
            data = my_cursor.fetchall()
            my_db.commit()
            my_cursor.close()
            my_db.close()
            return render_template('index.html', products=data)

    except Exception as exc:
        flash('Unexpected error: {}'.format(exc))
        return render_template('index.html')


@app.route('/search_title', methods=['POST'])
def search_title():
    try:
        prod_search = request.form['searchprod']
        sql_stm_cnt = "SELECT COUNT(1) FROM invent_table_view WHERE title LIKE %s;"
        sql_stm = "SELECT * FROM invent_table_view WHERE title LIKE %s;"
        if prod_search == "":
            flash('Please fill out the search field ')
            return render_template('index.html')
        else:
            db_res = search_col(prod_search, sql_stm_cnt, sql_stm)
            if db_res != 'There no such product as ':
                flash(prod_search + ' Found!')
                return render_template('index.html', prodnames=db_res)
            elif db_res == "index.html":
                return render_template('index.html')
            else:
                flash('There no such product as ' + prod_search)
                return render_template('index.html')

    except Exception as exc:
        flash('Unexpected error: {}'.format(exc))
        return render_template('index.html')


@app.route('/search_author', methods=['POST'])
def search_author():
    try:
        prod_search = request.form['searchprod']
        sql_stm_cnt = "SELECT COUNT(1) FROM invent_table_view WHERE author LIKE %s;"
        sql_stm = "SELECT * FROM invent_table_view WHERE author LIKE %s;"
        if prod_search == "":
            flash('Please fill out the search field ')
            return render_template('index.html')
        else:
            db_res = search_col(prod_search, sql_stm_cnt, sql_stm)
            if db_res != 'There no such product as ':
                flash(prod_search + ' Found!')
                return render_template('index.html', prodnames=db_res)
            elif db_res == "index.html":
                return render_template('index.html')
            else:
                flash('There no such product as ' + prod_search)
                return render_template('index.html')

    except Exception as exc:
        flash('Unexpected error: {}'.format(exc))
        return render_template('index.html')


@app.route('/search_language', methods=['POST'])
def search_language():
    try:
        prod_search = request.form['searchprod']
        sql_stm_cnt = "SELECT COUNT(1) FROM invent_table_view WHERE language LIKE %s;"
        sql_stm = "SELECT * FROM invent_table_view WHERE language LIKE %s;"
        if prod_search == "":
            flash('Please fill out the search field ')
            return render_template('index.html')
        else:
            db_res = search_col(prod_search, sql_stm_cnt, sql_stm)
            if db_res != 'There no such product as ':
                flash(prod_search + ' Found!')
                return render_template('index.html', prodnames=db_res)
            elif db_res == "index.html":
                return render_template('index.html')
            else:
                flash('There no such product as ' + prod_search)
                return render_template('index.html')

    except Exception as exc:
        flash('Unexpected error: {}'.format(exc))
        return render_template('index.html')


def search_col(prod_search, sql_stm_cnt_ex, sql_stm_ex):
    prod_search_str = prod_search
    if request.method == 'POST':
        my_db = myconnutils.my_db_connection()
        my_cursor = my_db.cursor()
        if request.method == 'POST':
            my_cursor.execute(sql_stm_cnt_ex, ["%" + prod_search_str + "%"])
            if my_cursor.fetchone()[0]:
                my_cursor.execute(sql_stm_ex, ["%" + prod_search_str + "%"])
                prod = my_cursor.fetchall()
                my_cursor.close()
                my_db.close()
                return prod
            else:
                my_cursor.close()
                my_db.close()
                return 'There no such product as '
        else:
            my_cursor.close()
            my_db.close()
            return 'There no such product as '
    else:
        return 'index.html'


@app.route('/delete', methods=['POST'])
def delete():
    try:
        del_title = request.form['titlename']
        if del_title == "":
            return render_template('index.html')
        else:
            # if request.method == 'POST':
            #     my_db = myconnutils.my_db_connection()
            #     my_cursor = my_db.cursor()
            if request.method == 'POST':
                my_db = myconnutils.my_db_connection()
                my_cursor = my_db.cursor()
                my_cursor.execute("SELECT COUNT(1) FROM invent_table_view WHERE title = %s;", [del_title])
                if my_cursor.fetchone()[0]:
                    my_cursor.execute("DELETE FROM invent_table_view WHERE title = %s;", [del_title])
                    my_db.commit()
                    my_cursor.close()
                    my_db.close()
                    flash('Successfully Deleted!')
                    return render_template('index.html')
                else:
                    my_cursor.close()
                    my_db.close()
                    flash('Record ' + request.form['titlename'] + ' is not on the List')
        return render_template('index.html')

    except Exception as exc:
        flash('Unexpected error: {}'.format(exc))
        return render_template('index.html')


@app.route('/update', methods=['POST'])
def update():
    try:
        title_p = request.form['updtitle']
        author_p = request.form['updauthor']
        date_pub_p = request.form['upddatepub']
        isbn_p = request.form['updisbn']
        pages_p = request.form['updpages']
        cover_p = request.form['updcover']
        lang_p = request.form['updlang']
        if title_p == "":
            return render_template('index.html')
        elif author_p == "":
            return render_template('index.html')
        elif date_pub_p == "":
            return render_template('index.html')
        elif isbn_p == "":
            return render_template('index.html')
        elif pages_p == "":
            return render_template('index.html')
        elif cover_p == "":
            return render_template('index.html')
        elif lang_p == "":
            return render_template('index.html')
        else:
            # if request.method == 'POST':
                # my_db = myconnutils.my_db_connection()
                # my_cursor = my_db.cursor()
            if request.method == 'POST':
                my_db = myconnutils.my_db_connection()
                my_cursor = my_db.cursor()
                my_cursor.execute("SELECT COUNT(1) FROM invent_table_view WHERE title = %s;", [title_p])
                if my_cursor.fetchone()[0]:
                    my_cursor.execute("SELECT * FROM invent_table_view WHERE title = %s;", [title_p])
                    flash(title_p + ' Found!')
                    my_cursor.execute("UPDATE invent_table_view SET author='" + author_p +
                                      "' , date_of_publication='" + date_pub_p +
                                      "' , isbn='" + isbn_p +
                                      "' , pages='" + pages_p +
                                      "' , cover='" + cover_p +
                                      "' , language='" + lang_p +
                                      "' WHERE title='" + title_p + "'")
                    my_db.commit()
                    my_cursor.close()
                    my_db.close()
                    flash('Successfully Updated')
                    return render_template('index.html')
                else:
                    my_cursor.close()
                    my_db.close()
                    flash('There no such product as ' + title_p)
                return render_template('index.html')

    except Exception as exc:
        flash('Unexpected error: {}'.format(exc))
        return render_template('index.html')


@app.route('/searchapi', methods=['POST'])
def searchapi():
    try:
        q_value = request.form['value_str']
        req_api = request_ggl_bks_api(q_value)
        req_jsn = json.load(req_api)
        data = ret_from_ggl_bks_jsn(req_jsn)

        return render_template('index.html', apiproducts=data)

    except Exception as exc:
        flash('Unexpected error: {}'.format(exc))
        return render_template('index.html')


def request_ggl_bks_api(form_value):
    s = form_value
    q_value = s.translate({ord(c): None for c in string.whitespace})
    google_api_key = constants.GOOGLE_BOOKS_API_KEY
    req_params = ('?q=' + q_value + '&maxResults=40' + '&key=' + google_api_key)
    req_api = urlopen("https://www.googleapis.com/books/v1/volumes" + req_params)
    return req_api


def ret_from_ggl_bks_jsn(req_jsn):
    items_req_jsn = req_jsn["items"]
    x = len(items_req_jsn)
    for i in range(0, x):
        volume_info = items_req_jsn[i]["volumeInfo"]
        volume_info_cover = "" if "imageLinks" not in volume_info else volume_info["imageLinks"]

        p_title = "" if "title" not in volume_info else volume_info["title"]
        p_subtitle = "" if "subtitle" not in volume_info else " - " + volume_info["subtitle"]
        title_subtitle = p_title + p_subtitle
        p_pub_date = "none date" if "publishedDate" not in volume_info else volume_info["publishedDate"]
        p_page_count = 0 if "pageCount" not in volume_info else volume_info["pageCount"]
        p_thumbnail = "none link" if "thumbnail" not in volume_info_cover else volume_info_cover["thumbnail"]
        p_language = "none lang" if "language" not in volume_info else volume_info["language"]

        if "authors" not in volume_info:
            prettify_author = ""
        else:
            p_author = volume_info["authors"]
            prettify_author = p_author if len(p_author) > 1 else p_author[0]

        if "industryIdentifiers" not in volume_info:
            volume_info_id = "0"
        else:
            volume_info_id = volume_info["industryIdentifiers"]

        if len(volume_info_id) > 1:
            for x_id in range(0, len(volume_info_id)):
                id_cds = volume_info_id[x_id]
                id_cdt = 0 if "identifier" not in id_cds else id_cds["identifier"]
                if len(id_cdt) == 13:
                    p_identifier = id_cdt
        else:
            volume_info_isbn = volume_info_id[0]
            req_identifier = "none isbn" if "identifier" not in volume_info_isbn else volume_info_isbn["identifier"]
            p_identifier = req_identifier if len(req_identifier) > 1 else req_identifier[1]

        title_str = title_subtitle
        author_str = prettify_author
        pubdate_str = p_pub_date
        id_str = p_identifier
        page_str = p_page_count
        thumb_str = p_thumbnail
        lang_str = p_language

        t1 = title_str, author_str, pubdate_str, id_str, page_str, thumb_str, lang_str
        if i == 0:
            data = [t1]
        else:
            data += [t1]
    data_bks = data
    return data_bks


# for localhost use, uncomment below lines
# if __name__ == "__main__":
#     app.run(debug=constants.DEBUG_MODE)
