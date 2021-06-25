import mysql.connector
from datetime import datetime



connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Sema_tolga85",
    database = "scholldb"
)