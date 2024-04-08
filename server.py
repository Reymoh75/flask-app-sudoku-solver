from flask import Flask,render_template,request,redirect,flash,get_flashed_messages,url_for
from solver import Sudoku

app = Flask(__name__)
app.secret_key = b'my secret key'

@app.get("/")
def index():
    puzzle = get_flashed_messages()[0] if (len(get_flashed_messages())>0) else False
    return render_template("index.html",puzzle=puzzle)


@app.post("/solve")
def solve():
    puzzle = [[0 for i in range(9)] for j in range(9)]
    for input in request.form :
        i = int(input.split("-")[0])
        j = int(input.split("-")[1])
        value = int(request.form[input]) if request.form[input] else 0
        puzzle[j-1][i-1] = value 

    sudoku = Sudoku(puzzle)
    sudoku.solve()
    
    flash(sudoku.puzzle)
    return redirect(url_for("index"))