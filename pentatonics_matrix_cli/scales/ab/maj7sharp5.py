# maj7sharp5.py — Ab key center

SCALE_DATA = {
    "abmaj7#5": [
        {"notes": ("Ab", "C", "E", "G")},
        {"scales": [

            {"scale": "E major b6",
             "notes": ("Ab", "C", "D", "E", "G"),
             "tensions": ("r", "3", "#11", "#5", "7"),
             "order": 10},

            {"scale": "B minor 6",
             "notes": ("B", "D", "E", "F#", "G"),
             "tensions": ("7", "9", "3", "#11", "#5"),
             "order": 20},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("Ab", "Bb", "C", "E", "F"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("Ab", "Bb", "Db", "Eb", "F"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("Ab", "A", "C", "E", "F"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("Ab", "Bb", "C", "Eb", "F#"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
