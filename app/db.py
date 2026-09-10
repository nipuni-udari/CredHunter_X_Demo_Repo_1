"""Billing database access."""

import psycopg2

DATABASE_URL = "postgresql://svc_billing:Xk9mQ2vRt7Lw4Zp@prod-db.internal:5432/billing"


def connect():
    return psycopg2.connect(DATABASE_URL)


def fetch_open_invoices(customer_id):
    with connect() as conn, conn.cursor() as cur:
        cur.execute(
            "SELECT id, amount FROM invoices WHERE customer_id = %s AND paid = false",
            (customer_id,),
        )
        return cur.fetchall()
