from flask import Flask, request, jsonify, make_response
import json
import models as db
import validator

app = Flask(__name__)


@app.route("/api/sign_up", methods=["POST", "GET"])
def signup():
    try:
        if request.method == "POST":
            data = request.get_json()
            print(data["name"])
            name = data["name"]
            email = data["email"]
            password = data["password"]
            validatePass = validator.CheckPassword(password)
            if not validatePass:
                message = jsonify({"success": False})
                return make_response(message, 400)
            else:
                user = db.insertUser(name, email, password)
                if user:
                    message = jsonify({"success": True})
                    return make_response(message, 201)
                else:
                    message = jsonify({"success": False})
                    return make_response(message, 400)
        else:
            message = jsonify({"success": False})
            return make_response(message, 400)
    except Exception as e:
        # print(e)
        message = jsonify({"success": False})
        return make_response(message, 500)


@app.route("/api/sign_in", methods=["POST", "GET"])
def viewData():
    try:
        if request.method == "POST":
            data = request.get_json()
            email = data["email"]
            password = data["password"]
            userEmail = db.checkDuplicate(email)
            userPassw = db.checkPassword(password, email)
            if userEmail == None:
                message = jsonify({"success": False})
                return make_response(message, 400)
            else:
                if userPassw[0] == password:
                    message = jsonify({"success": True})
                    return make_response(message, 200)
                else:
                    message = jsonify({"success": False})
                    return make_response(message, 400)
        else:
            message = jsonify({"success": False})
            return make_response(message, 400)
    except Exception as e:
        # print(e)
        message = jsonify({"success": False})
        return make_response(message, 500)


@app.route("/api/clean", methods=["POST", "GET"])
def clean():
    try:
        if request.method == "POST":
            res = db.delete()
            if res:
                message = jsonify({"success": True})
                return make_response(message)
            else:
                message = jsonify({"success": False})
                return make_response(message)
        else:
            message = jsonify({"success": False})
            return make_response(message, 400)
    except Exception as e:
        message = jsonify({"success": False})
        return make_response(message, 500)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
