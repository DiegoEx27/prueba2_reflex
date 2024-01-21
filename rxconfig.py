import reflex as rx

config = rx.Config(
    app_name="Reflex",
    db_url="mysql+mysqldb://root:@localhost/pruebas",
    api_url="http://app.example.com:8000"
)
#mysql://scott:tiger@localhost/foo