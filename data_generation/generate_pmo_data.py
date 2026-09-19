import mysql.connector
from faker import Faker
from datetime import date, timedelta
import random

fake = Faker("en_GB")
random.seed(42)
Faker.seed(42)

# ---------------------------------------------------------
# MYSQL CONNECTION
# ---------------------------------------------------------

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0402",
    database="pmo_project_portfolio"
)

cursor = connection.cursor()

print("Connected to MySQL successfully.")

# ---------------------------------------------------------
# CLEAR EXISTING DATA
# ---------------------------------------------------------

cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

for table in ["resources", "issues", "risks", "projects", "project_managers"]:
    cursor.execute(f"TRUNCATE TABLE {table}")

cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

print("Existing data cleared.")

# ---------------------------------------------------------
# REFERENCE DATA
# ---------------------------------------------------------

departments = [
    "IT",
    "Finance",
    "Operations",
    "HR",
    "Marketing",
    "Procurement"
]

project_types = [
    "Technology",
    "Infrastructure",
    "Process Improvement",
    "Digital Transformation",
    "Compliance",
    "Business Change"
]

priorities = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

project_statuses = [
    "Completed",
    "In Progress",
    "Delayed",
    "At Risk",
    "On Hold"
]

risk_categories = [
    "Financial",
    "Resource",
    "Technical",
    "Operational",
    "Schedule",
    "Compliance",
    "Supplier"
]

risk_statuses = [
    "Open",
    "Monitoring",
    "Mitigated",
    "Closed"
]

issue_categories = [
    "Technical",
    "Resource",
    "Budget",
    "Schedule",
    "Supplier",
    "Quality",
    "Communication"
]

issue_severities = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

issue_statuses = [
    "Open",
    "In Progress",
    "Resolved",
    "Escalated"
]

roles = [
    "Business Analyst",
    "Developer",
    "Project Coordinator",
    "Data Analyst",
    "Engineer",
    "QA Analyst",
    "Product Owner",
    "Finance Analyst",
    "Change Manager",
    "Technical Lead"
]

# ---------------------------------------------------------
# 1. PROJECT MANAGERS
# ---------------------------------------------------------

managers = []

for i in range(1, 11):

    manager_id = f"PM{i:03d}"
    manager_name = fake.name()

    department = random.choice(departments)

    managers.append({
        "id": manager_id,
        "name": manager_name,
        "department": department
    })

    cursor.execute("""
        INSERT INTO project_managers
        (project_manager_id, manager_name, department)
        VALUES (%s, %s, %s)
    """, (
        manager_id,
        manager_name,
        department
    ))

print("Inserted 10 project managers.")

# ---------------------------------------------------------
# 2. PROJECTS
# ---------------------------------------------------------

projects = []

for i in range(1, 121):

    project_id = f"PRJ{i:03d}"

    department = random.choice(departments)

    manager = random.choice(managers)

    project_type = random.choice(project_types)

    priority = random.choices(
        priorities,
        weights=[15, 45, 30, 10]
    )[0]

    status = random.choices(
        project_statuses,
        weights=[30, 35, 15, 15, 5]
    )[0]

    start_date = date(
        2024,
        random.randint(1, 12),
        random.randint(1, 28)
    )

    duration_days = random.randint(90, 450)

    planned_end_date = start_date + timedelta(
        days=duration_days
    )

    # Actual completion behaviour depends on status
    if status == "Completed":

        delay = random.randint(-30, 60)

        actual_end_date = planned_end_date + timedelta(
            days=delay
        )

    elif status in ["Delayed", "At Risk"]:

        delay = random.randint(30, 180)

        actual_end_date = planned_end_date + timedelta(
            days=delay
        )

    else:

        actual_end_date = None

    # Generate realistic project budgets
    budget = round(
        random.uniform(50000, 2000000),
        2
    )

    # Actual cost varies around budget
    if status == "Completed":

        actual_cost = round(
            budget * random.uniform(0.90, 1.20),
            2
        )

    elif status in ["Delayed", "At Risk"]:

        actual_cost = round(
            budget * random.uniform(0.80, 1.15),
            2
        )

    else:

        actual_cost = round(
            budget * random.uniform(0.30, 0.90),
            2
        )

    project_name = (
        f"{project_type} "
        f"{random.choice(['Programme', 'Implementation', 'Upgrade', 'Transformation', 'Initiative'])} "
        f"{i}"
    )

    projects.append({
        "id": project_id,
        "manager_id": manager["id"],
        "status": status
    })

    cursor.execute("""
        INSERT INTO projects
        (
            project_id,
            project_name,
            department,
            project_manager_id,
            project_type,
            priority,
            status,
            start_date,
            planned_end_date,
            actual_end_date,
            budget,
            actual_cost
        )
        VALUES
        (%s, %s, %s, %s, %s, %s, %s,
         %s, %s, %s, %s, %s)
    """, (
        project_id,
        project_name,
        department,
        manager["id"],
        project_type,
        priority,
        status,
        start_date,
        planned_end_date,
        actual_end_date,
        budget,
        actual_cost
    ))

