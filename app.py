from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/memo', methods=['POST'])
def post_software():
    # 1. 클라이언트로부터 데이터를 받기
    name_receive = request.form['name_give']  # 클라이언트로부터 comment를 받는 부분
    category_receive = request.form['category_give']  # 클라이언트로부터 comment를 받는 부분
    comment_receive = request.form['comment_give']  # 클라이언트로부터 comment를 받는 부분
    homepage_receive = request.form['homepage_give']  # 클라이언트로부터 comment를 받는 부분
    gpdown_receive = request.form['gpdown_give']  # 클라이언트로부터 comment를 받는 부분
    asdown_receive = request.form['asdown_give']  # 클라이언트로부터 comment를 받는 부분
    image_receive = request.form['image_give']  # 클라이언트로부터 url을 받는 부분

    software = {'name': name_receive, 'category': category_receive, 'comment': comment_receive, 'homepage': homepage_receive, 'gwdown': gpdown_receive, 'asdown': asdown_receive,'image': image_receive}

    # 3. mongoDB에 데이터를 넣기
    db.softwares.insert_one(software)

    return jsonify({'result': 'success'})


@app.route('/memo', methods=['GET'])
def read_software():
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기 (Read)
    result = list(db.softwares.find({}, {'_id': 0}))
    # 2. articles라는 키 값으로 article 정보 보내주기
    return jsonify({'result': 'success', 'softwares': result})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)