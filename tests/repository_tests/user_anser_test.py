import pytest

from repository.database import create_tables, get_db_connection, drop_all_tables


@pytest.fixture(scope='module')
def setup_database():
    create_tables()
    yield

    conn = get_db_connection()
    cur = conn.cursor()
    drop_all_tables()
    conn.commit()
    cur.close()
    conn.close()