# dom7sharp11.py

SCALE_DATA = {
    "d7#11": [
        {"notes": ("D", "F#", "A", "C", "G#")},
        {"scales": [

            # --- Standard pentatonics ---
            {
                "scale": "a whole tone",
                "notes": ("A", "C#", "D#", "F", "G"),
                "tensions": ("5", "7", "b9", "#9", "11"),
                "order": 10
            },

            {
                "scale": "e major b6",
                "notes": ("C", "E", "F#", "G#", "A"),
                "tensions": ("b7", "9", "3", "#11", "5"),
                "order": 20
            },

            {
                "scale": "b minor 6",
                "notes": ("B", "D", "E", "F#", "G#"),
                "tensions": ("13", "r", "9", "3", "#11"),
                "order": 30
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
