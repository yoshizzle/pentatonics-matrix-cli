# dom7.py

SCALE_DATA = {
    "c#7": [
        {"notes": ("C#", "E#", "G#", "B")},
        {"scales": [

            {"scale": "g# minor 6",
             "notes": ("G#", "B", "C#", "D#", "E#"),
             "tensions": ("5", "b7", "r", "9", "3"),
             "order": 10},

            {"scale": "d# minor",
             "notes": ("D#", "F#", "G#", "A#", "C#"),
             "tensions": ("9", "11", "5", "13", "r"),
             "order": 20},

            {"scale": "a# minor",
             "notes": ("A#", "C#", "D#", "E#", "G#"),
             "tensions": ("13", "r", "9", "3", "5"),
             "order": 30},

            {"scale": "e# minor 7b5",
             "notes": ("E#", "G#", "A#", "B", "D#"),
             "tensions": ("3", "5", "13", "b7", "9"),
             "order": 40},

            {"scale": "d# minor b5 pentatonic",
             "notes": ("D#", "F#", "G#", "A#", "C#"),
             "tensions": ("#9", "b5", "#5", "b7", "b9"),
             "order": 50},

            {"scale": "c# major b2",
             "notes": ("C#", "D", "E#", "G#", "A#"),
             "tensions": ("r", "b9", "3", "5", "13"),
             "order": 60},

            {"scale": "e major b2",
             "notes": ("E", "F", "G#", "B", "C#"),
             "tensions": ("#9", "3", "5", "b7", "r"),
             "order": 70},

            {"scale": "fx major b2",
             "notes": ("Fx", "G#", "Ax", "Cx", "Dx"),
             "tensions": ("#11", "5", "b7", "b9", "#9"),
             "order": 80},

            {"scale": "a# major b2",
             "notes": ("A#", "B", "Cx", "E#", "Fx"),
             "tensions": ("13", "b7", "b9", "3", "#11"),
             "order": 90},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("C#", "D#", "E#", "Gx", "A#"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("C#", "D#", "F#", "G#", "A#"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("C#", "D", "E#", "G", "A#"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("C#", "E", "G", "A#", "B"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
