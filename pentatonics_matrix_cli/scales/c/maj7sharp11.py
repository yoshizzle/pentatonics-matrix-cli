# maj7sharp11.py

SCALE_DATA = {
    "cmaj7#11": [
        {"notes": ("C", "E", "G", "B", "F#")},
        {"scales": [
            {"scale": "a minor 6", "notes": ("A", "C", "D", "E", "F#"),
             "tensions": ("13", "r", "9", "3", "#11"), "order": 10},

            {"scale": "b minor", "notes": ("B", "D", "E", "F#", "A"),
             "tensions": ("7", "9", "3", "#11", "13"), "order": 20},

            {"scale": "f# whole tone", "notes": ("F#", "A#", "B#", "D", "E"),
             "tensions": ("#11", "7", "r", "9", "3"), "order": 30},

            # Added pentatonics
            {"scale": "coltrane pentatonic", "notes": ("C", "D", "E", "G#", "A#"),
             "tensions": ("r", "9", "3", "#5", "7"), "order": 100},

            {"scale": "mccoy pentatonic", "notes": ("C", "D", "F", "G", "A"),
             "tensions": ("r", "9", "11", "5", "13"), "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("C", "Db", "E", "Gb", "A"),
             "tensions": ("r", "b9", "3", "b5", "13"), "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("C", "Eb", "Gb", "A", "Bb"),
             "tensions": ("r", "#9", "b5", "13", "b7"), "order": 130}
        ]}
    ]
}
