from model import Person
from error import Error
from typing import Dict, List
from datetime import datetime


def get_age(birthdate):
    birth_date = datetime.strptime(birthdate, '%Y%m%d')
    current_date = datetime.now()
    age = (current_date - birth_date).days // 365
    return age


def process(record: Person):
    if record.objectInfo is None:
        return
    if record.objectInfo["户类型"] == "脱贫户":
        birthdate = record.objectInfo['出生日期']
        age = get_age(birthdate)
        if age >= 16 and age < 60:
            if record.objectInfo["健康状况"] != "健康":
                if record.objectInfo["劳动技能"] == "普通劳动力" and record.objectInfo["劳动技能"] == "技能劳动能力":
                        raise Error(no='5_12_009-16', objectInfo=[record.objectInfo])
