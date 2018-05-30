from pgnotify import sql_templates


def parse_table_object(table_object):
    table = table_object["table"]
    schema = table_object.get("schema", "public")
    columns = table_object.get("columns", "*")
    table_events = {}
    if isinstance(columns, dict):
        table_events = columns
    else:
        table_events['insert'] = columns
        table_events['update'] = columns
        table_events['delete'] = columns
    return table_events, table, schema


def convert_json_to_sql(table_object):
    table_events, table, schema = parse_table_object(table_object)
    for event, columns in table_events.items():
        event = event.lower()
        if event == 'delete':
            status = 'OLD'
        else:
            status = 'NEW'
        if columns == "*":
            expression = "row_to_json({})".format(status)
        else:
            expression = "row_to_json((select r from (SELECT {}) as r))".format(
                ",".join(["{}.{}".format(status, col) for col in columns])
            )
        sql = sql_templates.create_trigger_template.format(
            schema=schema,
            table=table,
            event=event,
            data_expression=expression
        )
        yield sql
