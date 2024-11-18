from flask import Flask ,render_template
from views.auth_view import auth_blueprint
from views.images_view import images_blueprint
from views.vacations_view import vacations_blueprint
from logging import getLogger, ERROR

app = Flask(__name__,static_url_path='/static')


app.secret_key = "The amazing python first app"
app.register_blueprint(vacations_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(images_blueprint)




if __name__ == '__main__':
    app.run(debug=True)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")

@app.errorhandler(Exception)
def catch_all(error):
    print(error)
    return render_template('500.html', error=error)