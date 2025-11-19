# alt.py — B key center

SCALE_DATA = {
    "b7alt": [
        {"notes": ("B", "D#", "F#", "G", "A", "A#", "C#")},
        {"scales": [

            {"scale": "B whole tone",
             "notes": ("B", "D#", "F##", "G##", "A##"),
             "tensions": ("r", "3", "#11", "#5", "b7"),
             "order": 10},

            {"scale": "F# major b6",
             "notes": ("E#", "G#", "A#", "B", "D#"),
             "tensions": ("3", "#5", "b7", "r", "#9"),
             "order": 20},

            {"scale": "B minor 6",
             "notes": ("B", "D", "E", "F#", "G#"),
             "tensions": ("#9", "b5", "#5", "b7", "r"),
             "order": 30},

            {"scale": "E minor",
             "notes": ("E", "G", "A", "B", "D"),
             "tensions": ("#9", "b5", "#5", "b7", "b9"),
             "order": 40},

            {"scale": "E minor 6",
             "notes": ("E", "G", "A", "B", "C#"),
             "tensions": ("#9", "b5", "#5", "b7", "r"),
             "order": 50},

            {"scale": "B minor 7b5",
             "notes": ("B", "D", "E", "F", "G#"),
             "tensions": ("b7", "b9", "#9", "b5", "#5"),
             "order": 60},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("B", "C#", "D#", "G", "A"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("B", "C#", "E", "F#", "G#"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("B", "C", "D#", "G", "A"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("B", "D", "F", "F#", "G#"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
