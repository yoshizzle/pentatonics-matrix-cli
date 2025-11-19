# dom7.py — Bb key center

SCALE_DATA = {
    "bb7": [
        {"notes": ("Bb", "D", "F", "Ab")},
        {"scales": [

            {"scale": "G minor 6",
             "notes": ("G", "Bb", "C", "D", "F"),
             "tensions": ("5", "b7", "r", "9", "3"),
             "order": 10},

            {"scale": "D minor",
             "notes": ("D", "F", "G", "A", "C"),
             "tensions": ("9", "11", "5", "13", "r"),
             "order": 20},

            {"scale": "A minor",
             "notes": ("A", "C", "D", "E", "G"),
             "tensions": ("13", "r", "9", "3", "5"),
             "order": 30},

            {"scale": "E minor 7b5",
             "notes": ("E", "G", "A", "Bb", "D"),
             "tensions": ("3", "5", "13", "b7", "9"),
             "order": 40},

            {"scale": "Eb minor",
             "notes": ("Eb", "Gb", "Ab", "Bb", "Db"),
             "tensions": ("#9", "b5", "#5", "b7", "b9"),
             "order": 50},

            {"scale": "C major b2",
             "notes": ("C", "Db", "E", "G", "A"),
             "tensions": ("r", "b9", "3", "5", "13"),
             "order": 60},

            {"scale": "Eb major b2",
             "notes": ("Eb", "Fb", "G", "Bb", "C"),
             "tensions": ("#9", "3", "5", "b7", "r"),
             "order": 70},

            {"scale": "F# major b2",
             "notes": ("F#", "G", "A#", "C#", "D#"),
             "tensions": ("#11", "5", "b7", "b9", "#9"),
             "order": 80},

            {"scale": "A major b2",
             "notes": ("A", "Bb", "C#", "E", "F#"),
             "tensions": ("13", "b7", "b9", "3", "#11"),
             "order": 90},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("Bb", "C", "D", "G#", "A#"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("Bb", "C", "Eb", "F", "G"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("Bb", "B", "D", "F", "G"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("Bb", "C#", "E", "F", "G#"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
