import os
import sqlite3


def a(name):
    print(name + "hello")

# 현재 폴더의 파일과 사이즈 들을 딕셔너리 객체로 만든 후 리스트에 추가하고 튜블로 전환


def get_file_list():

    # 파일 목록을 튜플 리스트로 가져온다,
    file_name_list = os.listdir(".")
    #file_size_list = os.stat("app.py").st_size
    #print(file_name_list, file_size_list)

    # 빈 파일리스트 변수를 생성한다
    file_list = []

    # 파일 목록을 반복하여 딕셔너리 객체("file_name","file_Size", key)를 만들어 파일정보를 넣는다
    for file_name in file_name_list:
        file_size = os.stat(file_name).st_size
        # 파일명과 파일 사이즈를 딕셔너리에 넣는다
        file_dict = {"file_name": file_name, "file_size": file_size}
        #print(file_name_list, file_size, file_dict)
        # 빈 파일 리스트에 하나씩 딕셔너리를 넣는다.
        file_list.append(file_dict)

    # 파일 목록을 튜플 리스트로 변환해 리턴한다.
    return tuple(file_list)

# db 연결 함수


def db_connect():
    con = sqlite3.connect("data.db")

    return con

# 데이터 추가 : 데이터 값(파라미터)를 받아옴


def add_data(file_list):

    try:
        cur = CON.cursor()
        # """은 멀티라인을 지원 변수는 ? 지원
        sql = """
        INSERT INTO new
        (file_name, file_size)
        VALUES(?, ?);
        """

        for file_dict in file_list:

            # SQL 실행 EXCUTE(SQL, (변수들))
            cur.execute(sql, (file_dict["file_name"], file_dict["file_size"]))
        # 반드시 commit를 해야 실행된다
        CON.commit()

        print("insert")
    except Exception as e:
        print(e)
    finally:
        CON.close()


if __name__ == "__main__":

    a("소진")
    file_list = get_file_list()

    # db 연결
    CON = db_connect()
    print(CON)

    CUR = CON.cursor()

    # add_data(file_list)

    while True:

        CUR.execute("select * from new")

        # 한줄읽기
        read1 = CUR.fetchone()
        print(read1)

        # 전부읽기
        read2 = CUR.fetchall()
        print(read2)
