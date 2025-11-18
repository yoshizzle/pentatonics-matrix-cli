# dom7.py

SCALE_DATA = {
    "c7": [
        {"notes": ("C", "E", "G", "Bb")},
        {"scales": [
            {"scale": "g minor 6", "notes": ("G", "Bb", "C", "D", "E"),
             "tensions": ("5", "b7", "r", "9", "3"), "order": 10},

            {"scale": "d minor", "notes": ("D", "F", "G", "A", "C"),
             "tensions": ("9", "11", "5", "13", "r"), "order": 20},

            {"scale": "a minor", "notes": ("A", "C", "D", "E", "G"),
             "tensions": ("13", "r", "9", "3", "5"), "order": 30},

            {"scale": "e minor 7b5", "notes": ("E", "G", "A", "Bb", "D"),
             "tensions": ("3", "5", "13", "b7", "9"), "order": 40},

            {"scale": "eb minor", "notes": ("Eb", "Gb", "Ab", "Bb", "Db"),
             "tensions": ("#9", "b5", "#5", "b7", "b9"), "order": 50},

            {"scale": "c major b2", "notes": ("C", "Db", "E", "G", "A"),
             "tensions": ("r", "b9", "3", "5", "13"), "order": 60},

            {"scale": "eb major b2", "notes": ("Eb", "Fb", "G", "Bb", "C"),
             "tensions": ("#9", "3", "5", "b7", "r"), "order": 70},

            {"scale": "f# major b2", "notes": ("F#", "G", "A#", "C#", "D#"),
             "tensions": ("#11", "5", "b7", "b9", "#9"), "order": 80},

            {"scale": "a major b2", "notes": ("A", "Bb", "C#", "E", "F#"),
             "tensions": ("13", "b7", "b9", "3", "#11"), "order": 90},

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
