from flask import render_template, request, abort
from webapp import app
from base64 import b64decode, b64encode
def base64Encode(data):
    return b64encode(data.encode('utf-8')).decode('utf-8')
def base64Decoded(data):
    if not data or len(data) > 999:
        return None
    try:
        data = data.rstrip('=')
        if len(data) % 4:
            data += '=' * (4 - len(data) % 4)
        decoded = b64decode(data).decode('utf-8')
        return decoded
    except Exception:
        return None
def outcomesValidated(outcome):
    expectedOutcomes = ["win!", "lose :(", "draw"]
    return outcome in expectedOutcomes
def boardValidated(board):
    cells = board.split(",")
    if len(cells) != 9:
        return False
    return all(cell in ["", "X", "O"] for cell in cells)
@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')
@app.route("/end", methods=["GET"])
def handle_end():
    encodedOutcome = request.args.get("outcome", "").strip()
    encodedBoard = request.args.get("board", "").strip()
    outcome = base64Decoded(encodedOutcome)
    board = base64Decoded(encodedBoard)
    if not board or not boardValidated(board):
        board = ",".join([""for _ in range(9)])
    else:
        board = ",".join(board.split(",")) 
    encodedBoard = base64Encode(board)
    if not outcome or not outcomesValidated(outcome):
        outcome = "Outcome is not valid"
    encodedOutcome = base64Encode(outcome)
    return render_template('end.html', result=encodedOutcome, board=encodedBoard)
