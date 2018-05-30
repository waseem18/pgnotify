drop_triggers = """
DO $$DECLARE r record;
BEGIN
    FOR r IN SELECT routine_schema, routine_name FROM information_schema.routines
             WHERE routine_name LIKE 'pgnotify_%'
    LOOP
        EXECUTE 'DROP FUNCTION ' || quote_ident(r.routine_schema) || '.' || quote_ident(r.routine_name) || ' CASCADE';
    END LOOP;
END$$;
"""

create_trigger_template = """
CREATE OR REPLACE FUNCTION {schema}.pgnotify_{table}_{event}() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
  DECLARE
    cur_rec record;
    BEGIN
      PERFORM pg_notify('pgnotify', json_build_object(
                    'table', TG_TABLE_NAME,
                    'schema', TG_TABLE_SCHEMA,
                    'op',    TG_OP,
                    'data',  {data_expression}
              )::text);
      RETURN cur_rec;
    END;
$$;
DROP TRIGGER IF EXISTS pgnotify_{table}_{event} ON {schema}.{table};
CREATE TRIGGER pgnotify_{table}_{event} AFTER {event} ON {schema}.{table} FOR EACH ROW EXECUTE PROCEDURE {schema}.pgnotify_{table}_{event}();
"""