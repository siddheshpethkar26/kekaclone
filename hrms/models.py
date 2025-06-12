from dataclasses import dataclass, field
from datetime import date, datetime
from typing import List, Optional

@dataclass
class Employee:
    id: int
    name: str
    department: str
    designation: str
    date_of_joining: date
    email: str
    manager_id: Optional[int] = None
    status: str = "active"  # active, on_leave, exited

@dataclass
class AttendanceRecord:
    employee_id: int
    timestamp: datetime
    type: str  # check_in, check_out
    location: Optional[str] = None

@dataclass
class LeaveRequest:
    employee_id: int
    start_date: date
    end_date: date
    leave_type: str
    status: str = "pending"  # pending, approved, rejected

@dataclass
class PayrollEntry:
    employee_id: int
    month: int
    year: int
    basic: float
    allowances: float
    deductions: float
    taxes: float
    net_pay: float

@dataclass
class PerformanceGoal:
    employee_id: int
    goal: str
    due_date: date
    status: str = "open"  # open, achieved, missed

@dataclass
class PerformanceReview:
    employee_id: int
    reviewer_id: int
    date: date
    comments: str
    rating: int  # 1-5

@dataclass
class TrainingCourse:
    id: int
    title: str
    description: str
    assigned_to: List[int] = field(default_factory=list)
    completed_by: List[int] = field(default_factory=list)

@dataclass
class JobPosting:
    id: int
    title: str
    description: str
    department: str

@dataclass
class Application:
    id: int
    job_id: int
    candidate_name: str
    resume: str
    status: str = "applied"  # applied, interviewed, offered, rejected

@dataclass
class Interview:
    application_id: int
    interviewer: str
    date: datetime
    feedback: str = ""

