from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:viveksray7@postgres:5432/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self) -> str:
        return f"Todo(title:'{self.title}', description:'{self.description}')"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        todo_title = request.form["todo_title"]
        todo_description = request.form["todo_description"]
        todo = Todo(title=todo_title, description=todo_description)
        db.session.add(todo)
        db.session.commit()
    return render_template("home.djhtml")


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
