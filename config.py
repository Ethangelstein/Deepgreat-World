from settings import x


# SQLAlchemy configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://your_username:your_password@localhost/your_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
