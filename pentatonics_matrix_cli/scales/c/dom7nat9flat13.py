# dom7nat9flat13.py

SCALE_DATA = {
    "c7nat9b13": [
        {"notes": ("C", "E", "G", "Bb", "D", "Ab")},
        {"scales": [
            {"scale": "e whole tone", "notes": ("E", "G#", "A#", "B#", "D"),
             "tensions": ("3", "b13", "b7", "r", "9"), "order": 10},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("C", "D", "E", "G#", "A#"),
             "tensions": ("r", "9", "3", "#5", "7"), "order": 100},

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
