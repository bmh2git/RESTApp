__author__ = 'hashbang'

from flask import Flask

phrases = ["When you come to a fork in the road, take it.",
"You can observe a lot by just watching.",
"It aint over till its over",
"No one goes there nowadays, its too crowded.",
"Baseball is ninety percent mental and the other half is physical.",
"Always go to other people's funerals, otherwise they won't come to yours.",
"A nickel ain't worth a dime anymore.",
"It's like deja vu all over again.",
"We made too many wrong mistakes.",
"Congratulations. I knew the record would stand until it was broken.",
"A nickel aint worth a dime anymore."]

app = Flask(__name__)
index = 0

@app.route("/",methods=["GET"])
def get():
    print phrases[index]
    return phrases[index] + '\n'

@app.route("/",methods=["POST"])
def update():
    global index
    index = (index+1)%len(phrases)
    return "updated\n"

if __name__ == "__main__":
    app.run(port=9080)