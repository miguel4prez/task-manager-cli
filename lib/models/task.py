from models.__init__ import CURSOR, CONN

class Task:
  
  all = {}

  def __init__(self, task_name, priority, user_id, id=None):
    self.id = id
    self.task_name = task_name
    self.priority = priority
    self.user_id = user_id

  def __repr__(self):
    return f'<Task {self.id} {self.task_name}>'
  
  @property
  def task_name(self):
    return self._task_name
  
  @task_name.setter
  def task_name(self, task_name):
    if task_name.isspace() or len(task_name) < 1:
      raise ValueError('Task name must not be empty')
    else:
      self._task_name = task_name

  @classmethod
  def create_table(cls):
    sql = """
        CREATE TABLE IF NOT EXISTS tasks (
          id INTEGER PRIMARY KEY,
          task_name TEXT,
          priority TEXT,
          user_id INTEGER,
          FOREIGN KEY (user_id) REFERENCES users(id)
        );
      """
    CURSOR.execute(sql)
    CONN.commit()
  
  @classmethod
  def instance_from_db(cls, row):
    task = cls.all.get(row[0])
    if task:
      task.task_name = row[1]
      task.priority = row[2]
      task.user_id = row[3]
    else:
      task = cls(row[1], row[2], row[3])
      task.id = row[0]
      cls.all[task.id] = task
    return task

  def save(self):
    sql = """
      INSERT INTO tasks (task_name, priority, user_id)
      VALUES (?, ?, ?)
    """
    CURSOR.execute(sql, (self.task_name, self.priority, self.user_id))
    CONN.commit()

  def update(self):
    sql = """
        UPDATE tasks
        SET task_name = ?, priority = ?
        WHERE id = ?
    """
    CURSOR.execute(sql, (self.task_name, self.priority, self.id))
    CONN.commit()

  @classmethod
  def view_all(cls, user_id):
    sql = """
      SELECT *
      FROM tasks
      WHERE user_id = ?
    """
    rows = CURSOR.execute(sql, (user_id,)).fetchall()
    return [cls.instance_from_db(row) for row in rows]

  @classmethod
  def create(cls, task_name, priority, user_id):
    task = cls(task_name, priority, user_id)
    task.save()
    return task
  
  @classmethod
  def find_by_id(cls, task_id):
    sql = """
      SELECT *
      FROM tasks
      WHERE id = ?
    """
    row = CURSOR.execute(sql, (task_id,)).fetchone()
    if row:
        return cls.instance_from_db(row)
    else:
        return None


  def delete(self):
    sql = """
      DELETE FROM tasks
      WHERE id = ?
    """

    CURSOR.execute(sql, (self.id,))
    CONN.commit()

    del type(self).all[self.id]

    self.id = None