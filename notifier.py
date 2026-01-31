from db import update_health_state, insert_health_result  # optional, if needed

def send_notification(api_name, old_state, new_state):
    """
    Trigger notification when API state changes.
    For simplicity, we'll log to console and record in DB.
    """

    # 1. Print alert to console
    print(f"[ALERT] API '{api_name}' changed state: {old_state} → {new_state}")

    # 2. Optional: store in notifications table
    # If you created the table `api_monitor_schema.notifications`
    try:
        from db import get_connection
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO notifications
                (api_id, old_state, new_state)
                SELECT id, %s, %s FROM api_endpoints
                WHERE name = %s;
            """, (old_state, new_state, api_name))
            conn.commit()
       
    except Exception as e:
        print(f"[ERROR] Failed to insert notification for {api_name} - {e}")
    finally:
       # Always connection closed 
       if 'conn' in local():    
          conn.close()


# send_email(to="ops@example.com", subject=f"{api_name} state changed", body=...)
# or
# sns.publish(TopicArn=..., Message=f"{api_name} state changed: {old_state} → {new_state}")
