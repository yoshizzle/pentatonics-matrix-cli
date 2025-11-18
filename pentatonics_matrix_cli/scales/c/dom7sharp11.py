# dom7sharp11.py

SCALE_DATA = {
    "c7#11": [
        {"notes": ("C", "E", "G", "Bb", "F#")},
        {"scales": [
            {"scale": "g whole tone", "notes": ("G", "Bb", "C", "D", "E"),
             "tensions": ("5", "b7", "r", "9", "3"), "order": 10},

            {"scale": "d major b6", "notes": ("Bb", "D", "E", "F#", "G"),
             "tensions": ("b7", "9", "3", "#11", "5"), "order": 20},

            {"scale": "a minor 6", "notes": ("A", "C", "D", "E", "F#"),
             "tensions": ("13", "r", "9", "3", "#11"), "order": 30},

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
