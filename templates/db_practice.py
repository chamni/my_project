from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.

# MongoDB에 insert 하기

# 'users'라는 collection에 데이터를 생성합니다.
db.softwares.insert_one({'name': 'Notion', 'category': '##', 'comment': '여러사람에게 동일한 정보를 공유하는 데 도움', 'gwdown': '###', 'asdown': '##', 'image': '##'})

