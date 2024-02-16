from flask import Flask
from models import db
from views import add_member, get_member, getlist_member, update_member, delete_member
from config import SQLALCHEMY_DATABASE_URI

# Flask 애플리케이션을 생성
app = Flask(__name__)
# 데이터베이스 연결 정보를 설정
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
# 데이터베이스 객체를 Flask 애플리케이션과 연결
db.init_app(app)

# 데이터베이스 테이블 생성
with app.app_context():
    db.create_all()

# 라우트 설정
app.add_url_rule('/add_member', view_func=add_member, methods=['POST'])
app.add_url_rule('/get_member/<int:id>', view_func=get_member, methods=['GET'])
app.add_url_rule('/getlist_member', view_func=getlist_member, methods=['GET'])
app.add_url_rule('/update_member/<int:id>', view_func=update_member, methods=['PUT'])
app.add_url_rule('/delete_member/<int:id>', view_func=delete_member, methods=['DELETE'])

# 디버그 모드를 활성화하여 애플리케이션을 실행
if __name__ == '__main__':
    app.run(debug=True)
