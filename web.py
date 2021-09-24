from flask import Flask, render_template
import workloads
import controllers


app = Flask(__name__)


@app.route("/")
def main():
    operator_list = controllers.test_suites.keys()
    return render_template("index.html", name="\n".join(operator_list))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
