import sqlite3


class DataConn:

  def __init__(self, db_name):
    """Constructor"""
    print('__init__')
    self.db_name = db_name

  def __enter__(self):
    """
    Open the database connection.
    """
    print('__enter__')
    self.conn = sqlite3.connect(self.db_name)
    return self.conn

  def __exit__(self, exc_type, exc_val, exc_tb):
    """
    Close the connection.
    """
    print('__exit__:', exc_type, exc_val)
    self.conn.close()
    if exc_val:
      raise

  def __del__(self):
    print('__del__', self)


if __name__ == '__main__':
  db = 'test_1.db'

  with DataConn(db) as conn:
    cursor = conn.cursor()
    print('fetchall: ', cursor.fetchall())

  print('завершаем действия')

print('Выполнено')