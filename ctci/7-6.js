

// Edge = A, A-,

class Edge {
    constructor(unfilled) {
        this.unfilled = unfilled
    }
}

class Piece {
    constructor(id, edges) {
        this.id = id
        this.edges = edges
    }
}

class CombinedPiece {
    constructor([pieces]) {
        this.piecees = pieces
        this.edges = pieces.reduce((piece) => piece.edges.filter(edge => edge.unfilled == true), _.union, [])
    }
}

const fitsWith = (pieceA, pieceB) => Math.random() > 0.5


// return graph showing which piece connected to which
const solvePuzzleNaively = (pieces) => {
    const queue = pieces
    
    const solution = {}

    const pieceInHand = queue.pop()
    while (queue.length != 0) {
        const somePiece = queue.pop()
        
        if (fitsWith(pieceInHand, somePiece)) {
            //  mark those things as fitting together
            solution[pieceInHand.id] = [...solution[pieceInHand.id], somePiece.id]
        }
    }

    return solutioon
}

// return graph showing which piece connected to which
const solvePuzzleGreedy = (pieces) => {
    const queue = pieces
    
    const solution = {}

    const pieceInHand = queue.pop()
    while (queue.length != 0) {
        const somePiece = queue.pop()
        
        if (fitsWith(pieceInHand, somePiece)) {
            //  mark those things as fitting together
            solution[pieceInHand.id] = [...solution[pieceInHand.id], somePiece.id]
        }
        
        const pieceInHand = new CombinedPiece([pieceInHand, somePiece])
    }

    return solutioon
}

const puzzle = [
    new Piece(1),
    new Piece(2),
    new Piece(3),
    new Piece(4),
]

solvePuzzleNaively(puzzle)