# min7b5nat9.py — Bb key center

SCALE_DATA = {
    "bbmin7b5nat9": [
        {"notes": ("Bb", "Db", "E", "Ab", "C")},
        {"scales": [

            {"scale": "C major b6",
             "notes": ("G", "Bb", "C", "D", "F"),
             "tensions": ("b5", "b7", "r", "9", "11"),
             "order": 10},

            # Added pentatonics
            {"scale": "coltrane pentatonic",
             "notes": ("Bb", "C", "D", "G#", "A#"),
             "tensions": ("r", "9", "3", "#5", "7"),
             "order": 100},

            {"scale": "mccoy pentatonic",
             "notes": ("Bb", "C", "Eb", "F", "G"),
             "tensions": ("r", "9", "11", "5", "13"),
             "order": 110},

            {"scale": "hexatonic altered dominant pentatonic",
             "notes": ("Bb", "B", "D", "F", "G"),
             "tensions": ("r", "b9", "3", "b5", "13"),
             "order": 120},

            {"scale": "altered pentatonic",
             "notes": ("Bb", "C#", "E", "F", "G#"),
             "tensions": ("r", "#9", "b5", "13", "b7"),
             "order": 130}
        ]}
    ]
}
