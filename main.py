# TO CONFIGURE:
# UPLOAD A IMAGE TO USE AS A FAVICON INTO THE 'TEMPLATES' FOLDER
# THEN RENAME IT TO 'favicon.png'
# IT WILL AUTOMATICALLY BE SET AS THE FAVICON
# GOTO ALL OF THE HTML DOCUMENTS IN THE 'TEMPLATES' FOLDER AND EDIT THE TEXT.
# TELL PEOPLE ABOUT YOUR SITE!
# !!! UNTIL YOU UPLOAD A FAVICON YOU WILL GET AN ERROR IN THE CONSOLE !!!
from flask import Flask, render_template, send_file
app = Flask('app')



@app.route('/')
def index():
  return render_template("index.html")


@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/style.css')
def style():
  return send_file('templates/style.css')


@app.route('/script.js')
def script():
  return send_file('templates/script.js')

@app.route('/imgs/Dark_Mode.svg')
def dark_mode_svg():
  return send_file('templates/imgs/Dark_Mode.svg')

@app.route('/favicon.png')
def favicon():
  return send_file('templates/favicon.png')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
    
@app.errorhandler(500)
def server_overloaded(e):
    # note that we set the 404 status explicitly
    return render_template('500.html'), 500

app.run(host='0.0.0.0', port=8080)