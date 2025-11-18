# 7.py

SCALE_DATA = {
    "d7": [
        {"notes": ("D", "F#", "A", "C")},
        {"scales": [

            # --- Standard pentatonics ---
            {
                "scale": "a minor 6",
                "notes": ("A", "C", "D", "E", "F#"),
                "tensions": ("5", "b7", "r", "9", "3"),
                "order": 10
            },

            {
                "scale": "e minor",
                "notes": ("E", "G", "A", "B", "D"),
                "tensions": ("9", "11", "5", "13", "r"),
                "order": 20
            },

            {
                "scale": "b minor",
                "notes": ("B", "D", "E", "F#", "A"),
                "tensions": ("13", "r", "9", "3", "5"),
                "order": 30
            },

            {
                "scale": "f# minor 7b5",
                "notes": ("F#", "A", "B", "C", "E"),
                "tensions": ("3", "5", "13", "b7", "9"),
                "order": 40
            },

            {
                "scale": "f minor",
                "notes": ("F", "Ab", "Bb", "C", "Eb"),
                "tensions": ("#9", "b5", "#5", "b7", "b9"),
                "order": 50
            },

            {
                "scale": "d major b2",
                "notes": ("D", "Eb", "F#", "A", "B"),
                "tensions": ("r", "b9", "3", "5", "13"),
                "order": 60
            },

            {
                "scale": "f major b2",
                "notes": ("F", "Gb", "A", "C", "D"),
                "tensions": ("#9", "3", "5", "b7", "r"),
                "order": 70
            },

            {
                "scale": "a major b2",
                "notes": ("A", "Bb", "C#", "E", "F#"),
                "tensions": ("13", "b7", "b9", "3", "#11"),
                "order": 80
            },

            {
                "scale": "c# major b2",
                "notes": ("C#", "D", "E#", "G#", "A#"),
                "tensions": ("7", "b9", "3", "5", "13"),
                "order": 90
            },

            # --- Added pentatonics ---
            {
                "scale": "coltrane pentatonic",
                "notes": ("D", "E", "F#", "A#", "C"),
                "tensions": ("r", "9", "3", "#5", "b7"),
                "order": 100
            },

            {
                "scale": "mccoy pentatonic",
                "notes": ("D", "E", "G", "A", "B"),
                "tensions": ("r", "9", "11", "5", "13"),
                "order": 110
            },

            {
                "scale": "hexatonic altered dominant pentatonic",
                "notes": ("D", "Eb", "F#", "G#", "B"),
                "tensions": ("r", "b9", "3", "#11", "13"),
                "order": 120
            },

            {
                "scale": "altered pentatonic",
                "notes": ("D", "F", "G#", "B", "C"),
                "tensions": ("r", "b3/#9", "b5", "13", "b7"),
                "order": 130
            },

        ]}
    ]
}
