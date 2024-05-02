from models.__init__ import CURSOR, CONN

class Task:
  
  all = {}

  def __init__(self, task_name, priority, id=None):
    self.id = id
    self.task_name = task_name
    self.priority = priority

  def __repr__(self):
    return f'<Task {self.id} {self.task_name}>'
  
  @property
  def task_name(self):
    return self._task_name
  
  @task_name.setter
  def task_name(self, task_name):
    if task_name.isspace() or len(task_name) < 0:
      raise ValueError('Task name must not be empty')
    else:
      self._task_name = task_name

  @classmethod
  def create_table(cls):
    sql = """
        CREATE TABLE IF NOT EXISTS tasks (
          id INTEGER PRIMARY KEY,
          task_name TEXT,
          priority TEXT
        );
      """
    
    CURSOR.execute(sql)
    CONN.commit()
  
  @classmethod
  def instance_from_db(cls, row):
    tasks = cls.all.get(row[0])
    if tasks:
        tasks.task_name = row[1]
        tasks.priority = row[2]
    else:
        tasks = cls(row[1], row[2])
        tasks.id = row[0]
        cls.all[tasks.id] = tasks
    return tasks

  
  def save(self):
    sql = """
      INSERT INTO tasks (task_name, priority)
      VALUES (?, ?)
    """

    CURSOR.execute(sql, (self.task_name, self.priority))
    CONN.commit()

  @classmethod
  def view_all(cls):
    sql = """
      SELECT *
      FROM tasks
    """

    rows = CURSOR.execute(sql).fetchall()
    return [cls.instance_from_db(row) for row in rows]

  @classmethod
  def create(cls, task_name, priority):
    task = cls(task_name, priority)

    task.save()
    return task

    
    
    
  

  
