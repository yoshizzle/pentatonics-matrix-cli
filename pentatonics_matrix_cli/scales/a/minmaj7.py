# minmaj7.py — A key center

SCALE_DATA = {
    "aminmaj7": [
        {"notes": ("A", "C", "E", "G#")},
        {"scales": [

            {"scale": "E major b6",
             "notes": ("C", "E", "F#", "G#", "B"),
             "tensions": ("b3", "5", "13", "7", "9"),
             "order": 10},

            {"scale": "B whole tone",
             "notes": ("B", "E", "F#", "G#", "A#"),
             "tensions": ("7", "b3", "11", "5", "13"),
             "order": 20},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("A", "B", "C#", "F", "G"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("A", "B", "D", "E", "F#"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("A", "Bb", "C#", "F", "G"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("A", "C", "Eb", "F#", "G#"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
