from sqlalchemy import URL, create_engine, text
from sqlalchemy.orm import sessionmaker

url = URL.create(
    drivername="postgresql+psycopg2",
    username="testuser",
    password="testpassword",
    host="localhost",
    port=5432,
    database="testuser"
)

engine = create_engine(url, echo=True)

session_pool = sessionmaker(engine)

# with session_pool() as session:
    # query = text("""
    # CREATE TABLE users
    # (
    # telegram_id BIGINT PRIMARY KEY,
    # full_name VARCHAR(255) NOT NULL,
    # username VARCHAR(255),
    # language_code VARCHAR(255),
    # created_at TIMESTAMP DEFAULT NOW(),
    # referrer_id BIGINT,
    # FOREIGN KEY (referrer_id)
    #     REFERENCES users (telegram_id)
    #     ON DELETE SET NULL
    # );
    # """)
    # session.execute(query)
    # session.commit()

# with session_pool() as session:
#     insert_query = text("""
#         INSERT INTO users (telegram_id, full_name, username, language_code, referrer_id)
#         VALUES (1, 'John Doe', 'johndoe', 'en', NULL),
#                   (2, 'Jane Doe', 'janedoe', 'en', 1);
#         """)
#     session.execute(insert_query)
#     session.commit()
#
#     select_query = text("""
#         SELECT * FROM users;
#         """)
#     result = session.execute(select_query)
#     for row in result:
#         print(row)

# with session_pool() as session:
#     result = session.execute(text("SELECT * FROM users;"))
#     print(f"execute result: {result}")
#
#     result = session.execute(text("SELECT * FROM users;")).fetchall()
#     print(f"execute fetch all : {result}")
#
#     result = session.execute(text("SELECT * FROM users;")).fetchone()
#     print(f"execute fetch one : {result}")