print("Inserted 120 projects.")

# ---------------------------------------------------------
# 3. RISKS
# ---------------------------------------------------------

risk_count = 0

for project in projects:

    number_of_risks = random.randint(1, 4)

    for _ in range(number_of_risks):

        risk_count += 1

        risk_id = f"RSK{risk_count:03d}"

        category = random.choice(risk_categories)

        probability = random.randint(1, 5)

        impact = random.randint(1, 5)

        risk_score = probability * impact

        if risk_score >= 15:
            status = random.choice([
                "Open",
                "Monitoring"
            ])
        elif risk_score >= 8:
            status = random.choice([
                "Monitoring",
                "Mitigated"
            ])
        else:
            status = random.choice([
                "Mitigated",
                "Closed"
            ])

        description = (
            f"Potential {category.lower()} risk "
            f"affecting project delivery"
        )

        cursor.execute("""
            INSERT INTO risks
            (
                risk_id,
                project_id,
                risk_category,
                risk_description,
                probability,
                impact,
                risk_score,
                status
            )
            VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            risk_id,
            project["id"],
            category,
            description,
            probability,
            impact,
            risk_score,
            status
        ))

print(f"Inserted {risk_count} risks.")

# ---------------------------------------------------------
# 4. ISSUES
# ---------------------------------------------------------

issue_count = 0

for project in projects:

    number_of_issues = random.randint(1, 4)

    for _ in range(number_of_issues):

        issue_count += 1

        issue_id = f"ISS{issue_count:03d}"

        category = random.choice(issue_categories)

        severity = random.choices(
            issue_severities,
            weights=[25, 45, 25, 5]
        )[0]

        status = random.choice(issue_statuses)

        date_raised = date(
            2025,
            random.randint(1, 12),
            random.randint(1, 28)
        )

        if status == "Resolved":

            resolution_days = random.randint(3, 60)

            date_resolved = (
                date_raised +
                timedelta(days=resolution_days)
            )

        else:

            date_resolved = None

        description = (
            f"{category} issue requiring "
            f"project team attention"
        )

        cursor.execute("""
            INSERT INTO issues
            (
                issue_id,
                project_id,
                issue_category,
                description,
                severity,
                status,
                date_raised,
                date_resolved
            )
            VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            issue_id,
            project["id"],
            category,
            description,
            severity,
            status,
            date_raised,
            date_resolved
        ))

print(f"Inserted {issue_count} issues.")

# ---------------------------------------------------------
# 5. RESOURCES
# ---------------------------------------------------------

resource_count = 0

for project in projects:

    number_of_resources = random.randint(4, 10)

    for _ in range(number_of_resources):

        resource_count += 1

        resource_id = f"RES{resource_count:03d}"

        resource_name = fake.name()

        role = random.choice(roles)

        allocated_hours = random.randint(
            100,
            1000
        )

        # Actual hours can be above or below allocation
        actual_hours = int(
            allocated_hours *
            random.uniform(0.70, 1.25)
        )

        cursor.execute("""
            INSERT INTO resources
            (
                resource_id,
                project_id,
                resource_name,
                role,
                allocated_hours,
                actual_hours
            )
            VALUES
            (%s, %s, %s, %s, %s, %s)
        """, (
            resource_id,
            project["id"],
            resource_name,
            role,
            allocated_hours,
            actual_hours
        ))

print(f"Inserted {resource_count} resource assignments.")

# ---------------------------------------------------------
# COMMIT
# ---------------------------------------------------------

connection.commit()

print()
print("======================================")
print("PMO DATA GENERATION COMPLETE")
print("======================================")
print(f"Project managers: 10")
print(f"Projects:         {len(projects)}")
print(f"Risks:            {risk_count}")
print(f"Issues:           {issue_count}")
print(f"Resources:        {resource_count}")
print("======================================")

cursor.close()
connection.close()

print("MySQL connection closed.")