from flask import Flask
from config import SQLALCHEMY_DATABASE_URI
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# 객체 생성
db = SQLAlchemy() 

def create_app():

    # Flask 애플리케이션을 생성
    app = Flask(__name__)
    # 데이터베이스 연결 정보를 설정
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    # 데이터베이스 객체를 Flask 애플리케이션과 연결
    db.init_app(app)

    from models import Member
    Migrate(app, Member)

    # 데이터베이스 테이블 생성
    with app.app_context():
        db.create_all()

    # 라우트 설정
    # app.add_url_rule('/add_member', view_func=add_member, methods=['POST'])
    # app.add_url_rule('/get_member/<int:id>', view_func=get_member, methods=['GET'])
    # app.add_url_rule('/getlist_member', view_func=getlist_member, methods=['GET'])
    # app.add_url_rule('/update_member/<int:id>', view_func=update_member, methods=['PUT'])
    # app.add_url_rule('/delete_member/<int:id>', view_func=delete_member, methods=['DELETE'])

    from views import member_bp
    app.register_blueprint(member_bp, url_prefix='/members')

    return app

# 디버그 모드를 활성화하여 애플리케이션을 실행
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
