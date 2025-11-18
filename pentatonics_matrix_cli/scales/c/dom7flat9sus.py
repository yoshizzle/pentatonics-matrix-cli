# dom7flat9sus.py

SCALE_DATA = {
    "c7b9sus": [
        {"notes": ("C", "F", "G", "Bb", "Db")},
        {"scales": [
            {"scale": "bb minor 6", "notes": ("Bb", "Db", "Eb", "F", "A"),
             "tensions": ("b7", "b9", "#9", "11", "13"), "order": 20},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("C", "D", "Eb", "G", "A"),
             "tensions": ("r", "9", "b3", "5", "13"), "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("C", "D", "F", "G", "A"),
             "tensions": ("r", "9", "11", "5", "13"), "order": 110},

            {"scale": "altered dominant pentatonic",
             "notes": ("C", "Db", "E", "Gb", "Bb"),
             "tensions": ("r", "b9", "3", "b5", "b7"), "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("C", "Eb", "Gb", "A", "Bb"),
             "tensions": ("r", "#9", "b5", "13", "b7"), "order": 130}
        ]}
    ]
}
