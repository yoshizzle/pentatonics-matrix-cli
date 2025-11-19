# dom7.py — B key center

SCALE_DATA = {
    "b7": [
        {"notes": ("B", "D#", "F#", "A")},
        {"scales": [

            {"scale": "G# minor 6",
             "notes": ("G#", "B", "C#", "D#", "F#"),
             "tensions": ("5", "b7", "r", "9", "3"),
             "order": 10},

            {"scale": "A# minor",
             "notes": ("A#", "C#", "D#", "E#", "G#"),
             "tensions": ("13", "r", "9", "3", "5"),
             "order": 20},

            {"scale": "E# minor 7b5",
             "notes": ("E#", "G#", "A#", "B", "D#"),
             "tensions": ("3", "5", "13", "b7", "9"),
             "order": 30},

            {"scale": "B major b2",
             "notes": ("B", "C", "D#", "F#", "G#"),
             "tensions": ("r", "b9", "3", "5", "13"),
             "order": 40},

            {"scale": "D# minor",
             "notes": ("D#", "F#", "G#", "A#", "C#"),
             "tensions": ("9", "11", "5", "13", "r"),
             "order": 50},

            {"scale": "E major b2",
             "notes": ("E", "F#", "G#", "B", "C#"),
             "tensions": ("#9", "3", "5", "b7", "r"),
             "order": 60},

            {"scale": "F## major b2",
             "notes": ("F##", "G#", "A#", "C#", "D#"),
             "tensions": ("#11", "5", "b7", "b9", "#9"),
             "order": 70},

            {"scale": "A# major b2",
             "notes": ("A#", "B", "C##", "E#", "F##"),
             "tensions": ("13", "b7", "b9", "3", "#11"),
             "order": 80},

            {"scale": "E minor",
             "notes": ("E", "G", "A", "B", "D"),
             "tensions": ("#9", "b5", "#5", "b7", "b9"),
             "order": 90},

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
