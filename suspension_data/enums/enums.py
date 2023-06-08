from enum import unique

from utils import AutoCheckRecognizableStrEnum


@unique
class Gender(AutoCheckRecognizableStrEnum):
    BOY = '男'
    GIRL = '女'
    OTHER = '其他'


@unique
class SchoolType(AutoCheckRecognizableStrEnum):
    PUBLIC = '公立'
    PRIVATE = '私立'
    OTHER = '其他'


@unique
class EducationProgram(AutoCheckRecognizableStrEnum):
    ASSOCIATE_DEGREE = "專科"
    BACHELORS = "學士班"
    DAYTIME_DOCTORAL = "博士日間"
    DAYTIME_MASTERS = "碩士日間"
    DOCTORAL = "博士班"
    EXECUTIVE_DOCTORAL = "博士在職"
    EXECUTIVE_MASTERS = "碩士在職"
    FOUR_PLUS_X = "4+X"
    FOUR_PLUS_X_EXTENSION = "4+X進修"
    FOUR_YEAR_COLLEGE_EXTENSION = "大學四年制進修"
    FOUR_YEAR_DAYTIME_COLLEGE = "大學四年制日間"
    FIVE_YEAR_ASSOCIATE_DEGREE = "五專"
    MASTERS = "碩士班"
    MASTERS_SUMMER = "碩士暑"
    TWO_YEAR_ASSOCIATE_DEGREE_EXTENSION = "二專進修"
    TWO_YEAR_COLLEGE_EXTENSION = "大學二年制進修"
    TWO_YEAR_DAYTIME_ASSOCIATE_DEGREE = "二專日間"
    TWO_YEAR_DAYTIME_COLLEGE = "大學二年制日間"
    OTHER = "其他"


@unique
class SuspensionReason(AutoCheckRecognizableStrEnum):
    WORK_REQUIREMENTS = "因工作需求"
    TRAVEL_ABROAD = "因出國"
    EXAM_TRAINING = "因考試訓練"
    MILITARY_SERVICE = "因兵役"
    DISINTEREST = "因志趣不合"
    PARENTING = "因育嬰"
    FAMILY_ILLNESS = "因家人傷病"
    ILLNESS = "因傷病"
    FINANCIAL_DIFFICULTIES = "因經濟困難"
    OVERDUE_REGISTRATION = "因逾期未註冊、繳費、選課"
    THESIS_WRITING = "因論文撰寫"
    ADJUSTMENT_DIFFICULTIES = "因適應不良"
    POOR_GRADES = "因學業成績不佳"
    PREGNANCY = "因懷孕"
    OTHER = "其他"
