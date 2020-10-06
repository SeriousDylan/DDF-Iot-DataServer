import psutil
import sqlite3

import time
connection = sqlite3.connect("db_CPU_Load.db")
csr = connection.cursor()


csr.execute("CREATE TABLE IF NOT EXISTS CPULoad("
            "[id] INTEGER PRIMARY KEY,"
            "[temperature] DECIMAL,"
            "[created_at] DATETIME)")
connection.commit()
connection.close()



def MaxCpuLoad():
    return max(psutil.cpu_percent(percpu=True))


while True:
    load = MaxCpuLoad()
    print(load)
    connection = sqlite3.connect("db_CPU_Load.db")
    csr = connection.cursor()
    csr.execute(
        "INSERT INTO "
        "CPULoad(id, temperature, created_at)"
        f"VALUES (null, {load}, datetime())")
    connection.commit()
    connection.close()
    time.sleep(30)
