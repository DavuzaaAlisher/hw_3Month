CREATE_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS telegram_users
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
USERNAME CHAR(50),
FISRT_NAME CHAR(50),
LAST_NAME CHAR(50),
UNIQUE (TELEGRAM_ID)
)
"""
CREATE_BAN_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS ban_users
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
COUNT INTEGER,
UNIQUE (TELEGRAM_ID)
)
"""

CREATE_USER_FORM_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS user_form
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
NICKNAME CHAR(50),
BIO TEXT,
GEO TEXT,
GENDER CHAR(50),
AGE INTEGER,
PHOTO TEXT,
UNIQUE (TELEGRAM_ID)
)
"""

CREATE_LIKE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS like_forms
(
ID INTEGER PRIMARY KEY,
OWNER_TELEGRAM_ID INTEGER,
LIKER_TELEGRAM_ID INTEGER,
UNIQUE (OWNER_TELEGRAM_ID, LIKER_TELEGRAM_ID)
)
"""

INSERT_USER_QUERY = """
INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?)
"""

INSERT_BAN_USER_QUERY = """
INSERT INTO ban_users VALUES (?,?,?)
"""
INSERT_LIKE_QUERY = """
INSERT INTO like_forms VALUES (?,?,?)
"""
INSERT_USER_FORM_QUERY = """
INSERT INTO user_form VALUES (?,?,?,?,?,?,?,?)
"""
SELECT_BAN_USER_QUERY = """
SELECT * FROM ban_users WHERE TELEGRAM_ID = ?
"""

SELECT_USER_FORM_QUERY = """
SELECT * FROM user_form WHERE TELEGRAM_ID = ?
"""
SELECT_ALL_USER_FORM_QUERY = """
SELECT * FROM user_form
"""
UPDATE_BAN_USER_COUNT_QUERY = """
UPDATE ban_users SET COUNT = COUNT + 1 WHERE TELEGRAM_ID = ?
"""
FILTER_LEFT_JOIN_USER_FORM_LIKE_QUERY = """
SELECT * FROM user_form
LEFT JOIN like_forms ON user_form.TELEGRAM_ID = like_forms.OWNER_TELEGRAM_ID
AND like_forms.LIKER_TELEGRAM_ID = ?
WHERE like_forms.ID IS NULL
AND user_form.TELEGRAM_ID != ?
"""