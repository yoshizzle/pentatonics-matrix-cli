# min7.py

SCALE_DATA = {
    "dmin7": [
        {"notes": ("D", "F", "A", "C")},
        {"scales": [

            # --- Standard pentatonics ---
            {
                "scale": "d minor",
                "notes": ("D", "F", "G", "A", "C"),
                "tensions": ("r", "b3", "11", "5", "b7"),
                "order": 10
            },

            {
                "scale": "a minor",
                "notes": ("A", "C", "D", "E", "G"),
                "tensions": ("5", "b7", "r", "9", "11"),
                "order": 20
            },

            {
                "scale": "e minor",
                "notes": ("E", "G", "A", "B", "D"),
                "tensions": ("9", "11", "5", "13", "r"),
                "order": 30
            },

            {
                "scale": "c minor",
                "notes": ("C", "Eb", "F", "G", "Bb"),
                "tensions": ("b7", "b9", "11", "5", "13"),
                "order": 40
            },

            # --- Added pentatonics ---
            {
                "scale": "coltrane pentatonic",
                "notes": ("D", "E", "F#", "A#", "C"),
                "tensions": ("r", "9", "3", "#5", "7"),
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
