# min7b5nat9.py — B key center

SCALE_DATA = {
    "bmin7b5nat9": [
        {"notes": ("B", "D", "F", "A", "C#")},
        {"scales": [

            {"scale": "E major b6",
             "notes": ("G#", "B", "C#", "D#", "F#"),
             "tensions": ("b5", "b7", "r", "9", "11"),
             "order": 10},

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
