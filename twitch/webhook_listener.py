from flask import Flask, request


app = Flask(__name__)


@app.route("/", methods=["POST"])
def parse_request():
    data = request.data
    print(data)


@app.route("/", methods=["GET"])
def parse_get_request():
    try:
        data = request.data
        data = data["hub.challenge"]
        return data
    except KeyError:
        return "error"


if __name__ == "__main__":
    app.run()
#
# urls = ("/.*", "hooks")
#
# app = web.application(urls, globals())
#
#
# class hooks:
#     def POST(self):
#         data = web.data()
#         print("")
#         print("DATA RECEIVED:")
#         print(data)
#         print("")
#
#         return "OK"
#
#     def GET(self):
#         try:
#             data = web.input()
#             data = data["hub.challenge"]
#             print("Hub challenge: ", data)
#             return data
#         except KeyError:
#             return web.BadRequest
#
#
# if __name__ == "__main__":
#     app.run()
