import time
import pywinmacro as pw
import random


def weather():
    # 실행 프로그램으로 크롬 시크릿모드 실행
    pw.key_on("window")
    pw.key_on("r")
    pw.key_off("window")
    pw.key_off("r")
    time.sleep(1)
    pw.type_in("chrome -incognito")
    pw.key_press_once("enter")
    time.sleep(random.randint(1,3))

    # 구글에서 검색
    pw.type_in("서울 날씨")
    pw.key_press_once("enter")

weather()