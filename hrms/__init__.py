"""Minimal HRMS package."""

from .core import HRMS
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

__all__ = [
    "HRMS",
    "Employee",
    "AttendanceRecord",
    "LeaveRequest",
    "PayrollEntry",
    "PerformanceGoal",
    "PerformanceReview",
    "TrainingCourse",
    "JobPosting",
    "Application",
    "Interview",
]
