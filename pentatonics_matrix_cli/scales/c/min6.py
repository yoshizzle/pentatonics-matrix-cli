# min6.py

SCALE_DATA = {
    "cmin6": [
        {"notes": ("C", "Eb", "G", "A")},
        {"scales": [
            {"scale": "c minor 6", "notes": ("C", "Eb", "F", "G", "A"),
             "tensions": ("r", "b3", "11", "5", "13"), "order": 10},

            {"scale": "a minor 7b5", "notes": ("A", "C", "D", "Eb", "G"),
             "tensions": ("13", "r", "9", "b3", "5"), "order": 20},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("C", "D", "Eb", "G", "A"),
             "tensions": ("r", "9", "b3", "5", "13"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("C", "D", "F", "G", "A"),
             "tensions": ("r", "9", "11", "5", "13"),
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
