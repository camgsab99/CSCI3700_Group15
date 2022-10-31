from flask import Flask, render_template
import util

# create an application instance
# all requests it receives from clients to this object for handling
# we are instantiating a Flask object by passing __name__ argument to the Flask constructor. 
# The Flask constructor has one required argument which is the name of the application package. 
# Most of the time __name__ is the correct value. The name of the application package is used 
# by Flask to find static assets, templates and so on.
app = Flask(__name__)

# evil global variables
# can be placed in a config file
# here is a possible tutorial how you can do this
username='camgsab'
password='1234'
host='127.0.0.1'
port='5432'
database='dvdrental'

@app.route('/api/update_basket_a')
def update_basket_a():
    # connect to DB
    cursor, connection = util.connect_to_db(
        username, password, host, port, database)
    # insert a new row (5, 'Cherry') into basket_a
    record = cursor.execute("INSERT INTO basket_a VALUES (5, 'Cherry');")
    # print an error message if the SQL command is wrong
    if record == -1:
        print('Something is wrong with the SQL command')
    else:
        print('Successfully updated basket_a')
        connection.commit()
    # disconnect from database
    util.disconnect_from_db(connection, cursor)
    return 'Successfully updated basket_a'

@app.route('/api/unique')
def unique():
    # show unique fruits in basket_a and unique fruits in basket_b in an HTML table
    # connect to DB
    cursor, connection = util.connect_to_db(
        username, password, host, port, database)
    # execute SQL commands
    record = util.run_and_fetch_sql(cursor, "SELECT DISTINCT basket_a.fruit_a FROM basket_a UNION SELECT DISTINCT basket_b.fruit_b FROM basket_b;")
    if record == -1:
        # you can replace this part with a 404 page
        print('Something is wrong with the SQL command')
    else:
        print('Successfully fetched unique fruits')
        # this will return all column names of the select result table
        # ['fruit_a']
        col_names = [desc[0] for desc in cursor.description]
        # only use the first five rows
        log = record[:7]
        # log=[[1,2],[3,4]]
    # disconnect from database
    util.disconnect_from_db(connection, cursor)
    return render_template('index.html', sql_table = log, table_title=col_names)
    

if __name__ == '__main__':
    # set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
