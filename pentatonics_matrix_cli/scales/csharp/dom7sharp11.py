# dom7sharp11.py

SCALE_DATA = {
    "c#7#11": [
        {"notes": ("C#", "E#", "G#", "B", "Fx")},
        {"scales": [

            {"scale": "g# whole tone",
             "notes": ("G#", "B", "C#", "D#", "E#"),
             "tensions": ("5", "b7", "r", "9", "3"),
             "order": 10},

            {"scale": "d# major b6",
             "notes": ("B", "D#", "E#", "Fx", "G#"),
             "tensions": ("b7", "9", "3", "#11", "5"),
             "order": 20},

            {"scale": "a# minor 6",
             "notes": ("A#", "C#", "D#", "E#", "Fx"),
             "tensions": ("13", "r", "9", "3", "#11"),
             "order": 30},

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
