from tgbot.services.database.db import Base

from tgbot.models.student import Student
from tgbot.models.subject import Subject
from tgbot.models.subject_type import SubjectType
from tgbot.models.user import User
from tgbot.models.submission import Submission
from tgbot.models.day import Day
from tgbot.models.couple import Couple
from tgbot.models.timetable import Timetable
from tgbot.models.timetable_date import TimetableDate
from tgbot.models.teacher import Teacher
from tgbot.models.links import Link
from tgbot.models.links_tabs import LinkTab


def create_tables(engine):
    Base.metadata.create_all(engine)
