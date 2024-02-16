from flask import request, jsonify
from models import db, Member

# 회원 추가
def add_member():
    try:
        data = request.json
        # Member 모델에 생성자를 명시하지 않아도 기본 생성자를 제공해줌
        new_member = Member(name=data['name'], email=data['email'], address=data['address'], password=data['password'])
        # 해당 레코드를 세션에 추가
        db.session.add(new_member)
        # 추가된 레코드를 디비에 반영 커밋 처리
        db.session.commit()
        # 추가된 레코드 id 값 표시
        data['id'] = new_member.id
        return jsonify({'status': 'success', 'data': data})
    except Exception as e:
        error_msg = str(e)
        # 예외 발생시 롤백 처리
        db.session.rollback()
        print(f" ===== msg : {error_msg} =====")
        return jsonify({'status': 'fail', 'msg': error_msg})

# 회원 조회
def get_member(id):
    try:
        # key 값으로 데이터를 조회하고 없으면 404 에러 발생
        member = Member.query.get_or_404(id)
        return jsonify({'status': 'success', 'data' : {'id': member.id, 'name': member.name, 'email': member.email, 'address': member.address}})
    except Exception as e:
        error_msg = str(e)
        print(f" ===== msg : {error_msg} =====")
        return jsonify({'status': 'fail', 'msg': error_msg})
    
# 회원 리스트 조회
def getlist_member():
    try:
        member_list = Member.query.all()  # 메서드 호출을 위해 소괄호 추가
        return jsonify({'status': 'success', 'data' : [member.serialize() for member in member_list]})
    except Exception as e:
        error_msg = str(e)
        print(f" ===== msg : {error_msg} =====")
        return jsonify({'status': 'fail', 'msg': error_msg})

# 회원 수정
def update_member(id):
    try:
        data = request.json
        # key 값으로 데이터를 조회하고 없으면 404 에러 발생
        member = Member.query.get_or_404(id)
        member.name = data['name']
        member.email = data['email']
        member.address = data['address']
        member.password = data['password']
        # 추가된 레코드를 디비에 반영 커밋 처리
        # 데이터를 가져와서 수정하기에 add_member() 와 달리 db.session.add 과정이 없음
        db.session.commit()
        return jsonify({'status': 'sucess', 'data' : {'id': member.id, 'name': member.name, 'email': member.email, 'address': member.address}})
    except Exception as e:
        error_msg = str(e)
        # 예외 발생시 롤백 처리
        db.session.rollback()
        print(f" ===== msg : {error_msg} =====")
        return jsonify({'status': 'fail', 'msg': error_msg})

# 회원 삭제
def delete_member(id):
    try:
        member = Member.query.get_or_404(id)
        # 레코드에서 삭제 처리
        db.session.delete(member)
        # 삭제된 레코드를 디비에 반영 커밋 처리
        db.session.commit()
        return jsonify({'status': 'sucess'})
    except Exception as e:
        error_msg = str(e)
        # 예외 발생시 롤백 처리
        db.session.rollback()
        print(f" ===== msg : {error_msg} =====")
        return jsonify({'status': 'fail', 'msg': error_msg})
