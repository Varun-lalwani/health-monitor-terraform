import os 
import psycopg2
from psycopg2.extras import RealDictCursor
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

# Load credentials from environment
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", 5432)
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Connection helper
def get_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn



def get_apis_to_check():
    """Return all APIs from api_endpoints table"""
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM  api_endpoints;")
            return cur.fetchall()


def insert_health_result(api_id, status_code, response_time_ms, success):
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO health_results
            (api_id, status_code, response_time_ms, success)
            VALUES (%s, %s, %s, %s);
        """, (api_id, status_code, response_time_ms, success))
        conn.commit()
    conn.close()

def get_health_state(api_id):
    conn = get_connection()
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("""
            SELECT * FROM  health_state
                    WHERE api_id = %s;
        """, (api_id,))
        state = cur.fetchone()
    conn.close()
    return state

def update_health_state(api_id, new_state, consecutive_failures):
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("""
            UPDATE  health_state
            SET current_state = %s,
                consecutive_failures = %s,
                last_changed_at = CURRENT_TIMESTAMP
            WHERE api_id = %s;
                     """, (new_state, consecutive_failures, api_id))
        conn.commit()
    conn.close()

if __name__=="__main__":
    apis = get_apis_to_check()
    print("APIs in DB:", apis) 
