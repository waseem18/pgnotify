# -*- coding: utf-8 -*-

"""
pgnotify.api
~~~~~~~~
Class definitions to be able to create an initial pgnotify object.

Example :

pg = PgNotify(dsn, tables)
pg.listen(callback_method)

"""

import psycopg2
import select
import logging
import time
import json
from pgnotify import utils

log = logging.getLogger(__name__)


class PgNotify(object):
    """Class to create a pgnotify object"""

    def __init__(self, database_url, tables_list):
        """

        :param database_url: Postgres db url
        :param tables_list: List of JSON's defining triggers on tables
        """
        self.database_url = database_url
        self.conn = psycopg2.connect(self.database_url)
        self.conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        self.curs = self.conn.cursor()
        self.tables_list = tables_list
        self._create_triggers()

    def _create_triggers(self):
        for table in self.tables_list:
            for sql in utils.convert_json_to_sql(table):
                self.curs.execute(sql)

    def listen(self, callback):
        self.curs.execute("LISTEN pgnotify;")
        while True:
            if select.select([self.conn], [], [], 60) == ([], [], []):
                log.info("Connection timeout")
            else:
                self.conn.poll()
                while self.conn.notifies:
                    notify = self.conn.notifies.pop(0)
                    payload = json.loads(notify.payload)
                    payload['timestamp'] = time.time()
                    callback(payload)
