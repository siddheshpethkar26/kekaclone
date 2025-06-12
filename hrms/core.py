"""Simple in-memory HRMS core engine.
This is a minimal prototype inspired by Keka HRMS features.
"""
from __future__ import annotations

from collections import defaultdict
from datetime import date, datetime
from typing import Dict, List, Optional

from .models import (
    Employee,
    AttendanceRecord,
    LeaveRequest,
    PayrollEntry,
    PerformanceGoal,
    PerformanceReview,
    TrainingCourse,
    JobPosting,
    Application,
    Interview,
)


class HRMS:
    def __init__(self):
        self.employees: Dict[int, Employee] = {}
        self.attendance: List[AttendanceRecord] = []
        self.leave_requests: List[LeaveRequest] = []
        self.payroll: List[PayrollEntry] = []
        self.goals: List[PerformanceGoal] = []
        self.reviews: List[PerformanceReview] = []
        self.courses: List[TrainingCourse] = []
        self.job_postings: List[JobPosting] = []
        self.applications: List[Application] = []
        self.interviews: List[Interview] = []
        self.next_employee_id = 1
        self.next_course_id = 1
        self.next_job_id = 1
        self.next_app_id = 1

    # Employee Management
    def add_employee(
        self, name: str, department: str, designation: str, doj: date, email: str,
        manager_id: Optional[int] = None
    ) -> Employee:
        emp = Employee(
            id=self.next_employee_id,
            name=name,
            department=department,
            designation=designation,
            date_of_joining=doj,
            email=email,
            manager_id=manager_id,
        )
        self.employees[emp.id] = emp
        self.next_employee_id += 1
        return emp

    def get_employee(self, emp_id: int) -> Optional[Employee]:
        return self.employees.get(emp_id)

    def list_employees(self) -> List[Employee]:
        return list(self.employees.values())

    def update_employee(self, emp_id: int, **updates) -> Optional[Employee]:
        emp = self.employees.get(emp_id)
        if not emp:
            return None
        for key, value in updates.items():
            if hasattr(emp, key):
                setattr(emp, key, value)
        return emp

    # Attendance Management
    def record_attendance(
        self, employee_id: int, timestamp: Optional[datetime] = None,
        type: str = "check_in", location: Optional[str] = None
    ) -> AttendanceRecord:
        rec = AttendanceRecord(
            employee_id=employee_id,
            timestamp=timestamp or datetime.now(),
            type=type,
            location=location,
        )
        self.attendance.append(rec)
        return rec

    def get_attendance(self, emp_id: int) -> List[AttendanceRecord]:
        return [a for a in self.attendance if a.employee_id == emp_id]

    # Leave Management
    def apply_leave(
        self, employee_id: int, start_date: date, end_date: date, leave_type: str
    ) -> LeaveRequest:
        lr = LeaveRequest(
            employee_id=employee_id,
            start_date=start_date,
            end_date=end_date,
            leave_type=leave_type,
        )
        self.leave_requests.append(lr)
        return lr

    def list_leave_requests(self, employee_id: Optional[int] = None) -> List[LeaveRequest]:
        if employee_id is None:
            return self.leave_requests
        return [lr for lr in self.leave_requests if lr.employee_id == employee_id]

    # Payroll Management
    def add_payroll_entry(
        self, employee_id: int, month: int, year: int, basic: float,
        allowances: float, deductions: float, taxes: float
    ) -> PayrollEntry:
        net = basic + allowances - deductions - taxes
        pe = PayrollEntry(
            employee_id=employee_id,
            month=month,
            year=year,
            basic=basic,
            allowances=allowances,
            deductions=deductions,
            taxes=taxes,
            net_pay=net,
        )
        self.payroll.append(pe)
        return pe

    def get_payroll_entries(self, employee_id: int) -> List[PayrollEntry]:
        return [p for p in self.payroll if p.employee_id == employee_id]

    # Performance Management
    def add_goal(self, employee_id: int, goal: str, due_date: date) -> PerformanceGoal:
        g = PerformanceGoal(employee_id=employee_id, goal=goal, due_date=due_date)
        self.goals.append(g)
        return g

    def record_review(
        self, employee_id: int, reviewer_id: int, date: date, comments: str, rating: int
    ) -> PerformanceReview:
        pr = PerformanceReview(
            employee_id=employee_id,
            reviewer_id=reviewer_id,
            date=date,
            comments=comments,
            rating=rating,
        )
        self.reviews.append(pr)
        return pr

    # Learning & Development
    def create_course(self, title: str, description: str) -> TrainingCourse:
        course = TrainingCourse(id=self.next_course_id, title=title, description=description)
        self.courses.append(course)
        self.next_course_id += 1
        return course

    def assign_course(self, course_id: int, employee_id: int) -> Optional[TrainingCourse]:
        course = next((c for c in self.courses if c.id == course_id), None)
        if not course:
            return None
        course.assigned_to.append(employee_id)
        return course

    def complete_course(self, course_id: int, employee_id: int) -> Optional[TrainingCourse]:
        course = next((c for c in self.courses if c.id == course_id), None)
        if not course:
            return None
        course.completed_by.append(employee_id)
        return course

    # Recruitment
    def create_job_posting(self, title: str, description: str, department: str) -> JobPosting:
        job = JobPosting(id=self.next_job_id, title=title, description=description, department=department)
        self.job_postings.append(job)
        self.next_job_id += 1
        return job

    def apply_for_job(self, job_id: int, candidate_name: str, resume: str) -> Application:
        app = Application(id=self.next_app_id, job_id=job_id, candidate_name=candidate_name, resume=resume)
        self.applications.append(app)
        self.next_app_id += 1
        return app

    def schedule_interview(
        self, application_id: int, interviewer: str, when: datetime
    ) -> Interview:
        interview = Interview(application_id=application_id, interviewer=interviewer, date=when)
        self.interviews.append(interview)
        return interview

    # Analytics
    def headcount(self) -> int:
        return len([e for e in self.employees.values() if e.status == "active"])


    # AI placeholder features
    def predict_attrition(self, employee_id: int) -> float:
        """Return a dummy attrition risk score between 0 and 1."""
        # Placeholder: Real implementation would use ML model
        emp = self.get_employee(employee_id)
        if not emp:
            return 0.0
        tenure_days = (date.today() - emp.date_of_joining).days
        if tenure_days < 365:
            return 0.5
        return 0.2
