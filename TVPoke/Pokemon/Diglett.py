from TVPoke.BaseClasses.PokeTypes import Ground
from TVPoke.BaseClasses.Move import Move

class Diglett(Ground):
    def __init__(self):
        moves = [
            Move("Scratch", "NORMAL", 60),
            Move("Slash", "NORMAL", 80),
            Move("Earthquake", "GROUND", 100),
        ]
        super().__init__("Diglett", 140, moves, "./TVPoke/Pokemon/imgs/Diglett.png")