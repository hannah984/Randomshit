from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def clickingAround():
  return render_template("contact.html")

if __name__ == "__main__":
  app.run(port='23456')
