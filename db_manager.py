import asyncpg
from asyncpg.pool import Pool
import os


class DBManager:
    def __init__(self, config):
        self.config = config
        self.pool: Pool = None

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect()

    async def connect(self):
        try:
            self.pool = await asyncpg.create_pool(
                user=self.config['user'],
                password=self.config['password'],
                database=self.config['database'],
                host=self.config['host'],
                port=self.config['port']

            )
        except asyncpg.PostgresError as e:
            raise e

    async def disconnect(self):
        if self.pool:
            try:
                await self.pool.close()
            except asyncpg.PostgresError as e:
                raise e

    async def execute(self, query, *args):
        async with self.pool.acquire() as connection:
            try:
                return await connection.execute(query, *args)
            except asyncpg.PostgresError as e:
                raise e

    async def fetch(self, query, *args):
        async with self.pool.acquire() as connection:
            try:
                return await connection.fetch(query, *args)
            except asyncpg.PostgresError as e:
                raise e

    async def fetchrow(self, query, *args):
        async with self.pool.acquire() as connection:
            try:
                return await connection.fetchrow(query, *args)
            except asyncpg.PostgresError as e:
                raise e

    async def fetchval(self, query, *args):
        async with self.pool.acquire() as connection:
            try:
                return await connection.fetchval(query, *args)
            except asyncpg.PostgresError as e:
                raise e
