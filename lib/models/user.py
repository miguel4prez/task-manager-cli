from models.__init__ import CURSOR, CONN
import hashlib

class User:

  all = {}

  def __init__(self, username, password, id=None):
    self.id = id
    self.username = username
    self.password = password

  
  def __repr__(self):
    return f'<User {self.id} {self.username}>'
  
  @property
  def username(self):
    return self._username
  
  @username.setter
  def username(self, username):
    if username.isspace() or len(username) < 0:
      raise ValueError('Name must not be empty')
    else:
      self._username = username

  @property
  def password(self):
    return self._password
  
  @password.setter
  def password(self, password):
    if password.isspace() or len(password) < 5:
      raise ValueError('Password must not be empty and not less than five chars')
    else:
      self._password = password

  
  @classmethod
  def create_table(cls):
    """ Create a new table to persist the attributes of User instances """
    sql = """
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT)
    """
    CURSOR.execute(sql)
    CONN.commit()

  @classmethod
  def drop_table(cls):
    sql = """
      DROP TABLE IF EXISTS users
    """
    CURSOR.execute(sql)
    CONN.commit()

  def save(self):
    hashed_password = self._hash_password(self.password)

    sql = """
      INSERT INTO users (username, password)
      VALUES (?, ?)
    """

    CURSOR.execute(sql, (self.username, hashed_password))
    CONN.commit()

    self.id = CURSOR.lastrowid
    type(self).all[self.id] = self

  @staticmethod
  def _hash_password(password):
      """ Hash the password using SHA-256 """
      hashed_bytes = hashlib.sha256(password.encode('utf-8'))
      return hashed_bytes.hexdigest()


  @classmethod
  def create(cls, username, password):
    user = cls(username, password)

    user.save()
    return user
  
  def update(self):
    sql ="""
      UPDATE users
      SET username = ?, password = ?
      WHERE id = ?
    """

    CURSOR.execute(sql, (self.username, self.password, self.id))
    CONN.commit()

  def delete(self):
    sql ="""
      DELETE FROM users
      WHERE id = ?
    """

    CURSOR.execute(sql, (self.id,))
    CONN.commit()

    del type(self).all[self.id]

    self.id = None


  @classmethod
  def instance_from_db(cls, row):
    user = cls.all.get(row[0])
    if user:
      user.username = row[1]
      user.password = row[2]
    else:
      # not in dictionary, create new instance and add to dictionary
      user = cls(row[1], row[2])
      user.id = row[0]
      cls.all[user.id] = user
    return user

  @classmethod
  def find_by_username(cls, username):
    sql = """
      SELECT * 
      FROM users
      WHERE username is ?
    """

    row = CURSOR.execute(sql, (username,)).fetchone()
    return cls.instance_from_db(row) if row else None
  
  @classmethod
  def find_by_id(cls, id):
    sql = """
      SELECT * 
      FROM users
      WHERE id = ?
    """
    row = CURSOR.execute(sql, (id,)).fetchone()
    return cls.instance_from_db(row) if row else None





    

    