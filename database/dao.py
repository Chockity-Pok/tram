from .tram_relation import Attack
import logging


class Dao:

    def __init__(self, database):
        self.logger = logging.getLogger('DataService')
        self.db = Attack(database)

    async def build(self, schema):
        await self.db.build(schema)

    async def get(self, table, equal=None, not_equal=None):
        return await self.db.get(table, equal=equal, not_equal=not_equal)

    async def update(self, table, where={}, data={}, return_sql=False):
        return await self.db.update(table, where=where, data=data, return_sql=return_sql)

    async def insert(self, table, data, return_sql=False):
        return await self.db.insert(table, data, return_sql=return_sql)

    async def insert_generate_uid(self, table, data, id_field='uid', return_sql=False):
        return await self.db.insert_generate_uid(table, data, id_field, return_sql=return_sql)

    async def delete(self, table, data, return_sql=False):
        return await self.db.delete(table, data, return_sql=return_sql)

    async def raw_query(self, query, one=False):
        return await self.db.raw_query(query, one)
        
    async def raw_select(self, query, parameters=None):
        return await self.db.raw_select(query, parameters=parameters)

    async def run_sql_list(self, sql_list=None):
        return await self.db.run_sql_list(sql_list=sql_list)
