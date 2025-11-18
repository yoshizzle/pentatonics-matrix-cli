# min7flat5.py

SCALE_DATA = {
    "cmin7b5": [
        {"notes": ("C", "Eb", "Gb", "Bb")},
        {"scales": [
            {"scale": "eb minor 6", "notes": ("Eb", "Gb", "Ab", "Bb", "C"),
             "tensions": ("b3", "b5", "13", "b7", "r"), "order": 10},

            {"scale": "c minor 7b5", "notes": ("C", "Eb", "F", "Gb", "Bb"),
             "tensions": ("r", "b3", "11", "b5", "b7"), "order": 20},

            {"scale": "f minor", "notes": ("F", "Ab", "Bb", "C", "Eb"),
             "tensions": ("11", "13", "b7", "r", "b3"), "order": 30},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("C", "D", "Eb", "Gb", "A"),
             "tensions": ("r", "9", "b3", "b5", "13"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("C", "D", "F", "Gb", "Bb"),
             "tensions": ("r", "9", "11", "b5", "b7"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("C", "Db", "Eb", "Gb", "A"),
             "tensions": ("r", "b9", "b3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("C", "Eb", "Gb", "A", "Bb"),
             "tensions": ("r", "b3", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
