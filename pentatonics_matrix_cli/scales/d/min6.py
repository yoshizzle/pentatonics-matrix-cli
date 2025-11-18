# min6.py

SCALE_DATA = {
    "dmin6": [
        {"notes": ("D", "F", "A", "B")},
        {"scales": [

            # --- Standard pentatonics ---
            {
                "scale": "d minor 6",
                "notes": ("D", "F", "G", "A", "B"),
                "tensions": ("r", "b3", "11", "5", "13"),
                "order": 10
            },

            {
                "scale": "b minor 7b5",
                "notes": ("B", "D", "E", "F", "A"),
                "tensions": ("13", "r", "9", "b3", "5"),
                "order": 20
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
