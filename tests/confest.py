import os

# фейковые переменные для CI
os.environ["POSTGRES_USER"] = "test_user"
os.environ["POSTGRES_PASSWORD"] = "test_password"
os.environ["POSTGRES_DB"] = "test_db"
os.environ["GREETING"] = "ci"