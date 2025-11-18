# alt.py

SCALE_DATA = {
    "d7alt": [
        {"notes": ("D", "F#", "G", "G#", "A#", "C", "Eb")},  
        # Altered chord tones: 1, 3, b5, #5, b7, b9, #9
        {"scales": [

            # --- Standard pentatonics ---
            {
                "scale": "d whole tone",
                "notes": ("D", "F#", "G#", "A#", "C"),
                "tensions": ("r", "3", "#11", "#5", "b7"),
                "order": 10
            },

            {
                "scale": "a major b6",
                "notes": ("F", "A", "B", "C#", "E"),
                "tensions": ("3", "#5", "b7", "r", "#9"),
                "order": 20
            },

            {
                "scale": "e minor 6",
                "notes": ("E", "G", "A", "B", "C#"),
                "tensions": ("#9", "b5", "#5", "b7", "r"),
                "order": 30
            },

            {
                "scale": "d minor 6",
                "notes": ("D", "F", "G", "A", "B"),
                "tensions": ("r", "b3", "4", "5", "13"),
                "order": 40
            },

            {
                "scale": "f minor",
                "notes": ("F", "Ab", "Bb", "C", "Eb"),
                "tensions": ("b3", "b5", "b7", "r", "b9/#9"),
                "order": 50
            },

            {
                "scale": "b minor 7b5",
                "notes": ("B", "D", "E", "F", "A"),
                "tensions": ("b7", "r", "9", "b3", "5"),
                "order": 60
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
