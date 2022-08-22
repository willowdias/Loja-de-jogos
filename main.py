
from flask import Flask
from werkzeug.utils import redirect
from flask_mysqldb import MySQL
from classviews import*
from datetime import datetime
from datetime import timedelta
from config import*

app = Flask(__name__)
from classviews import*
from logui_logout import*

if __name__ == "__main__":
    
	app.run(debug=True)
