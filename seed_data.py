import random
from datetime import datetime, timedelta
from faker import Faker
import psycopg2

fake = Faker()

conn = psycopg2.connect(
    host="localhost",
    database="taskflow_analytics",
    user="sthitapragyan"
)

cursor = conn.cursor()

start_date = datetime(2023, 1, 1)

num_users = 450

plans = {
    "Free": 0,
    "Starter": 29,
    "Pro": 99,
    "Enterprise": 499
}

channels = ["organic", "paid_ads", "referral"]

for _ in range(num_users):
    signup = start_date + timedelta(days=random.randint(0, 540))
    plan = random.choices(
        list(plans.keys()),
        weights=[50, 30, 15, 5]
    )[0]

    status = random.choices(
        ["active", "churned"],
        weights=[85, 15]
    )[0]

    cursor.execute("""
        INSERT INTO users (email, company_name, industry, signup_date, plan_type, status)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING user_id;
    """, (
        fake.email(),
        fake.company(),
        random.choice(["Tech", "Finance", "Healthcare", "Education"]),
        signup,
        plan,
        status
    ))

    user_id = cursor.fetchone()[0]

    # Acquisition
    cursor.execute("""
        INSERT INTO customer_acquisition (user_id, channel, campaign, acquisition_cost)
        VALUES (%s, %s, %s, %s);
    """, (
        user_id,
        random.choice(channels),
        fake.word(),
        random.randint(0, 200)
    ))

    # Subscription
    if plan != "Free":
        end = None
        if status == "churned":
            end = signup + timedelta(days=random.randint(30, 300))

        cursor.execute("""
            INSERT INTO subscriptions (user_id, plan_type, billing_cycle, mrr, start_date, end_date)
            VALUES (%s, %s, %s, %s, %s, %s);
        """, (
            user_id,
            plan,
            random.choice(["monthly", "annual"]),
            plans[plan],
            signup,
            end
        ))

    # Events
    for _ in range(random.randint(5, 40)):
        event_date = signup + timedelta(days=random.randint(0, 500))
        cursor.execute("""
            INSERT INTO events (user_id, event_type, event_date)
            VALUES (%s, %s, %s);
        """, (
            user_id,
            random.choice(["login", "create_project", "export_report"]),
            event_date
        ))

conn.commit()
cursor.close()
conn.close()

print("Data inserted successfully!")
