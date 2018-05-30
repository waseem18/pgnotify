import pgnotify

dsn = 'dbname=%s host=%s user=%s password=%s' % ("database_name",
                                                 "localhost",
                                                 "postgres",
                                                 "postgres"
                                                 )
tables = [
    {
        "table": "users",
        "columns": {
            "insert": "column_name",
            "update": "column_name",
            "delete": "column_name"
        }
    },
    {
        "table": "table_name"
    },
    {
        "table": "table_name",
        "columns": {
            "insert": "column_name"
        }
    }
]


def callback_method(payload):
    """
    payload is a JSON object defining the postgres event
    """
    pass


p = pgnotify.PgNotify(dsn, tables)
p.listen(callback_method)
