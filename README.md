##  Books Inventory App (deployed on Heroku)
### Installation Instructions (localhost MySql):
1. Download the BooksInvSystem
2. Place the cloned folder under your Users directory “PycharmProjects”.
3. Install all the dependencies included in the requirements.txt file
4. Open the Books_Inventory_App Project in Pycharm then run pyhton file app.py 
5. Visit the website
6. (To log into inventory page, use the username ‘admin’ and password ‘admin’.)
7. Add ".env" file containing your GOOGLE BOOKS API KEY like
 
   ```
   GOOGLE_BOOKS_API_KEY = "put here your google api key string",
   ```

    and other DB credentials for example:
   
    ```
    APP_SECRET_KEY = "put here your secret key",
    DB_USER_LOGIN = "put here your DB login",
    DB_USER_PASS = "put here your DB password",
    S_HOST = "host"
    ```
 
 for how app looks and work, check address [Books inventory app](http://books-inv-app.herokuapp.com)
