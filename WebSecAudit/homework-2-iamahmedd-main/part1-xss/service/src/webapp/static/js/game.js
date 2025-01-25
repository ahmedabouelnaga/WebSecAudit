var SPACE = "&nbsp;";
class TicTacToe {
    constructor(element) {
        this.view = element;
        this.model = Array.from(Array(3), () => new Array(3));
        this.initializeBoard();
    }
    initializeBoard() {
        this.view.classList.add("gameboard");
        for (var row = 0; row < this.model.length; row++) {
            for (var col = 0; col < this.model[row].length; col++) {
                this.model[row][col] = SPACE;
            }
        }
        this.userTurn = true;
        this.active = true;
    }
  
    play() {
        this.drawBoard();
    }

    drawBoard() {    
        var self = this;
        while (this.view.firstChild) {
            this.view.removeChild(this.view.firstChild);
        }
        for (var row_index = 0; row_index < this.model.length; row_index++) {
            var row = document.createElement("div");
            row.classList.add("gameboard-row");
            for(var col_index = 0; col_index < this.model[row_index].length; col_index++) {
                var col = document.createElement("span");
                col.classList.add("gameboard-col");
                col.classList.add("r"+row_index+"_c"+col_index);
                col.innerHTML= this.model[row_index][col_index];
                if(col.innerHTML == SPACE && this.active) {
                    col.classList.add("gameboard-empty");
                    col.onclick = function(self) {
                        var self = self;
                        var cur_row_index = row_index;
                        var cur_col_index = col_index;
                        return function() {
                            if (self.userTurn == false) {
                                return;
                            }
                            console.log(cur_row_index + " " + cur_col_index);
                            self.model[cur_row_index][cur_col_index] = "X";
                            self.userTurn = false;
                            self.drawBoard();
                            setTimeout(function() {self.computerTurn();}, 500);
                        };
                    }(this)
                }
                row.appendChild(col)
            }
            this.view.appendChild(row);
        }
        if(this.active)
            this.checkForGameEnd();
    }
    getEmptySpaces() {
        const available_turns = new Set()
        for (var row = 0; row < this.model.length; row++) {
            for (var col = 0; col < this.model[row].length; col++) {
                if(this.model[row][col] == SPACE) {
                    available_turns.add([row,col]);
                }
            }
        }
        let items = Array.from(available_turns);
        return items;
    }
    checkForGameEnd() {
        var hasWinner = this.checkForWin();
        if(hasWinner == "X") {
            this.triggerWin();
        } else if(hasWinner == "O") {
            this.triggerLose();
        } else if(this.getEmptySpaces().length == 0) {
            this.triggerDraw();
        } else {
            return false;
        }
        this.active = false;
        return true;
    }
    checkForWin() {
        if (this.model[0][0] == this.model[0][1] &&
            this.model[0][1] == this.model[0][2] )
            return this.model[0][0];
        if (this.model[1][0] == this.model[1][1] &&
            this.model[1][1] == this.model[1][2] )
            return this.model[1][0];
        if (this.model[2][0] == this.model[2][1] &&
            this.model[2][1] == this.model[2][2] )
            return this.model[2][0];
        if (this.model[0][0] == this.model[1][0] &&
            this.model[1][0] == this.model[2][0] )
            return this.model[0][0];
        if (this.model[0][1] == this.model[1][1] &&
            this.model[1][1] == this.model[2][1] )
            return this.model[0][1];
        if (this.model[0][2] == this.model[1][2] &&
            this.model[1][2] == this.model[2][2] )
            return this.model[0][2];
        if (this.model[0][0] == this.model[1][1] &&
            this.model[1][1] == this.model[2][2] )
            return this.model[0][0];
        if (this.model[0][2] == this.model[1][1] &&
            this.model[1][1] == this.model[2][0] )
            return this.model[1][1];
        return "";
    }
    checkForBlockingMove() {
        var move = [-1,-1]
        var X = "X";
        if (
            (this.model[0][0] == X && this.model[0][1] == X) ||
            (this.model[2][0] == X && this.model[1][1] == X) ||
            (this.model[2][2] == X && this.model[1][2] == X)
        ) {
            move = [0,2];
        } else if (
            (this.model[0][2] == X && this.model[0][1] == X) ||
            (this.model[2][0] == X && this.model[1][0] == X) ||
            (this.model[2][2] == X && this.model[1][1] == X)
        ) {
            move = [0,0];
        } else if (
            (this.model[0][0] == X && this.model[1][0] == X) ||
            (this.model[2][1] == X && this.model[2][2] == X) ||
            (this.model[0][2] == X && this.model[1][1] == X)
        ) {
            move = [2,0]
        } else if (
            (this.model[0][2] == X && this.model[1][2] == X) ||
            (this.model[2][1] == X && this.model[2][0] == X) ||
            (this.model[0][0] == X && this.model[1][1] == X)
        ) {
            move = [2,2]
        } else if (
            (this.model[0][0] == X && this.model[2][2] == X) ||
            (this.model[1][0] == X && this.model[1][2] == X) ||
            (this.model[0][1] == X && this.model[2][1] == X) ||
            (this.model[0][2] == X && this.model[2][0] == X)
        ) {
            move = [1,1]
        } else if (
            (this.model[0][0] == X && this.model[0][2] == X) ||
            (this.model[1][1] == X && this.model[2][1] == X)
        ) {
            move = [0,1]
        } else if (
            (this.model[2][0] == X && this.model[2][2] == X) ||
            (this.model[1][1] == X && this.model[0][1] == X)
        ) {
            move = [2,1]
        } else if (
            (this.model[0][0] == X && this.model[0][2] == X) ||
            (this.model[1][1] == X && this.model[1][2] == X)
        ) {
            move = [1,0]
        } else if (
            (this.model[2][0] == X && this.model[2][2] == X) ||
            (this.model[1][1] == X && this.model[1][0] == X)
        ) {
            move = [1,2]
        }
        return move;
    }
    checkForWinningMove() {
        var move = [-1,-1]
        var O = "O";
        if (
            (this.model[0][0] == O && this.model[0][1] == O) ||
            (this.model[2][0] == O && this.model[1][1] == O) ||
            (this.model[2][2] == O && this.model[1][2] == O)
        ) {
            move = [0,2];
        } else if (
            (this.model[0][2] == O && this.model[0][1] == O) ||
            (this.model[2][0] == O && this.model[1][0] == O) ||
            (this.model[2][2] == O && this.model[1][1] == O)
        ) {
            move = [0,0];
        } else if (
            (this.model[0][0] == O && this.model[1][0] == O) ||
            (this.model[2][1] == O && this.model[2][2] == O) ||
            (this.model[0][2] == O && this.model[1][1] == O)
        ) {
            move = [2,0]
        } else if (
            (this.model[0][2] == O && this.model[1][2] == O) ||
            (this.model[2][1] == O && this.model[2][0] == O) ||
            (this.model[0][0] == O && this.model[1][1] == O)
        ) {
            move = [2,2]
        } else if (
            (this.model[0][0] == O && this.model[2][2] == O) ||
            (this.model[1][0] == O && this.model[1][2] == O) ||
            (this.model[0][1] == O && this.model[2][1] == O) ||
            (this.model[0][2] == O && this.model[2][0] == O)
        ) {
            move = [1,1]
        } else if (
            (this.model[0][0] == O && this.model[0][2] == O) ||
            (this.model[1][1] == O && this.model[2][1] == O)
        ) {
            move = [0,1]
        } else if (
            (this.model[2][0] == O && this.model[2][2] == O) ||
            (this.model[1][1] == O && this.model[0][1] == O)
        ) {
            move = [2,1]
        } else if (
            (this.model[0][0] == O && this.model[0][2] == O) ||
            (this.model[1][1] == O && this.model[1][2] == O)
        ) {
            move = [1,0]
        } else if (
            (this.model[2][0] == O && this.model[2][2] == O) ||
            (this.model[1][1] == O && this.model[1][0] == O)
        ) {
            move = [1,2]
        }
        return move;
    }
    computerTurn() {
        if(this.userTurn) {
            return 0;
        }
        if(!this.active) {
            return 0;
        }
        var move = [-1,-1];
        move = this.checkForWinningMove();
        
        if (move[0] == -1 || this.model[move[0]][move[1]] != SPACE) {
            move = this.checkForBlockingMove();
        }
        if (move[0] == -1 || this.model[move[0]][move[1]] != SPACE) {
            var emptySpaces = this.getEmptySpaces();
            if(emptySpaces.length > 0) {
                move = emptySpaces[Math.floor(Math.random() * emptySpaces.length)];
            } else {
                this.triggerDraw();
            }
        }
        if(move[0] != -1 && this.model[move[0]][move[1]] == SPACE) {
            console.log(move);
            this.model[move[0]][move[1]] = "O";
            this.drawBoard();
            this.userTurn = true;
            return 0;
        }
    }
    stringToGameboard(gameString) {
        var elements = gameString.split(",");
        for (var index = 0; index< elements.length; index++) {
            var el = elements[index];
            var row = Math.floor(index /3); 
            var col = index %3;
            if (el == "") {
                this.model[row][col] = SPACE
            } else {
                this.model[row][col] = el;
            }
            
        }
    }
    gameboardToString() {
        var returnString = "";
        for (var row = 0; row < this.model.length; row++) {
            for (var col = 0; col < this.model[row].length; col++) {
                var cell = this.model[row][col];
                returnString += cell == SPACE ? "" : cell;
		if(!(row == 2 && col == 2)){
                returnString += ",";
            }
        }
	}
        return returnString;
    }
    redirectToEnd(outcome) {
        var board = this.gameboardToString();
        window.location = "/end?outcome=" + btoa(outcome) + "&board=" + btoa(board);
    }

    triggerDraw() {
        this.redirectToEnd("draw");
    }

    triggerWin() {
        this.redirectToEnd("win!");
    }

    triggerLose() {
        this.redirectToEnd("lose :(");
    }
}
