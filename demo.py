"""Example usage of the HRMS package."""
from datetime import date, datetime, timedelta
from hrms import HRMS


def main():
    hrms = HRMS()
    # Add an employee
    emp = hrms.add_employee(
        name="Alice",
        department="Engineering",
        designation="Developer",
        doj=date(2024, 1, 1),
        email="alice@example.com",
    )
    print("Added employee", emp)

    # Record attendance
    att = hrms.record_attendance(emp.id)
    print("Attendance record", att)

    # Apply leave
    leave = hrms.apply_leave(emp.id, date(2024, 5, 1), date(2024, 5, 5), "vacation")
    print("Leave request", leave)

    # Add payroll
    payroll = hrms.add_payroll_entry(emp.id, 5, 2024, 5000, 500, 200, 300)
    print("Payroll entry", payroll)

    # Performance goal
    goal = hrms.add_goal(emp.id, "Finish project X", date(2024, 12, 31))
    print("Added goal", goal)

    review = hrms.record_review(emp.id, emp.id, date.today(), "Great job", 5)
    print("Performance review", review)

    # Training course
    course = hrms.create_course("Security Training", "Basics of security")
    hrms.assign_course(course.id, emp.id)
    hrms.complete_course(course.id, emp.id)
    print("Course", course)

    # Recruitment
    job = hrms.create_job_posting("Tester", "QA role", "QA")
    app = hrms.apply_for_job(job.id, "Bob", "bob_resume.pdf")
    interview = hrms.schedule_interview(app.id, "Carol", datetime.now() + timedelta(days=1))
    print("Interview scheduled", interview)

    # Predict attrition
    score = hrms.predict_attrition(emp.id)
    print("Attrition risk score", score)


if __name__ == "__main__":
    main()
