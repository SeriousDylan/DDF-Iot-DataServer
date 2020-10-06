import sqlite3




class DataBase:
    def __init__(self):
        print("test")

    def __retrieve(self, query):
        connection = sqlite3.connect(self.__db_CPU_Load.db)
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        count = 0
        results = {}
        for row in rows:
            results[count] = dict(zip([c[0] for c in cursor.description], row))
            count += 1
        connection.close()
        return  results

    def get_last(self, value="10"):
        if not value.isnumeric():
           value = 10
        else:
            value = abs(int(value))
        query = f"SELECT * FROM {self.CPULoad}"\
                f"  ORDER BY created_at DESC"\
            f"  LIMIT {value}"
        return self.__retrieve(query)

    def get_in_last(self, value="1", period="MINUTES"):
        period = period.upper()
        if period not in (
            'SECONDS', 'MINUTES', 'HOURS', 'DAYS'
            'WEEKS', 'MONTHS', 'YEARS'):
            period = 'MINUTES'

        if not value.isnumeric():
           value = -1
        else:
           value = -abs(int(value))
        query = f"SELECT * FROM {self.CPULoad}"\
                f"  WHERE created_at > datetime('now', '{value} {period}')"\
                f"  ORDER BY created_at DESC"
        return self.__retrieve(query)