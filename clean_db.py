#!/usr/local/bin/python

import subprocess

from app.config.settings import DATABASES

hostname = DATABASES['default']['HOST']
username = DATABASES['default']['USER']
password = DATABASES['default']['PASSWORD']
database = DATABASES['default']['NAME']

command = f"PGPASSWORD={password} psql --host={hostname} --username={username} --dbname={database} -exec 'delete from festalist_festalist where id in (select id from (select id, row_number() over (partition by title order by id desc) as row_num from festalist_festalist) a where a.row_num > 1);'"

subprocess.run(command, shell=True)
