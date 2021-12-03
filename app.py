import os
import sqlite3


def a(name):
    print(name + "hello")


def show_ls():
    x = os.listdir(".")
    print(x)

# db 연결 함수


def db_connect():
    con = sqlite3.connect("data.db")

    return con

# 데이터 추가 : 데이터 값(파라미터)를 받아옴


def add_data(file_name, file_size):

    try:
        cur = CON.cursor()
        # """은 멀티라인을 지원 변수는 ? 지원
        sql = """
        INSERT INTO new
        (file_name, file_size)
        VALUES(?, ?);
        """

        # SQL 실행 EXCUTE(SQL, (변수들))
        cur.execute(sql, (file_name, file_size))
        # 반드시 commit를 해야 실행된다
        CON.commit()

        print("insert")
    except Exception as e:
        print(e)
    finally:
        CON.close()


if __name__ == "__main__":

    a("소진")
    show_ls()

    # db 연결
    CON = db_connect()
    print(CON)

    #CUR = CON.cursor()

    add_data("파일명.http", 100)
