from flask import request


@app.route("/", methods=["GET", "POST"])
def parse_request():
    data = request.data


import web

urls = ("/.*", "hooks")

app = web.application(urls, globals())


class hooks:
    def POST(self):
        data = web.data()
        print("")
        print("DATA RECEIVED:")
        print(data)
        print("")

        return "OK"

    def GET(self):
        try:
            data = web.input()
            data = data["hub.challenge"]
            print("Hub challenge: ", data)
            return data
        except KeyError:
            return web.BadRequest


if __name__ == "__main__":
    app.run()
