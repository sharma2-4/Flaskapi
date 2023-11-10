from flask import ( request, jsonify, Flask)
from datetime import timedelta

from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager
from db import Students


app = Flask(__name__)
jwt = JWTManager(app)



# Configurations
app.config["JWT_SECRET_KEY"] = "62BE71"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours = 1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days = 30)






@app.post("/login")
def login():
    if request.is_json:
        reg_no = request.json["register_no"]
        dpt = request.json["department"]
        student = Students.Verify(reg_no,dpt)
        if student:
            token = create_access_token(identity=reg_no,additional_claims={"hello":"world"})
            return jsonify(token=token)
        if student is False: return jsonify(error = "Department Wrong"), 415
        return jsonify(error = "Student Not Found.."), 415

    return jsonify({"error" : "invalid Format"}), 415



@app.get("/")
@jwt_required()
def main():

    current_student = Students.GetStudent(get_jwt_identity())
    return jsonify(current_student = current_student)




if __name__ == "__main__":
    print(app.config.JWT_ACCESS_TOKEN_EXPIRES)
