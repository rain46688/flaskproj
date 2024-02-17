from app import db

# 모델 정의
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(200))
    password = db.Column(db.String(100), nullable=False)

    # 객체를 JSON 형식으로 직렬화 기능
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'address': self.address,
            'password': self.password
        }

# 객체 매핑할때 사용
    def __repr__(self):
        return '<Member %r>' % self.name
        