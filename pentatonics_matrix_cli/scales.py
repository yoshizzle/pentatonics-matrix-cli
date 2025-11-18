scales = {
    # C
    "CMaj7": [
        {"notes": ("C","E","G","B")},
        {"scales": [
            {"scale": "A minor", "notes": ("A","C","E","F","G"), "tensions": ("13","R","3","11","5"), "order": 10},
            {"scale": "E minor", "notes": ("E","G","A","B","D"), "tensions": ("3","5","13","7","9"), "order": 20},
            {"scale": "B minor", "notes": ("B","D","E","F#","A"), "tensions": ("7","9","3","#11","13"), "order": 30},
        ]},
    ],

    "CMaj7#11": [
        {"notes": ("C","E","G","B","F#")},
        {"scales": [
            {"scale": "A minor 6", "notes": ("A","C","D","E","F#"), "tensions": ("13","R","9","3","#11"), "order": 10},
            {"scale": "B minor", "notes": ("B","D","E","F#","A"), "tensions": ("7","9","3","#11","13"), "order": 20},
            {"scale": "F# Whole Tone", "notes": ("F#","A#","B#","D","E"), "tensions": ("#11","7","R","9","3"), "order": 30},
        ]},
    ],

    "CMaj7#5": [
        {"notes": ("C","E","G#","B")},
        {"scales": [
            {"scale": "E Major b6", "notes": ("C","E","F#","G#","B"), "tensions": ("R","3","#11","#5","7"), "order": 10},
            {"scale": "B minor 6", "notes": ("B","D","E","F#","G#"), "tensions": ("7","9","3","#11","#5"), "order": 20},
        ]},
    ],

    "CMaj7b5": [
        {"notes": ("C","E","Gb","B")},
        {"scales": [
            # Corrected from (Gb, Bbb, Cb, Dbb, Fb)
            {"scale": "Gb minor 7b5", "notes": ("Gb","A","Cb","Dbb","Fb"), "tensions": ("b5","13","7","R","3"), "order": 10},
        ]},
    ],

    "Cmin7": [
        {"notes": ("C","Eb","G","Bb")},
        {"scales": [
            {"scale": "C minor", "notes": ("C","Eb","F","G","Bb"), "tensions": ("R","b3","11","5","b7"), "order": 10},
            {"scale": "G minor", "notes": ("G","Bb","C","D","F"), "tensions": ("5","b7","R","9","11"), "order": 20},
            {"scale": "D minor", "notes": ("D","F","G","A","C"), "tensions": ("9","11","5","13","R"), "order": 30},
            {"scale": "Bb minor", "notes": ("Bb","Db","Eb","F","Ab"), "tensions": ("b7","b9","b3","11","13"), "order": 40},
        ]},
    ],

    "Cmin6": [
        {"notes": ("C","Eb","G","A")},
        {"scales": [
            {"scale": "C minor 6", "notes": ("C","Eb","F","G","A"), "tensions": ("R","b3","11","5","13"), "order": 10},
            {"scale": "A minor 7b5", "notes": ("A","C","D","Eb","G"), "tensions": ("13","R","9","b3","5"), "order": 20},
        ]},
    ],

    "Cmin/Maj7": [
        {"notes": ("C","Eb","G","B")},
        {"scales": [
            {"scale": "G Major b6", "notes": ("Eb","G","A","B","D"), "tensions": ("b3","5","13","7","9"), "order": 10},
            {"scale": "B Whole Tone", "notes": ("B","Eb","F","G","A"), "tensions": ("7","b3","11","5","13"), "order": 20},
        ]},
    ],

    "Cmin7b5": [
        {"notes": ("C","Eb","Gb","Bb")},
        {"scales": [
            {"scale": "Eb minor 6", "notes": ("Eb","Gb","Ab","Bb","C"), "tensions": ("b3","b5","13","b7","R"), "order": 10},
            {"scale": "C minor 7b5", "notes": ("C","Eb","F","Gb","Bb"), "tensions": ("R","b3","11","b5","b7"), "order": 20},
            {"scale": "F minor", "notes": ("F","Ab","Bb","C","Eb"), "tensions": ("11","13","b7","R","b3"), "order": 30},
        ]},
    ],

    "Cmin7b5nat9": [
        {"notes": ("C","Eb","Gb","Bb","D")},
        {"scales": [
            {"scale": "Bb Major b6", "notes": ("G","Bb","C","D","F"), "tensions": ("b5","b7","R","9","11"), "order": 10},
        ]},
    ],

    "C7": [
        {"notes": ("C","E","G","Bb")},
        {"scales": [
            {"scale": "G minor 6", "notes": ("G","Bb","C","D","E"), "tensions": ("5","b7","R","9","3"), "order": 10},
            {"scale": "D minor", "notes": ("D","F","G","A","C"), "tensions": ("9","11","5","13","R"), "order": 20},
            {"scale": "A minor", "notes": ("A","C","D","E","G"), "tensions": ("13","R","9","3","5"), "order": 30},
            {"scale": "E minor 7b5", "notes": ("E","G","A","Bb","D"), "tensions": ("3","5","13","b7","9"), "order": 40},
            {"scale": "Eb minor", "notes": ("Eb","Gb","Ab","Bb","Db"), "tensions": ("#9","b5","#5","b7","b9"), "order": 50},
            {"scale": "C Major b2", "notes": ("C","Db","E","G","A"), "tensions": ("R","b9","3","5","13"), "order": 60},
            {"scale": "Eb Major b2", "notes": ("Eb","Fb","G","Bb","C"), "tensions": ("#9","3","5","b7","R"), "order": 70},
            {"scale": "F# Major b2", "notes": ("F#","G","A#","C#","D#"), "tensions": ("#11","5","b7","b9","#9"), "order": 80},
            {"scale": "A Major b2", "notes": ("A","Bb","C#","E","F#"), "tensions": ("13","b7","b9","3","#11"), "order": 90},
        ]},
    ],

    "C7#11": [
        {"notes": ("C","E","G","Bb","F#")},
        {"scales": [
            {"scale": "G Whole Tone", "notes": ("G","Bb","C","D","E"), "tensions": ("5","b7","R","9","3"), "order": 10},
            {"scale": "D Major b6", "notes": ("Bb","D","E","F#","G"), "tensions": ("b7","9","3","#11","5"), "order": 20},
            {"scale": "A minor 6", "notes": ("A","C","D","E","F#"), "tensions": ("13","R","9","3","#11"), "order": 30},
        ]},
    ],

    "C7b9sus": [
        {"notes": ("C","F","G","Bb","Db")},
        {"scales": [
            {"scale": "Bb minor 6", "notes": ("Bb","Db","Eb","F","A"), "tensions": ("b7","b9","#9","11","13"), "order": 20},
        ]},
    ],

    "C7nat9b13": [
        {"notes": ("C","E","G","Bb","D","Ab")},
        {"scales": [
            {"scale": "E Whole Tone", "notes": ("E","G#","A#","B#","D"), "tensions": ("3","b13","b7","R","9"), "order": 10},
        ]},
    ],

    "C7alt": [
        # Corrected chord tones (consistent #9 = Eb, not D#)
        {"notes": ("C","E","Gb","G#","Bb","Db","Eb")},
        {"scales": [
            {"scale": "C Whole Tone", "notes": ("C","E","F#","G#","A#"), "tensions": ("R","3","#11","#5","b7"), "order": 10},
            {"scale": "Ab Major b6", "notes": ("Fb","Ab","Bb","C","Eb"), "tensions": ("3","#5","b7","R","#9"), "order": 20},
            {"scale": "Db minor 6", "notes": ("Db","Fb","Gb","Ab","Bb"), "tensions": ("b9","3","b5","#5","7"), "order": 30},
            {"scale": "Eb minor", "notes": ("Eb","Gb","Ab","Bb","Db"), "tensions": ("#9","b5","#5","b7","b9"), "order": 40},
            {"scale": "Eb minor 6", "notes": ("Eb","Gb","Ab","Bb","C"), "tensions": ("#9","b5","#5","b7","R"), "order": 50},
            {"scale": "Bb minor 7b5", "notes": ("Bb","Db","Eb","Fb","Ab"), "tensions": ("b7","b9","#9","b5","#5"), "order": 60},
        ]},
    ],

    # C#
    "C#Maj7": [
        {"notes": ("C#","E#","G#","B#")},
        {"scales": [
            {"scale": "A# minor", "notes": ("A#","C#","E#","F#","G#"), 
             "tensions": ("13","R","3","11","5"), "order": 10},

            {"scale": "E# minor", "notes": ("E#","G#","A#","B#","D#"), 
             "tensions": ("3","5","13","7","9"), "order": 20},

            {"scale": "B# minor", "notes": ("B#","D#","E#","Fx","A#"), 
             "tensions": ("7","9","3","#11","13"), "order": 30},
        ]},
    ],

    "C#Maj7#11": [
        {"notes": ("C#","E#","G#","B#","Fx")},
        {"scales": [
            {"scale": "A# minor 6", 
             "notes": ("A#","C#","D#","E#","Fx"),
             "tensions": ("13","R","9","3","#11"), "order": 10},

            {"scale": "B# minor", 
             "notes": ("B#","D#","E#","Fx","A#"),
             "tensions": ("7","9","3","#11","13"), "order": 20},

            {"scale": "Fx Whole Tone", 
             "notes": ("Fx","Ax","Bx","D#","E#"),
             "tensions": ("#11","7","R","9","3"), "order": 30},
        ]},
    ],

    "C#Maj7#5": [
        {"notes": ("C#","E#","Gx","B#")},
        {"scales": [
            {"scale": "E# Major b6", 
             "notes": ("C#","E#","Fx","Gx","B#"), 
             "tensions": ("R","3","#11","#5","7"), "order": 10},

            {"scale": "B# minor 6", 
             "notes": ("B#","D#","E#","Fx","Gx"),
             "tensions": ("7","9","3","#11","#5"), "order": 20},
        ]},
    ],

    "C#Maj7b5": [
        {"notes": ("C#","E#","G","B#")},
        {"scales": [
            # Corrected enharmonic spelling (G–Bb–C–Db–F)
            # Original had unnecessary double-flats
            {"scale": "G minor 7b5", 
             "notes": ("G","Bb","C","Db","F"),
             "tensions": ("b5","13","7","R","3"), "order": 10},
        ]},
    ],

    "C#min7": [
        {"notes": ("C#","E","G#","B")},
        {"scales": [
            {"scale": "C# minor", 
             "notes": ("C#","E","F#","G#","B"),
             "tensions": ("R","b3","11","5","b7"), "order": 10},

            {"scale": "G# minor", 
             "notes": ("G#","B","C#","D#","F#"),
             "tensions": ("5","b7","R","9","11"), "order": 20},

            {"scale": "D# minor", 
             "notes": ("D#","F#","G#","A#","C#"),
             "tensions": ("9","11","5","13","R"), "order": 30},

            {"scale": "B minor", 
             "notes": ("B","D","E","F#","A"),
             "tensions": ("b7","b9","3","11","13"), "order": 40},
        ]},
    ],

    "C#min6": [
        {"notes": ("C#","E","G#","A#")},
        {"scales": [
            {"scale": "C# minor 6", 
             "notes": ("C#","E","F#","G#","A#"),
             "tensions": ("R","b3","11","5","13"), "order": 10},

            {"scale": "A# minor 7b5",
             "notes": ("A#","C#","D#","E","G#"),
             "tensions": ("13","R","9","b3","5"), "order": 20},
        ]},
    ],

    "C#min/Maj7": [
        {"notes": ("C#","E","G#","B#")},
        {"scales": [
            {"scale": "G# Major b6", 
             "notes": ("E","G#","A#","B#","D#"),
             "tensions": ("3","5","13","7","9"), "order": 10},

            {"scale": "B# Whole Tone", 
             "notes": ("B#","E","F#","G#","A#"),
             "tensions": ("7","b3","11","5","13"), "order": 20},
        ]},
    ],

    "C#min7b5": [
        {"notes": ("C#","E","G","B")},
        {"scales": [
            {"scale": "F# minor", 
             "notes": ("F#","A","B","C#","E"),
             "tensions": ("11","13","b7","R","3"), "order": 10},

            {"scale": "E minor 6", 
             "notes": ("E","G","A","B","C#"),
             "tensions": ("3","b5","13","b7","R"), "order": 20},

            {"scale": "C# minor 7b5",
             "notes": ("C#","E","F#","G","B"),
             "tensions": ("R","b3","11","5","b7"), "order": 30},
        ]},
    ],

    "C#min7b5nat9": [
        {"notes": ("C#","E","G","B","D#")},
        {"scales": [
            {"scale": "B Major b6", 
             "notes": ("G#","B","C#","D#","F#"),
             "tensions": ("b5","b7","R","9","11"), "order": 10},
        ]},
    ],

    # C# DOMINANTS
    "C#7": [
        {"notes": ("C#","E#","G#","B")},
        {"scales": [
            {"scale": "G# minor 6",
             "notes": ("G#","B","C#","D#","E#"),
             "tensions": ("5","b7","R","9","3"), "order": 10},

            {"scale": "A# minor",
             "notes": ("A#","C#","D#","E#","G#"),
             "tensions": ("13","R","9","3","5"), "order": 20},

            {"scale": "E# minor 7b5",
             "notes": ("E#","G#","A#","B","D#"),
             "tensions": ("3","5","13","b7","9"), "order": 30},

            {"scale": "C# Major b2",
             "notes": ("C#","D","E#","G#","A#"),
             "tensions": ("R","b9","3","5","13"), "order": 40},

            {"scale": "D# minor",
             "notes": ("D#","F#","G#","A#","C#"),
             "tensions": ("9","11","5","13","R"), "order": 50},

            {"scale": "E Major b2",
             "notes": ("E","F","G#","B","C#"),
             "tensions": ("#9","3","5","b7","R"), "order": 60},

            {"scale": "Fx Major b2",
             "notes": ("Fx","G#","Ax","Cx","Dx"),
             "tensions": ("#11","5","b7","b9","#9"), "order": 70},

            {"scale": "A# Major b2",
             "notes": ("A#","B","Cx","E#","Fx"),
             "tensions": ("13","b7","b9","3","#11"), "order": 80},

            {"scale": "E minor",
             "notes": ("E","G","A","B","D"),
             "tensions": ("#9","b5","#5","b7","b9"), "order": 90},
        ]},
    ],

    "C#7#11": [
        {"notes": ("C#","E#","G#","B","Fx")},
        {"scales": [
            {"scale": "G# Whole Tone",
             "notes": ("G#","B","C#","D#","E#"),
             "tensions": ("5","b7","R","9","3"), "order": 10},

            {"scale": "D# Major b6",
             "notes": ("B","D#","E#","Fx","G#"),
             "tensions": ("b7","9","3","#11","5"), "order": 20},

            {"scale": "A# minor 6",
             "notes": ("A#","C#","D#","E#","Fx"),
             "tensions": ("13","R","9","3","#11"), "order": 30},
        ]},
    ],

    "C#7b9sus": [
        {"notes": ("C#","F#","G#","B","D")},
        {"scales": [
            {"scale": "B minor 6",
             "notes": ("B","D","E","F#","A#"),
             "tensions": ("b7","b9","#9","11","13"), "order": 20},
        ]},
    ],

    "C#7nat9b13": [
        {"notes": ("C#","E#","G#","B","D#","A")},
        {"scales": [
            {"scale": "E# Whole Tone",
             "notes": ("E#","Gx","Ax","Bx","D#"),
             "tensions": ("3","b13","b7","R","9"), "order": 10},
        ]},
    ],

    "C#7alt": [
        {"notes": ("C#","E#","G","G#","B","D","Eb")},
        {"scales": [
            {"scale": "C# Whole Tone",
             "notes": ("C#","E#","Fx","Gx","Ax"),
             "tensions": ("R","3","#11","#5","b7"), "order": 10},

            {"scale": "A Major b6",
             "notes": ("F","A","B","C#","E"),
             "tensions": ("3","#5","b7","R","#9"), "order": 20},

            {"scale": "E minor 6",
             "notes": ("E","G","A","B","C#"),
             "tensions": ("#9","b5","#5","b7","R"), "order": 30},

            {"scale": "D minor 6",
             "notes": ("D","F","G","A","B"),
             "tensions": ("b9","3","b5","#5","b7"), "order": 40},

            {"scale": "E minor",
             "notes": ("E","G","A","B","D"),
             "tensions": ("#9","b5","#5","b7","b9"), "order": 50},

            {"scale": "B minor 7b5",
             "notes": ("B","D","E","F","A"),
             "tensions": ("b7","b9","#9","b5","#5"), "order": 60},
        ]},
    ],

    # D
    "DMaj7": [
        {"notes": ("D","F#","A","C#")},
        {"scales": [
            {"scale": "B minor",
             "notes": ("B","D","F#","G","A"),
             "tensions": ("13","R","3","11","5"), "order": 10},

            {"scale": "F# minor",
             "notes": ("F#","A","B","C#","E"),
             "tensions": ("3","5","13","7","9"), "order": 20},

            {"scale": "C# minor",
             "notes": ("C#","E","F#","G#","B"),
             "tensions": ("7","9","3","#11","13"), "order": 30},
        ]},
    ],

    "DMaj7#11": [
        {"notes": ("D","F#","A","C#","G#")},
        {"scales": [
            {"scale": "B minor 6",
             "notes": ("B","D","E","F#","G#"),
             "tensions": ("13","R","9","3","#11"), "order": 10},

            {"scale": "C# minor",
             "notes": ("C#","E","F#","G#","B"),
             "tensions": ("7","9","3","#11","13"), "order": 20},

            {"scale": "G# Whole Tone",
             "notes": ("G#","B#","C#","E","F#"),
             "tensions": ("#11","7","R","9","3"), "order": 30},
        ]},
    ],

    "DMaj7#5": [
        {"notes": ("D","F#","A#","C#")},
        {"scales": [
            {"scale": "F# Major b6",
             "notes": ("D","F#","G#","A#","C#"),
             "tensions": ("R","3","#11","#5","7"), "order": 10},

            {"scale": "C# minor 6",
             "notes": ("C#","E","F#","G#","A#"),
             "tensions": ("7","9","3","#11","#5"), "order": 20},
        ]},
    ],

    "DMaj7b5": [
        {"notes": ("D","F#","Ab","C#")},
        {"scales": [
            {"scale": "Ab minor 7b5",
             "notes": ("Ab","Cb","Dbb","Ebb","Gb"),
             "tensions": ("b5","13","7","R","3"), "order": 10},
        ]},
    ],

    "Dmin7": [
        {"notes": ("D","F","A","C")},
        {"scales": [
            {"scale": "D minor",
             "notes": ("D","F","G","A","C"),
             "tensions": ("R","b3","11","5","b7"), "order": 10},

            {"scale": "A minor",
             "notes": ("A","C","D","E","G"),
             "tensions": ("5","b7","R","9","11"), "order": 20},

            {"scale": "E minor",
             "notes": ("E","G","A","B","D"),
             "tensions": ("9","11","5","13","R"), "order": 30},

            {"scale": "C minor",
             "notes": ("C","Eb","F","G","Bb"),
             "tensions": ("b7","b9","b3","11","13"), "order": 40},
        ]},
    ],

    "Dmin6": [
        {"notes": ("D","F","A","B")},
        {"scales": [
            {"scale": "D minor 6",
             "notes": ("D","F","G","A","B"),
             "tensions": ("R","b3","11","5","13"), "order": 10},

            {"scale": "B minor 7b5",
             "notes": ("B","D","E","F","A"),
             "tensions": ("13","R","9","b3","5"), "order": 20},
        ]},
    ],

    "Dmin/Maj7": [
        {"notes": ("D","F","A","C#")},
        {"scales": [
            {"scale": "A Major b6",
             "notes": ("F","A","B","C#","E"),
             "tensions": ("b3","5","13","7","9"), "order": 10},

            {"scale": "C Whole Tone",
             "notes": ("C#","F","G","A","B"),
             "tensions": ("7","b3","11","5","13"), "order": 20},
        ]},
    ],

    "Dmin7b5": [
        {"notes": ("D","F","Ab","C")},
        {"scales": [
            {"scale": "F minor 6",
             "notes": ("F","Ab","Bb","C","D"),
             "tensions": ("b3","b5","13","b7","R"), "order": 10},

            {"scale": "D minor 7b5",
             "notes": ("D","F","G","Ab","C"),
             "tensions": ("R","b3","11","b5","b7"), "order": 20},

            {"scale": "G minor",
             "notes": ("G","Bb","C","D","F"),
             "tensions": ("11","13","b7","R","b3"), "order": 30},
        ]},
    ],

    "Dmin7b5nat9": [
        {"notes": ("D","F","Ab","C","E")},
        {"scales": [
            {"scale": "C Major b6",
             "notes": ("A","C","D","E","G"),
             "tensions": ("5","b7","R","9","11"), "order": 10},
        ]},
    ],

    "D7": [
        {"notes": ("D","F#","A","C")},
        {"scales": [
            {"scale": "A minor 6",
             "notes": ("A","C","D","E","F#"),
             "tensions": ("5","b7","R","9","3"), "order": 10},

            {"scale": "E minor",
             "notes": ("E","G","A","B","D"),
             "tensions": ("9","11","5","13","R"), "order": 20},

            {"scale": "B minor",
             "notes": ("B","D","E","F#","A"),
             "tensions": ("13","R","9","3","5"), "order": 30},

            {"scale": "F# minor 7b5",
             "notes": ("F#","A","B","C","E"),
             "tensions": ("3","5","13","b7","9"), "order": 40},

            {"scale": "E# minor",
             "notes": ("E#","Ab","Bb","C","Eb"),
             "tensions": ("#9","b5","#5","b7","b9"), "order": 50},

            {"scale": "D Major b2",
             "notes": ("D","Eb","F#","A","B"),
             "tensions": ("R","b9","3","5","13"), "order": 60},

            {"scale": "F Major b2",
             "notes": ("F","Gb","A","C","D"),
             "tensions": ("#9","3","5","b7","R"), "order": 70},

            {"scale": "G# Major b2",
             "notes": ("G#","A","B#","D#","E#"),
             "tensions": ("#11","5","b7","b9","#9"), "order": 80},

            {"scale": "B Major b2",
             "notes": ("B","C","D#","F#","G#"),
             "tensions": ("13","b7","b9","3","#11"), "order": 90},
        ]},
    ],

    "D7#11": [
        {"notes": ("D","F#","A","C","G#")},
        {"scales": [
            {"scale": "A Whole Tone",
             "notes": ("A","C","D","E","F#"),
             "tensions": ("5","b7","R","9","3"), "order": 10},

            {"scale": "E Major b6",
             "notes": ("C","E","F#","G#","A"),
             "tensions": ("b7","9","3","#11","5"), "order": 20},

            {"scale": "B minor 6",
             "notes": ("B","D","E","F#","G#"),
             "tensions": ("13","R","9","3","#11"), "order": 30},
        ]},
    ],

    "D7b9sus": [
        {"notes": ("D","G","A","C","Eb")},
        {"scales": [
            {"scale": "C minor 6",
             "notes": ("C","Eb","F","G","A"),
             "tensions": ("b7","b9","#9","11","13"), "order": 20},
        ]},
    ],

    "D7nat9b13": [
        {"notes": ("D","F#","A","C","E","Bb")},
        {"scales": [
            {"scale": "F# Whole Tone",
             "notes": ("F#","A#","B#","C#","E"),
             "tensions": ("3","b13","b7","R","9"), "order": 10},
        ]},
    ],

    "D7alt": [
        {"notes": ("D","F#","Ab","A#","C","Eb","E#")},
        {"scales": [
            {"scale": "D Whole Tone",
             "notes": ("D","F#","G#","A#","B#"),
             "tensions": ("R","3","#11","#5","b7"), "order": 10},

            {"scale": "Bb Major b6",
             "notes": ("F#","Bb","C","D","Fb"),
             "tensions": ("3","#5","b7","R","#9"), "order": 20},

            {"scale": "Eb minor 6",
             "notes": ("Eb","Gb","Ab","Bb","C"),
             "tensions": ("b9","3","b5","#5","b7"), "order": 30},

            {"scale": "F minor",
             "notes": ("F","Ab","Bb","C","Eb"),
             "tensions": ("#9","b5","#5","b7","b9"), "order": 40},

            {"scale": "F minor 6",
             "notes": ("F","Ab","Bb","C","D"),
             "tensions": ("#9","b5","#5","b7","R"), "order": 50},

            {"scale": "C minor 7b5",
             "notes": ("C","Eb","F","Gb","Bb"),
             "tensions": ("b7","b9","#9","b5","#5"), "order": 60},
        ]},
    ],

    # Eb
    "EbMaj7": [
        {"notes": ("Eb","G","Bb","D")},
        {"scales": [
            {"scale": "C minor",
             "notes": ("C","Eb","G","Ab","Bb"),
             "tensions": ("13","R","3","#11","5"), "order": 10},

            {"scale": "G minor",
             "notes": ("G","Bb","C","D","F"),
             "tensions": ("3","5","13","7","9"), "order": 20},

            {"scale": "D minor",
             "notes": ("D","F","G","A","C"),
             "tensions": ("7","9","3","#11","13"), "order": 30},
        ]},
    ],

    "EbMaj7#11": [
        {"notes": ("Eb","G","Bb","D","A")},
        {"scales": [
            {"scale": "C minor 6",
             "notes": ("C","Eb","F","G","A"),
             "tensions": ("13","R","9","3","#11"), "order": 10},

            {"scale": "D minor",
             "notes": ("D","F","G","A","C"),
             "tensions": ("7","9","3","#11","13"), "order": 20},

            {"scale": "A Whole Tone",
             "notes": ("A","C#","D#","F","G"),
             "tensions": ("#11","7","R","9","3"), "order": 30},
        ]},
    ],

    "EbMaj7#5": [
        {"notes": ("Eb","G","B","D")},
        {"scales": [
            {"scale": "G Major b6",
             "notes": ("Eb","G","A","B","D"),
             "tensions": ("R","3","#11","#5","7"), "order": 10},

            {"scale": "D minor 6",
             "notes": ("D","F","G","A","B"),
             "tensions": ("7","9","3","#11","#5"), "order": 20},
        ]},
    ],

    "EbMaj7b5": [
        {"notes": ("Eb","G","Bbb","D")},
        {"scales": [
            {"scale": "A minor 7b5",
             "notes": ("A","C","D","Eb","G"),
             "tensions": ("b5","13","7","R","3"), "order": 10},
        ]},
    ],

    "Ebmin7": [
        {"notes": ("Eb","Gb","Bb","Db")},
        {"scales": [
            {"scale": "Eb minor",
             "notes": ("Eb","Gb","Ab","Bb","Db"),
             "tensions": ("R","b3","11","5","b7"), "order": 10},

            {"scale": "Bb minor",
             "notes": ("Bb","Db","Eb","F","Ab"),
             "tensions": ("5","b7","R","9","11"), "order": 20},

            {"scale": "F minor",
             "notes": ("F","Ab","Bb","C","Eb"),
             "tensions": ("9","11","5","13","R"), "order": 30},

            {"scale": "Db minor",
             "notes": ("Db","E","Gb","Ab","C"),
             "tensions": ("b7","b9","b3","11","13"), "order": 40},
        ]},
    ],

    "Ebmin6": [
        {"notes": ("Eb","Gb","Bb","C")},
        {"scales": [
            {"scale": "Eb minor 6",
             "notes": ("Eb","Gb","Ab","Bb","C"),
             "tensions": ("R","b3","11","5","13"), "order": 10},

            {"scale": "C minor 7b5",
             "notes": ("C","Eb","F","Gb","Bb"),
             "tensions": ("13","R","9","b3","5"), "order": 20},
        ]},
    ],

    "Ebmin/Maj7": [
        {"notes": ("Eb","Gb","Bb","D")},
        {"scales": [
            {"scale": "Bb Major b6",
             "notes": ("G","Bb","C","D","F"),
             "tensions": ("b3","5","13","7","9"), "order": 10},

            {"scale": "D Whole Tone",
             "notes": ("D","F","G","A","B"),
             "tensions": ("7","b3","11","5","13"), "order": 20},
        ]},
    ],

    "Ebmin7b5": [
        {"notes": ("Eb","Gb","Bbb","Db")},
        {"scales": [
            {"scale": "Gb minor 6",
             "notes": ("Gb","Bb","Cb","Db","Eb"),
             "tensions": ("b3","b5","13","b7","R"), "order": 10},

            {"scale": "Eb minor 7b5",
             "notes": ("Eb","Gb","Ab","Bbb","Db"),
             "tensions": ("R","b3","11","b5","b7"), "order": 20},

            {"scale": "Ab minor",
             "notes": ("Ab","Cb","Db","Eb","Gb"),
             "tensions": ("11","13","b7","R","b3"), "order": 30},
        ]},
    ],

    "Ebmin7b5nat9": [
        {"notes": ("Eb","Gb","Bbb","Db","F")},
        {"scales": [
            {"scale": "C Major b6",
             "notes": ("Bb","Db","Eb","F","Ab"),
             "tensions": ("b5","b7","R","9","11"), "order": 10},
        ]},
    ],

    "Eb7": [
        {"notes": ("Eb","G","Bb","Db")},
        {"scales": [
            {"scale": "Bb minor 6",
             "notes": ("Bb","Db","Eb","F","G"),
             "tensions": ("5","b7","R","9","3"), "order": 10},

            {"scale": "F minor",
             "notes": ("F","Ab","Bb","C","Eb"),
             "tensions": ("9","11","5","13","R"), "order": 20},

            {"scale": "C minor",
             "notes": ("C","Eb","F","G","Bb"),
             "tensions": ("13","R","9","3","5"), "order": 30},

            {"scale": "G minor 7b5",
             "notes": ("G","Bb","C","Db","F"),
             "tensions": ("3","5","13","b7","9"), "order": 40},

            {"scale": "F# minor",
             "notes": ("F#","A","B","Db","Fb"),
             "tensions": ("#9","b5","#5","b7","b9"), "order": 50},

            {"scale": "Eb Major b2",
             "notes": ("Eb","Fb","G","Bb","C"),
             "tensions": ("R","b9","3","5","13"), "order": 60},

            {"scale": "Gb Major b2",
             "notes": ("Gb","G","Bb","Db","Eb"),
             "tensions": ("#9","3","5","b7","R"), "order": 70},

            {"scale": "A Major b2",
             "notes": ("A","Bb","Db","Eb","F#"),
             "tensions": ("#11","5","b7","b9","#9"), "order": 80},

            {"scale": "C Major b2",
             "notes": ("C","Db","Fb","G","A"),
             "tensions": ("13","b7","b9","3","#11"), "order": 90},
        ]},
    ],

    "Eb7#11": [
        {"notes": ("Eb","G","Bb","Db","A")},
        {"scales": [
            {"scale": "Bb Whole Tone",
             "notes": ("Bb","Db","Eb","F","G"),
             "tensions": ("5","b7","R","9","3"), "order": 10},

            {"scale": "F Major b6",
             "notes": ("Db","F","G","A","Bb"),
             "tensions": ("b7","9","3","#11","5"), "order": 20},

            {"scale": "C minor 6",
             "notes": ("C","Eb","F","G","A"),
             "tensions": ("13","R","9","3","#11"), "order": 30},
        ]},
    ],

    "Eb7b9sus": [
        {"notes": ("Eb","Ab","Bb","Db","Fb")},
        {"scales": [
            {"scale": "Db minor 6",
             "notes": ("Db","Fb","Gb","Ab","Cb"),
             "tensions": ("b7","b9","#9","11","13"), "order": 20},
        ]},
    ],

    "Eb7nat9b13": [
        {"notes": ("Eb","G","Bb","Db","F","Cb")},
        {"scales": [
            {"scale": "G Whole Tone",
             "notes": ("G","B","C#","Eb","F"),
             "tensions": ("3","b13","b7","R","9"), "order": 10},
        ]},
    ],

    "Eb7alt": [
        {"notes": ("Eb","G","A","Bb","Db","Fb","F#")},
        {"scales": [
            {"scale": "Eb Whole Tone",
             "notes": ("Eb","G","A","B","Db"),
             "tensions": ("R","3","#11","#5","b7"), "order": 10},

            {"scale": "B Major b6",
             "notes": ("G","B","Db","Eb","F#"),
             "tensions": ("3","#5","b7","R","#9"), "order": 20},

            {"scale": "Fb minor 6",
             "notes": ("Fb","G","Bbb","Cb","Db"),
             "tensions": ("b9","3","b5","#5","b7"), "order": 30},

            {"scale": "F# minor",
             "notes": ("F#","Bbb","B","Db","Fb"),
             "tensions": ("#9","b5","#5","b7","b9"), "order": 40},

            {"scale": "F# minor 6",
             "notes": ("F#","Bbb","B","Db","Eb"),
             "tensions": ("#9","b5","#5","b7","R"), "order": 50},

            {"scale": "Db minor 7b5",
             "notes": ("Db","Fb","Gb","Bbb","Cb"),
             "tensions": ("b7","b9","#9","b5","#5"), "order": 60},
        ]},
    ],

    # E
    "EMaj7": [
        {"notes": ("E","G#","B","D#")},
        {"scales": [
            {"scale": "C# minor",
             "notes": ("C#","E","G#","A","B"),
             "tensions": ("13","R","3","11","5"), "order": 10},

            {"scale": "G# minor",
             "notes": ("G#","B","C#","D#","F#"),
             "tensions": ("3","5","13","7","9"), "order": 20},

            {"scale": "D# minor",
             "notes": ("D#","F#","G#","A#","C#"),
             "tensions": ("7","9","3","#11","13"), "order": 30},
        ]},
    ],

    "EMaj7#11": [
        {"notes": ("E","G#","B","D#","A#")},
        {"scales": [
            {"scale": "C# minor 6",
             "notes": ("C#","E","F#","G#","A#"),
             "tensions": ("13","R","9","3","#11"), "order": 10},

            {"scale": "D# minor",
             "notes": ("D#","F#","G#","A#","C#"),
             "tensions": ("7","9","3","#11","13"), "order": 20},

            {"scale": "A# Whole Tone",
             "notes": ("A#","C##","D##","F","G"),
             "tensions": ("#11","7","R","9","3"), "order": 30},
        ]},
    ],

    "EMaj7#5": [
        {"notes": ("E","G#","B#","D#")},
        {"scales": [
            {"scale": "G# Major b6",
             "notes": ("E","G#","A#","B#","D#"),
             "tensions": ("R","3","#11","#5","7"), "order": 10},

            {"scale": "D# minor 6",
             "notes": ("D#","F#","G#","A#","B#"),
             "tensions": ("7","9","3","#11","#5"), "order": 20},
        ]},
    ],

    "EMaj7b5": [
        {"notes": ("E","G#","Bb","D#")},
        {"scales": [
            {"scale": "Bb minor 7b5",
             "notes": ("Bb","Db","Ebb","Fb","Ab"),
             "tensions": ("b5","13","7","R","3"), "order": 10},
        ]},
    ],

    "Emin7": [
        {"notes": ("E","G","B","D")},
        {"scales": [
            {"scale": "E minor",
             "notes": ("E","G","A","B","D"),
             "tensions": ("R","b3","11","5","b7"), "order": 10},

            {"scale": "B minor",
             "notes": ("B","D","E","F#","A"),
             "tensions": ("5","b7","R","9","11"), "order": 20},

            {"scale": "F# minor",
             "notes": ("F#","A","B","C#","E"),
             "tensions": ("9","11","5","13","R"), "order": 30},

            {"scale": "D minor",
             "notes": ("D","F","G","A","C"),
             "tensions": ("b7","b9","b3","11","13"), "order": 40},
        ]},
    ],

    "Emin6": [
        {"notes": ("E","G","B","C#")},
        {"scales": [
            {"scale": "E minor 6",
             "notes": ("E","G","A","B","C#"),
             "tensions": ("R","b3","11","5","13"), "order": 10},

            {"scale": "C# minor 7b5",
             "notes": ("C#","E","F#","G","B"),
             "tensions": ("13","R","9","b3","5"), "order": 20},
        ]},
    ],

    "Emin/Maj7": [
        {"notes": ("E","G","B","D#")},
        {"scales": [
            {"scale": "B Major b6",
             "notes": ("G","B","C#","D#","F#"),
             "tensions": ("b3","5","13","7","9"), "order": 10},

            {"scale": "D# Whole Tone",
             "notes": ("D#","G","A","B","C#"),
             "tensions": ("7","b3","11","5","13"), "order": 20},
        ]},
    ],

    "Emin7b5": [
        {"notes": ("E","G","Bb","D")},
        {"scales": [
            {"scale": "G minor 6",
             "notes": ("G","Bb","C","D","E"),
             "tensions": ("b3","b5","13","b7","R"), "order": 10},

            {"scale": "E minor 7b5",
             "notes": ("E","G","A","Bb","D"),
             "tensions": ("R","b3","11","b5","b7"), "order": 20},

            {"scale": "A minor",
             "notes": ("A","C","D","E","G"),
             "tensions": ("11","13","b7","R","b3"), "order": 30},
        ]},
    ],

    "Emin7b5nat9": [
        {"notes": ("E","G","Bb","D","F#")},
        {"scales": [
            {"scale": "D Major b6",
             "notes": ("B","D","E","F#","A"),
             "tensions": ("b5","b7","R","9","11"), "order": 10},
        ]},
    ],

    "E7": [
        {"notes": ("E","G#","B","D")},
        {"scales": [
            {"scale": "B minor 6",
             "notes": ("B","D","E","F#","G#"),
             "tensions": ("5","b7","R","9","3"), "order": 10},

            {"scale": "F# minor",
             "notes": ("F#","A","B","C#","E"),
             "tensions": ("9","11","5","13","R"), "order": 20},

            {"scale": "C# minor",
             "notes": ("C#","E","F#","G#","B"),
             "tensions": ("13","R","9","3","5"), "order": 30},

            {"scale": "G# minor 7b5",
             "notes": ("G#","B","C#","D","F#"),
             "tensions": ("3","5","13","b7","9"), "order": 40},

            {"scale": "G## minor",
             "notes": ("G##","B#","C##","D#","F##"),
             "tensions": ("#9","b5","#5","b7","b9"), "order": 50},

            {"scale": "E Major b2",
             "notes": ("E","F","G#","B","C#"),
             "tensions": ("R","b9","3","5","13"), "order": 60},

            {"scale": "G Major b2",
             "notes": ("G","Ab","B","D","E"),
             "tensions": ("#9","3","5","b7","R"), "order": 70},

            {"scale": "A# Major b2",
             "notes": ("A#","B","Cx","E#","Fx"),
             "tensions": ("#11","5","b7","b9","#9"), "order": 80},

            {"scale": "C# Major b2",
             "notes": ("C#","D","E#","G#","A#"),
             "tensions": ("13","b7","b9","3","#11"), "order": 90},
        ]},
    ],

    "E7#11": [
        {"notes": ("E","G#","B","D","A#")},
        {"scales": [
            {"scale": "B Whole Tone",
             "notes": ("B","D","E","F#","G#"),
             "tensions": ("5","b7","R","9","3"), "order": 10},

            {"scale": "F# Major b6",
             "notes": ("D","F#","G#","A#","B"),
             "tensions": ("b7","9","3","#11","5"), "order": 20},

            {"scale": "C# minor 6",
             "notes": ("C#","E","F#","G#","A#"),
             "tensions": ("13","R","9","3","#11"), "order": 30},
        ]},
    ],

    "E7b9sus": [
        {"notes": ("E","A","B","D","F")},
        {"scales": [
            {"scale": "D minor 6",
             "notes": ("D","F","G","A","B"),
             "tensions": ("b7","b9","#9","11","13"), "order": 20},
        ]},
    ],

    "E7nat9b13": [
        {"notes": ("E","G#","B","D","F#","C")},
        {"scales": [
            {"scale": "G# Whole Tone",
             "notes": ("G#","B#","C##","D#","F#"),
             "tensions": ("3","b13","b7","R","9"), "order": 10},
        ]},
    ],

    "E7alt": [
        {"notes": ("E","G#","Bb","B#","D","F","F#")},
        {"scales": [
            {"scale": "E Whole Tone",
             "notes": ("E","G#","A#","B#","C##"),
             "tensions": ("R","3","#11","#5","b7"), "order": 10},

            {"scale": "C Major b6",
             "notes": ("G#","C","D","E","Fb"),
             "tensions": ("3","#5","b7","R","#9"), "order": 20},

            {"scale": "F minor 6",
             "notes": ("F","Ab","Bb","C","D"),
             "tensions": ("b9","3","b5","#5","b7"), "order": 30},

            {"scale": "G minor",
             "notes": ("G","Bb","C","D","F"),
             "tensions": ("#9","b5","#5","b7","b9"), "order": 40},

            {"scale": "G minor 6",
             "notes": ("G","Bb","C","D","E"),
             "tensions": ("#9","b5","#5","b7","R"), "order": 50},

            {"scale": "D minor 7b5",
             "notes": ("D","F","G","Ab","C"),
             "tensions": ("b7","b9","#9","b5","#5"), "order": 60},
        ]},
    ],

    # F
    "FMaj7": [
        {"notes": ("F","A","C","E")},
        {"scales": [
            {"scale": "D minor",
             "notes": ("D","F","A","Bb","C"),
             "tensions": ("13","R","3","11","5"), "order": 10},

            {"scale": "A minor",
             "notes": ("A","C","D","E","G"),
             "tensions": ("3","5","13","7","9"), "order": 20},

            {"scale": "E minor",
             "notes": ("E","G","A","B","D"),
             "tensions": ("7","9","3","#11","13"), "order": 30},
        ]},
    ],

    "FMaj7#11": [
        {"notes": ("F","A","C","E","B")},
        {"scales": [
            {"scale": "D minor 6",
             "notes": ("D","F","G","A","B"),
             "tensions": ("13","R","9","3","#11"), "order": 10},

            {"scale": "E minor",
             "notes": ("E","G","A","B","D"),
             "tensions": ("7","9","3","#11","13"), "order": 20},

            {"scale": "B Whole Tone",
             "notes": ("B","D#","E#","G","A"),
             "tensions": ("#11","7","R","9","3"), "order": 30},
        ]},
    ],

    "FMaj7#5": [
        {"notes": ("F","A","C#","E")},
        {"scales": [
            {"scale": "A Major b6",
             "notes": ("F","A","B","C#","E"),
             "tensions": ("R","3","#11","#5","7"), "order": 10},

            {"scale": "E minor 6",
             "notes": ("E","G","A","B","C#"),
             "tensions": ("7","9","3","#11","#5"), "order": 20},
        ]},
    ],

    "FMaj7b5": [
        {"notes": ("F","A","Cb","E")},
        {"scales": [
            {"scale": "Cb minor 7b5",
             "notes": ("Cb","Ebb","Fb","Gbb","Bbb"),
             "tensions": ("b5","13","7","R","3"), "order": 10},
        ]},
    ],

    "Fmin7": [
        {"notes": ("F","Ab","C","Eb")},
        {"scales": [
            {"scale": "F minor",
             "notes": ("F","Ab","Bb","C","Eb"),
             "tensions": ("R","b3","11","5","b7"), "order": 10},

            {"scale": "C minor",
             "notes": ("C","Eb","F","G","Bb"),
             "tensions": ("5","b7","R","9","11"), "order": 20},

            {"scale": "G minor",
             "notes": ("G","Bb","C","D","F"),
             "tensions": ("9","11","5","13","R"), "order": 30},

            {"scale": "Eb minor",
             "notes": ("Eb","Gb","Ab","Bb","Db"),
             "tensions": ("b7","b9","b3","11","13"), "order": 40},
        ]},
    ],

    "Fmin6": [
        {"notes": ("F","Ab","C","D")},
        {"scales": [
            {"scale": "F minor 6",
             "notes": ("F","Ab","Bb","C","D"),
             "tensions": ("R","b3","11","5","13"), "order": 10},

            {"scale": "D minor 7b5",
             "notes": ("D","F","G","Ab","C"),
             "tensions": ("13","R","9","b3","5"), "order": 20},
        ]},
    ],

    "Fmin/Maj7": [
        {"notes": ("F","Ab","C","E")},
        {"scales": [
            {"scale": "C Major b6",
             "notes": ("Ab","C","D","E","G"),
             "tensions": ("b3","5","13","7","9"), "order": 10},

            {"scale": "E Whole Tone",
             "notes": ("E","G#","A#","C","D"),
             "tensions": ("7","b3","11","5","13"), "order": 20},
        ]},
    ],

    "Fmin7b5": [
        {"notes": ("F","Ab","Cb","Eb")},
        {"scales": [
            {"scale": "Ab minor 6",
             "notes": ("Ab","Cb","Db","Eb","F"),
             "tensions": ("b3","b5","13","b7","R"), "order": 10},

            {"scale": "F minor 7b5",
             "notes": ("F","Ab","Bb","Cb","Eb"),
             "tensions": ("R","b3","11","b5","b7"), "order": 20},

            {"scale": "Bb minor",
             "notes": ("Bb","Db","Eb","F","Ab"),
             "tensions": ("11","13","b7","R","b3"), "order": 30},
        ]},
    ],

    "Fmin7b5nat9": [
        {"notes": ("F","Ab","Cb","Eb","G")},
        {"scales": [
            {"scale": "Db Major b6",
             "notes": ("Bb","Db","Eb","F","Ab"),
             "tensions": ("b5","b7","R","9","11"), "order": 10},
        ]},
    ],

    "F7": [
        {"notes": ("F","A","C","Eb")},
        {"scales": [
            {"scale": "C minor 6",
             "notes": ("C","Eb","F","G","A"),
             "tensions": ("5","b7","R","9","3"), "order": 10},

            {"scale": "G minor",
             "notes": ("G","Bb","C","D","F"),
             "tensions": ("9","11","5","13","R"), "order": 20},

            {"scale": "D minor",
             "notes": ("D","F","G","A","C"),
             "tensions": ("13","R","9","3","5"), "order": 30},

            {"scale": "A minor 7b5",
             "notes": ("A","C","D","Eb","G"),
             "tensions": ("3","5","13","b7","9"), "order": 40},

            {"scale": "G# minor",
             "notes": ("G#","B","C#","Eb","Gb"),
             "tensions": ("#9","b5","#5","b7","b9"), "order": 50},

            {"scale": "F Major b2",
             "notes": ("F","Gb","A","C","D"),
             "tensions": ("R","b9","3","5","13"), "order": 60},

            {"scale": "Ab Major b2",
             "notes": ("Ab","A","C","Eb","F"),
             "tensions": ("#9","3","5","b7","R"), "order": 70},

            {"scale": "B Major b2",
             "notes": ("B","C","D#","F#","G#"),
             "tensions": ("#11","5","b7","b9","#9"), "order": 80},

            {"scale": "D Major b2",
             "notes": ("D","Eb","F#","A","B"),
             "tensions": ("13","b7","b9","3","#11"), "order": 90},
        ]},
    ],

    "F7#11": [
        {"notes": ("F","A","C","Eb","B")},
        {"scales": [
            {"scale": "C Whole Tone",
             "notes": ("C","E","F#","G#","A#"),
             "tensions": ("5","b7","R","9","3"), "order": 10},

            {"scale": "G Major b6",
             "notes": ("Eb","G","A","B","C"),
             "tensions": ("b7","9","3","#11","5"), "order": 20},

            {"scale": "D minor 6",
             "notes": ("D","F","G","A","B"),
             "tensions": ("13","R","9","3","#11"), "order": 30},
        ]},
    ],

    "F7b9sus": [
        {"notes": ("F","Bb","C","Eb","Gb")},
        {"scales": [
            {"scale": "Eb minor 6",
             "notes": ("Eb","Gb","Ab","Bb","C"),
             "tensions": ("b7","b9","#9","11","13"), "order": 20},
        ]},
    ],

    "F7nat9b13": [
        {"notes": ("F","A","C","Eb","G","Db")},
        {"scales": [
            {"scale": "A Whole Tone",
             "notes": ("A","C#","D#","F","G"),
             "tensions": ("3","b13","b7","R","9"), "order": 10},
        ]},
    ],

    "F7alt": [
        {"notes": ("F","A","Cb","C#","Eb","Gb","G")},
        {"scales": [
            {"scale": "F Whole Tone",
             "notes": ("F","A","B","C#","D#"),
             "tensions": ("R","3","#11","#5","b7"), "order": 10},

            {"scale": "C# Major b6",
             "notes": ("A","C#","D#","F","G#"),
             "tensions": ("3","#5","b7","R","#9"), "order": 20},

            {"scale": "G minor 6",
             "notes": ("G","Bb","C","D","E"),
             "tensions": ("b9","3","b5","#5","b7"), "order": 30},

            {"scale": "A minor",
             "notes": ("A","C","D","E","G"),
             "tensions": ("#9","b5","#5","b7","b9"), "order": 40},

            {"scale": "A minor 6",
             "notes": ("A","C","D","E","F#"),
             "tensions": ("#9","b5","#5","b7","R"), "order": 50},

            {"scale": "Eb minor 7b5",
             "notes": ("Eb","Gb","Ab","Bbb","Cb"),
             "tensions": ("b7","b9","#9","b5","#5"), "order": 60},
        ]},
    ],

    # F#
    "F#Maj7": [
        {"notes": ("F#","A#","C#","E#")},
        {"scales": [
            {"scale": "D# minor",
             "notes": ("D#","F#","A#","B","C#"),
             "tensions": ("13","R","3","11","5"), "order": 10},

            {"scale": "A# minor",
             "notes": ("A#","C#","D#","E#","G#"),
             "tensions": ("3","5","13","7","9"), "order": 20},

            {"scale": "E# minor",
             "notes": ("E#","G#","A#","B#","D#"),
             "tensions": ("7","9","3","#11","13"), "order": 30},
        ]},
    ],

    "F#Maj7#11": [
        {"notes": ("F#","A#","C#","E#","B#")},
        {"scales": [
            {"scale": "D# minor 6",
             "notes": ("D#","F#","G#","A#","B#"),
             "tensions": ("13","R","9","3","#11"), "order": 10},

            {"scale": "E# minor",
             "notes": ("E#","G#","A#","B#","D#"),
             "tensions": ("7","9","3","#11","13"), "order": 20},

            {"scale": "B# Whole Tone",
             "notes": ("B#","D##","E##","G","A"),
             "tensions": ("#11","7","R","9","3"), "order": 30},
        ]},
    ],

    "F#Maj7#5": [
        {"notes": ("F#","A#","C##","E#")},
        {"scales": [
            {"scale": "A# Major b6",
             "notes": ("F#","A#","B#","C##","E#"),
             "tensions": ("R","3","#11","#5","7"), "order": 10},

            {"scale": "E# minor 6",
             "notes": ("E#","G#","A#","B#","C##"),
             "tensions": ("7","9","3","#11","#5"), "order": 20},
        ]},
    ],

    "F#Maj7b5": [
        {"notes": ("F#","A#","C","E#")},
        {"scales": [
            {"scale": "C minor 7b5",
             "notes": ("C","Eb","F","Gb","Bb"),
             "tensions": ("b5","13","7","R","3"), "order": 10},
        ]},
    ],

    "F#min7": [
        {"notes": ("F#","A","C#","E")},
        {"scales": [
            {"scale": "F# minor",
             "notes": ("F#","A","B","C#","E"),
             "tensions": ("R","b3","11","5","b7"), "order": 10},

            {"scale": "C# minor",
             "notes": ("C#","E","F#","G#","B"),
             "tensions": ("5","b7","R","9","11"), "order": 20},

            {"scale": "G# minor",
             "notes": ("G#","B","C#","D#","F#"),
             "tensions": ("9","11","5","13","R"), "order": 30},

            {"scale": "E minor",
             "notes": ("E","G","A","B","D"),
             "tensions": ("b7","b9","b3","11","13"), "order": 40},
        ]},
    ],

    "F#min6": [
        {"notes": ("F#","A","C#","D#")},
        {"scales": [
            {"scale": "F# minor 6",
             "notes": ("F#","A","B","C#","D#"),
             "tensions": ("R","b3","11","5","13"), "order": 10},

            {"scale": "D# minor 7b5",
             "notes": ("D#","F#","G#","A","C#"),
             "tensions": ("13","R","9","b3","5"), "order": 20},
        ]},
    ],

    "F#min/Maj7": [
        {"notes": ("F#","A","C#","E#")},
        {"scales": [
            {"scale": "C# Major b6",
             "notes": ("A","C#","D#","E#","G#"),
             "tensions": ("b3","5","13","7","9"), "order": 10},

            {"scale": "E# Whole Tone",
             "notes": ("E#","G##","A##","C#","D#"),
             "tensions": ("7","b3","11","5","13"), "order": 20},
        ]},
    ],

    "F#min7b5": [
        {"notes": ("F#","A","C","E")},
        {"scales": [
            {"scale": "A minor 6",
             "notes": ("A","C","D","E","F#"),
             "tensions": ("b3","b5","13","b7","R"), "order": 10},

            {"scale": "F# minor 7b5",
             "notes": ("F#","A","B","C","E"),
             "tensions": ("R","b3","11","b5","b7"), "order": 20},

            {"scale": "B minor",
             "notes": ("B","D","E","F#","A"),
             "tensions": ("11","13","b7","R","b3"), "order": 30},
        ]},
    ],

    "F#min7b5nat9": [
        {"notes": ("F#","A","C","E","G#")},
        {"scales": [
            {"scale": "D Major b6",
             "notes": ("B","D","E","F#","A"),
             "tensions": ("b5","b7","R","9","11"), "order": 10},
        ]},
    ],

    "F#7": [
        {"notes": ("F#","A#","C#","E")},
        {"scales": [
            {"scale": "C# minor 6",
             "notes": ("C#","E","F#","G#","A#"),
             "tensions": ("5","b7","R","9","3"), "order": 10},

            {"scale": "G# minor",
             "notes": ("G#","B","C#","D#","F#"),
             "tensions": ("9","11","5","13","R"), "order": 20},

            {"scale": "D# minor",
             "notes": ("D#","F#","G#","A#","C#"),
             "tensions": ("13","R","9","3","5"), "order": 30},

            {"scale": "A# minor 7b5",
             "notes": ("A#","C#","D#","E","G#"),
             "tensions": ("3","5","13","b7","9"), "order": 40},

            {"scale": "B# minor",
             "notes": ("B#","D#","E#","G","A"),
             "tensions": ("#9","b5","#5","b7","b9"), "order": 50},

            {"scale": "F# Major b2",
             "notes": ("F#","G","A#","C#","D#"),
             "tensions": ("R","b9","3","5","13"), "order": 60},

            {"scale": "A Major b2",
             "notes": ("A","Bb","C#","E","F#"),
             "tensions": ("#9","3","5","b7","R"), "order": 70},

            {"scale": "C## Major b2",
             "notes": ("C##","D#","E##","G##","A##"),
             "tensions": ("#11","5","b7","b9","#9"), "order": 80},

            {"scale": "E Major b2",
             "notes": ("E","F","G#","B","C#"),
             "tensions": ("13","b7","b9","3","#11"), "order": 90},
        ]},
    ],

    "F#7#11": [
        {"notes": ("F#","A#","C#","E","B#")},
        {"scales": [
            {"scale": "C# Whole Tone",
             "notes": ("C#","E","F#","G#","A#"),
             "tensions": ("5","b7","R","9","3"), "order": 10},

            {"scale": "G# Major b6",
             "notes": ("E","G#","A#","B#","C#"),
             "tensions": ("b7","9","3","#11","5"), "order": 20},

            {"scale": "D# minor 6",
             "notes": ("D#","F#","G#","A#","B#"),
             "tensions": ("13","R","9","3","#11"), "order": 30},
        ]},
    ],

    "F#7b9sus": [
        {"notes": ("F#","B","C#","E","G")},
        {"scales": [
            {"scale": "E minor 6",
             "notes": ("E","G","A","B","C#"),
             "tensions": ("b7","b9","#9","11","13"), "order": 20},
        ]},
    ],

    "F#7nat9b13": [
        {"notes": ("F#","A#","C#","E","G#","D")},
        {"scales": [
            {"scale": "A# Whole Tone",
             "notes": ("A#","C##","D##","F","G"),
             "tensions": ("3","b13","b7","R","9"), "order": 10},
        ]},
    ],

    "F#7alt": [
        {"notes": ("F#","A#","C","C##","E","G","G#")},
        {"scales": [
            {"scale": "F# Whole Tone",
             "notes": ("F#","A#","B#","C##","D##"),
             "tensions": ("R","3","#11","#5","b7"), "order": 10},

            {"scale": "D Major b6",
             "notes": ("A#","D","E","F#","G#"),
             "tensions": ("3","#5","b7","R","#9"), "order": 20},

            {"scale": "A minor 6",
             "notes": ("A","C","D","E","F#"),
             "tensions": ("b9","3","b5","#5","b7"), "order": 30},

            {"scale": "B minor",
             "notes": ("B","D","E","F#","A"),
             "tensions": ("#9","b5","#5","b7","b9"), "order": 40},

            {"scale": "B minor 6",
             "notes": ("B","D","E","F#","G#"),
             "tensions": ("#9","b5","#5","b7","R"), "order": 50},

            {"scale": "E minor 7b5",
             "notes": ("E","G","A","Bb","D"),
             "tensions": ("b7","b9","#9","b5","#5"), "order": 60},
        ]},
    ],

    # G
    "GMaj7": [
        {"notes": ("G","B","D","F#")},
        {"scales": [
            {"scale": "E minor",
             "notes": ("E","G","B","C","D"),
             "tensions": ("13","R","3","11","5"), "order": 10},

            {"scale": "B minor",
             "notes": ("B","D","E","F#","A"),
             "tensions": ("3","5","13","7","9"), "order": 20},

            {"scale": "F# minor",
             "notes": ("F#","A","B","C#","E"),
             "tensions": ("7","9","3","#11","13"), "order": 30},
        ]},
    ],

    "GMaj7#11": [
        {"notes": ("G","B","D","F#","C#")},
        {"scales": [
            {"scale": "E minor 6",
             "notes": ("E","G","A","B","C#"),
             "tensions": ("13","R","9","3","#11"), "order": 10},

            {"scale": "B minor",
             "notes": ("B","D","E","F#","A"),
             "tensions": ("7","9","3","#11","13"), "order": 20},

            {"scale": "C# Whole Tone",
             "notes": ("C#","E","F#","G#","A#"),
             "tensions": ("#11","7","R","9","3"), "order": 30},
        ]},
    ],

    "GMaj7#5": [
        {"notes": ("G","B","D#","F#")},
        {"scales": [
            {"scale": "B Major b6",
             "notes": ("G","B","C#","D#","F#"),
             "tensions": ("R","3","#11","#5","7"), "order": 10},

            {"scale": "F# minor 6",
             "notes": ("F#","A","B","C#","D#"),
             "tensions": ("7","9","3","#11","#5"), "order": 20},
        ]},
    ],

    "GMaj7b5": [
        {"notes": ("G","B","Db","F#")},
        {"scales": [
            {"scale": "Db minor 7b5",
             "notes": ("Db","E","Gb","A","C"),
             "tensions": ("b5","13","7","R","3"), "order": 10},
        ]},
    ],

    "Gmin7": [
        {"notes": ("G","Bb","D","F")},
        {"scales": [
            {"scale": "G minor",
             "notes": ("G","Bb","C","D","F"),
             "tensions": ("R","b3","11","5","b7"), "order": 10},

            {"scale": "D minor",
             "notes": ("D","F","G","A","C"),
             "tensions": ("5","b7","R","9","11"), "order": 20},

            {"scale": "A minor",
             "notes": ("A","C","D","E","G"),
             "tensions": ("9","11","5","13","R"), "order": 30},

            {"scale": "F minor",
             "notes": ("F","Ab","Bb","C","Eb"),
             "tensions": ("b7","b9","b3","11","13"), "order": 40},
        ]},
    ],

    "Gmin6": [
        {"notes": ("G","Bb","D","E")},
        {"scales": [
            {"scale": "G minor 6",
             "notes": ("G","Bb","C","D","E"),
             "tensions": ("R","b3","11","5","13"), "order": 10},

            {"scale": "E minor 7b5",
             "notes": ("E","G","A","Bb","D"),
             "tensions": ("13","R","9","b3","5"), "order": 20},
        ]},
    ],

    "Gmin/Maj7": [
        {"notes": ("G","Bb","D","F#")},
        {"scales": [
            {"scale": "D Major b6",
             "notes": ("Bb","D","E","F#","A"),
             "tensions": ("b3","5","13","7","9"), "order": 10},

            {"scale": "F# Whole Tone",
             "notes": ("F#","A#","B#","D","E"),
             "tensions": ("7","b3","11","5","13"), "order": 20},
        ]},
    ],

    "Gmin7b5": [
        {"notes": ("G","Bb","Db","F")},
        {"scales": [
            {"scale": "Bb minor 6",
             "notes": ("Bb","Db","Eb","F","G"),
             "tensions": ("b3","5","13","b7","R"), "order": 10},

            {"scale": "G minor 7b5",
             "notes": ("G","Bb","C","Db","F"),
             "tensions": ("R","b3","11","b5","b7"), "order": 20},

            {"scale": "C minor",
             "notes": ("C","Eb","F","G","Bb"),
             "tensions": ("11","13","b7","R","b3"), "order": 30},
        ]},
    ],

    "Gmin7b5nat9": [
        {"notes": ("G","Bb","Db","F","A")},
        {"scales": [
            {"scale": "Eb Major b6",
             "notes": ("C","Eb","F","G","Bb"),
             "tensions": ("b5","b7","R","9","11"), "order": 10},
        ]},
    ],

    "G7": [
        {"notes": ("G","B","D","F")},
        {"scales": [
            {"scale": "D minor 6",
             "notes": ("D","F","G","A","B"),
             "tensions": ("5","b7","R","9","3"), "order": 10},

            {"scale": "A minor",
             "notes": ("A","C","D","E","G"),
             "tensions": ("9","11","5","13","R"), "order": 20},

            {"scale": "E minor",
             "notes": ("E","G","A","B","D"),
             "tensions": ("13","R","9","3","5"), "order": 30},

            {"scale": "B minor 7b5",
             "notes": ("B","D","E","F","A"),
             "tensions": ("3","5","13","b7","9"), "order": 40},

            {"scale": "F minor",
             "notes": ("F","Ab","Bb","C","Eb"),
             "tensions": ("#9","b5","#5","b7","b9"), "order": 50},

            {"scale": "G Major b2",
             "notes": ("G","Ab","B","D","E"),
             "tensions": ("R","b9","3","5","13"), "order": 60},

            {"scale": "Bb Major b2",
             "notes": ("Bb","Cb","D","F","G"),
             "tensions": ("#9","3","5","b7","R"), "order": 70},

            {"scale": "D# Major b2",
             "notes": ("D#","E","F##","A","B"),
             "tensions": ("#11","5","b7","b9","#9"), "order": 80},

            {"scale": "E Major b2",
             "notes": ("E","F","G#","B","C#"),
             "tensions": ("13","b7","b9","3","#11"), "order": 90},
        ]},
    ],

    "G7#11": [
        {"notes": ("G","B","D","F","C#")},
        {"scales": [
            {"scale": "D Whole Tone",
             "notes": ("D","F#","G#","A#","C"),
             "tensions": ("5","b7","R","9","3"), "order": 10},

            {"scale": "A Major b6",
             "notes": ("F","A","B","C#","D"),
             "tensions": ("b7","9","3","#11","5"), "order": 20},

            {"scale": "E minor 6",
             "notes": ("E","G","A","B","C#"),
             "tensions": ("13","R","9","3","#11"), "order": 30},
        ]},
    ],

    "G7b9sus": [
        {"notes": ("G","C","D","F","Ab")},
        {"scales": [
            {"scale": "F minor 6",
             "notes": ("F","Ab","Bb","C","D"),
             "tensions": ("b7","b9","#9","11","13"), "order": 20},
        ]},
    ],

    "G7nat9b13": [
        {"notes": ("G","B","D","F","A","Eb")},
        {"scales": [
            {"scale": "B Whole Tone",
             "notes": ("B","D#","E#","F##","A"),
             "tensions": ("3","b13","b7","R","9"), "order": 10},
        ]},
    ],

    "G7alt": [
        {"notes": ("G","B","Db","D#","F","Ab","A")},
        {"scales": [
            {"scale": "G Whole Tone",
             "notes": ("G","B","C#","D#","F"),
             "tensions": ("R","3","#11","#5","b7"), "order": 10},

            {"scale": "Eb Major b6",
             "notes": ("B","Eb","F","G","A"),
             "tensions": ("3","#5","b7","R","#9"), "order": 20},

            {"scale": "A minor 6",
             "notes": ("A","C","D","E","F#"),
             "tensions": ("b9","3","b5","#5","b7"), "order": 30},

            {"scale": "B minor",
             "notes": ("B","D","E","F#","A"),
             "tensions": ("#9","b5","#5","b7","b9"), "order": 40},

            {"scale": "B minor 6",
             "notes": ("B","D","E","F#","G#"),
             "tensions": ("#9","b5","#5","b7","R"), "order": 50},

            {"scale": "F minor 7b5",
             "notes": ("F","Ab","Bb","Cb","Eb"),
             "tensions": ("b7","b9","#9","b5","#5"), "order": 60},
        ]},
    ],

    # Ab
    "AbMaj7": [
        {"notes": ("Ab","C","Eb","G")},
        {"scales": [
            {"scale": "F minor",
             "notes": ("F","Ab","C","Db","Eb"),
             "tensions": ("13","R","3","11","5"), "order": 10},

            {"scale": "C minor",
             "notes": ("C","Eb","F","G","Bb"),
             "tensions": ("3","5","13","7","9"), "order": 20},

            {"scale": "G minor",
             "notes": ("G","Bb","C","D","F"),
             "tensions": ("7","9","3","#11","13"), "order": 30},
        ]},
    ],

    "AbMaj7#11": [
        {"notes": ("Ab","C","Eb","G","D")},
        {"scales": [
            {"scale": "F minor 6",
             "notes": ("F","Ab","Bb","C","D"),
             "tensions": ("13","R","9","3","#11"), "order": 10},

            {"scale": "C minor",
             "notes": ("C","Eb","F","G","Bb"),
             "tensions": ("7","9","3","#11","13"), "order": 20},

            {"scale": "D Whole Tone",
             "notes": ("D","F#","G#","A#","C"),
             "tensions": ("#11","7","R","9","3"), "order": 30},
        ]},
    ],

    "AbMaj7#5": [
        {"notes": ("Ab","C","E","G")},
        {"scales": [
            {"scale": "C Major b6",
             "notes": ("Ab","C","D","E","G"),
             "tensions": ("R","3","#11","#5","7"), "order": 10},

            {"scale": "G minor 6",
             "notes": ("G","Bb","C","D","E"),
             "tensions": ("7","9","3","#11","#5"), "order": 20},
        ]},
    ],

    "AbMaj7b5": [
        {"notes": ("Ab","C","Ebb","G")},
        {"scales": [
            {"scale": "Ebb minor 7b5",
             "notes": ("Ebb","Gb","Abb","Bbb","Db"),
             "tensions": ("b5","13","7","R","3"), "order": 10},
        ]},
    ],

    "Abmin7": [
        {"notes": ("Ab","Cb","Eb","Gb")},
        {"scales": [
            {"scale": "Ab minor",
             "notes": ("Ab","Cb","Db","Eb","Gb"),
             "tensions": ("R","b3","11","5","b7"), "order": 10},

            {"scale": "Eb minor",
             "notes": ("Eb","Gb","Ab","Bb","Db"),
             "tensions": ("5","b7","R","9","11"), "order": 20},

            {"scale": "Bb minor",
             "notes": ("Bb","Db","Eb","F","Ab"),
             "tensions": ("9","11","5","13","R"), "order": 30},

            {"scale": "Gb minor",
             "notes": ("Gb","Bbb","Cb","Db","Fb"),
             "tensions": ("b7","b9","b3","11","13"), "order": 40},
        ]},
    ],

    "Abmin6": [
        {"notes": ("Ab","Cb","Eb","F")},
        {"scales": [
            {"scale": "Ab minor 6",
             "notes": ("Ab","Cb","Db","Eb","F"),
             "tensions": ("R","b3","11","5","13"), "order": 10},

            {"scale": "F minor 7b5",
             "notes": ("F","Ab","Bb","Cb","Eb"),
             "tensions": ("13","R","9","b3","5"), "order": 20},
        ]},
    ],

    "Abmin/Maj7": [
        {"notes": ("Ab","Cb","Eb","G")},
        {"scales": [
            {"scale": "Eb Major b6",
             "notes": ("Cb","Eb","F","G","Bb"),
             "tensions": ("b3","5","13","7","9"), "order": 10},

            {"scale": "G Whole Tone",
             "notes": ("G","B","C#","Eb","F"),
             "tensions": ("7","b3","11","5","13"), "order": 20},
        ]},
    ],

    "Abmin7b5": [
        {"notes": ("Ab","Cb","Ebb","Gb")},
        {"scales": [
            {"scale": "Cb minor 6",
             "notes": ("Cb","Ebb","Fb","Gb","Bb"),
             "tensions": ("b3","5","13","b7","R"), "order": 10},

            {"scale": "Ab minor 7b5",
             "notes": ("Ab","Cb","Db","Ebb","Gb"),
             "tensions": ("R","b3","11","b5","b7"), "order": 20},

            {"scale": "Db minor",
             "notes": ("Db","E","Gb","Ab","C"),
             "tensions": ("11","13","b7","R","b3"), "order": 30},
        ]},
    ],

    "Abmin7b5nat9": [
        {"notes": ("Ab","Cb","Ebb","Gb","Bb")},
        {"scales": [
            {"scale": "F Major b6",
             "notes": ("D","F","G","A","C"),
             "tensions": ("b5","b7","R","9","11"), "order": 10},
        ]},
    ],

    "Ab7": [
        {"notes": ("Ab","C","Eb","Gb")},
        {"scales": [
            {"scale": "Eb minor 6",
             "notes": ("Eb","Gb","Ab","Bb","C"),
             "tensions": ("5","b7","R","9","3"), "order": 10},

            {"scale": "Bb minor",
             "notes": ("Bb","Db","Eb","F","Ab"),
             "tensions": ("9","11","5","13","R"), "order": 20},

            {"scale": "F minor",
             "notes": ("F","Ab","Bb","C","Eb"),
             "tensions": ("13","R","9","3","5"), "order": 30},

            {"scale": "C minor 7b5",
             "notes": ("C","Eb","F","Gb","Bb"),
             "tensions": ("3","5","13","b7","9"), "order": 40},

            {"scale": "Gb minor",
             "notes": ("Gb","Bbb","Cb","Db","Fb"),
             "tensions": ("#9","b5","#5","b7","b9"), "order": 50},

            {"scale": "Ab Major b2",
             "notes": ("Ab","Bbb","C","Eb","F"),
             "tensions": ("R","b9","3","5","13"), "order": 60},

            {"scale": "Cb Major b2",
             "notes": ("Cb","Dbb","Eb","Gb","Ab"),
             "tensions": ("#9","3","5","b7","R"), "order": 70},

            {"scale": "E Major b2",
             "notes": ("E","F","G#","B","C#"),
             "tensions": ("#11","5","b7","b9","#9"), "order": 80},

            {"scale": "F Major b2",
             "notes": ("F","Gb","A","C","D"),
             "tensions": ("13","b7","b9","3","#11"), "order": 90},
        ]},
    ],

    "Ab7#11": [
        {"notes": ("Ab","C","Eb","Gb","D")},
        {"scales": [
            {"scale": "Eb Whole Tone",
             "notes": ("Eb","G","A","B","Db"),
             "tensions": ("5","b7","R","9","3"), "order": 10},

            {"scale": "Bb Major b6",
             "notes": ("G","Bb","C","D","F"),
             "tensions": ("b7","9","3","#11","5"), "order": 20},

            {"scale": "F minor 6",
             "notes": ("F","Ab","Bb","C","D"),
             "tensions": ("13","R","9","3","#11"), "order": 30},
        ]},
    ],

    "Ab7b9sus": [
        {"notes": ("Ab","Db","Eb","Gb","A")},
        {"scales": [
            {"scale": "Gb minor 6",
             "notes": ("Gb","Bbb","Cb","Db","Eb"),
             "tensions": ("b7","b9","#9","11","13"), "order": 20},
        ]},
    ],

    "Ab7nat9b13": [
        {"notes": ("Ab","C","Eb","Gb","Bb","Ebb")},
        {"scales": [
            {"scale": "C Whole Tone",
             "notes": ("C","E","F#","G#","B"),
             "tensions": ("3","b13","7","R","9"), "order": 10},
        ]},
    ],

    "Ab7alt": [
        {"notes": ("Ab","C","Ebb","E","Gb","A","Bb")},
        {"scales": [
            {"scale": "Ab Whole Tone",
             "notes": ("Ab","C","D","E","Gb"),
             "tensions": ("R","3","#11","#5","b7"), "order": 10},

            {"scale": "E Major b6",
             "notes": ("C","E","F#","G#","B"),
             "tensions": ("3","#5","b7","R","#9"), "order": 20},

            {"scale": "Bb minor 6",
             "notes": ("Bb","Db","Eb","F","G"),
             "tensions": ("b9","3","b5","#5","7"), "order": 30},

            {"scale": "C minor",
             "notes": ("C","Eb","F","G","Bb"),
             "tensions": ("#9","b5","#5","b7","b9"), "order": 40},

            {"scale": "C minor 6",
             "notes": ("C","Eb","F","G","A"),
             "tensions": ("#9","b5","#5","b7","R"), "order": 50},

            {"scale": "Gb minor 7b5",
             "notes": ("Gb","Bbb","Cb","Db","Fb"),
             "tensions": ("b7","b9","#9","b5","#5"), "order": 60},
        ]},
    ],

    # A
    "AMaj7": [
        {"notes": ("A","C#","E","G#")},
        {"scales": [
            {"scale": "F# minor",
             "notes": ("F#","A","C#","D","E"),
             "tensions": ("13","R","3","11","5"), "order": 10},

            {"scale": "C# minor",
             "notes": ("C#","E","F#","G#","B"),
             "tensions": ("3","5","13","7","9"), "order": 20},

            {"scale": "G# minor",
             "notes": ("G#","B","C#","D#","F#"),
             "tensions": ("7","9","3","#11","13"), "order": 30},
        ]},
    ],

    "AMaj7#11": [
        {"notes": ("A","C#","E","G#","D#")},
        {"scales": [
            {"scale": "F# minor 6",
             "notes": ("F#","A","B","C#","D#"),
             "tensions": ("13","R","9","3","#11"), "order": 10},

            {"scale": "C# minor",
             "notes": ("C#","E","F#","G#","B"),
             "tensions": ("7","9","3","#11","13"), "order": 20},

            {"scale": "D# Whole Tone",
             "notes": ("D#","F##","G##","A##","C#"),
             "tensions": ("#11","7","R","9","3"), "order": 30},
        ]},
    ],

    "AMaj7#5": [
        {"notes": ("A","C#","E#","G#")},
        {"scales": [
            {"scale": "C# Major b6",
             "notes": ("A","C#","D#","E#","G#"),
             "tensions": ("R","3","#11","#5","7"), "order": 10},

            {"scale": "G# minor 6",
             "notes": ("G#","B","C#","D#","E#"),
             "tensions": ("7","9","3","#11","#5"), "order": 20},
        ]},
    ],

    "AMaj7b5": [
        {"notes": ("A","C#","Eb","G#")},
        {"scales": [
            {"scale": "Eb minor 7b5",
             "notes": ("Eb","Gb","Ab","Bbb","Db"),
             "tensions": ("b5","13","7","R","3"), "order": 10},
        ]},
    ],

    "Amin7": [
        {"notes": ("A","C","E","G")},
        {"scales": [
            {"scale": "A minor",
             "notes": ("A","C","D","E","G"),
             "tensions": ("R","b3","11","5","b7"), "order": 10},

            {"scale": "E minor",
             "notes": ("E","G","A","B","D"),
             "tensions": ("5","b7","R","9","11"), "order": 20},

            {"scale": "B minor",
             "notes": ("B","D","E","F#","A"),
             "tensions": ("9","11","5","13","R"), "order": 30},

            {"scale": "G minor",
             "notes": ("G","Bb","C","D","F"),
             "tensions": ("b7","b9","b3","11","13"), "order": 40},
        ]},
    ],

    "Amin6": [
        {"notes": ("A","C","E","F#")},
        {"scales": [
            {"scale": "A minor 6",
             "notes": ("A","C","D","E","F#"),
             "tensions": ("R","b3","11","5","13"), "order": 10},

            {"scale": "F# minor 7b5",
             "notes": ("F#","A","B","C","E"),
             "tensions": ("13","R","9","b3","5"), "order": 20},
        ]},
    ],

    "Amin/Maj7": [
        {"notes": ("A","C","E","G#")},
        {"scales": [
            {"scale": "E Major b6",
             "notes": ("C","E","F#","G#","B"),
             "tensions": ("b3","5","13","7","9"), "order": 10},

            {"scale": "G# Whole Tone",
             "notes": ("G#","B#","C##","E","F#"),
             "tensions": ("7","b3","11","5","13"), "order": 20},
        ]},
    ],

    "Amin7b5": [
        {"notes": ("A","C","Eb","G")},
        {"scales": [
            {"scale": "C minor 6",
             "notes": ("C","Eb","F","G","A"),
             "tensions": ("b3","5","13","b7","R"), "order": 10},

            {"scale": "A minor 7b5",
             "notes": ("A","C","D","Eb","G"),
             "tensions": ("R","b3","11","b5","b7"), "order": 20},

            {"scale": "D minor",
             "notes": ("D","F","G","A","C"),
             "tensions": ("11","13","b7","R","b3"), "order": 30},
        ]},
    ],

    "Amin7b5nat9": [
        {"notes": ("A","C","Eb","G","B")},
        {"scales": [
            {"scale": "F Major b6",
             "notes": ("D","F","G","A","C"),
             "tensions": ("b5","b7","R","9","11"), "order": 10},
        ]},
    ],

    "A7": [
        {"notes": ("A","C#","E","G")},
        {"scales": [
            {"scale": "E minor 6",
             "notes": ("E","G","A","B","C#"),
             "tensions": ("5","b7","R","9","3"), "order": 10},

            {"scale": "B minor",
             "notes": ("B","D","E","F#","A"),
             "tensions": ("9","11","5","13","R"), "order": 20},

            {"scale": "F# minor",
             "notes": ("F#","A","B","C#","E"),
             "tensions": ("13","R","9","3","5"), "order": 30},

            {"scale": "C# minor 7b5",
             "notes": ("C#","E","F#","G","B"),
             "tensions": ("3","5","13","b7","9"), "order": 40},

            {"scale": "G minor",
             "notes": ("G","Bb","C","D","F"),
             "tensions": ("#9","b5","#5","b7","b9"), "order": 50},

            {"scale": "A Major b2",
             "notes": ("A","Bb","C#","E","F#"),
             "tensions": ("R","b9","3","5","13"), "order": 60},

            {"scale": "C Major b2",
             "notes": ("C","Db","E","G","A"),
             "tensions": ("#9","3","5","b7","R"), "order": 70},

            {"scale": "F## Major b2",
             "notes": ("F##","G#","A##","C##","D##"),
             "tensions": ("#11","5","b7","b9","#9"), "order": 80},

            {"scale": "B Major b2",
             "notes": ("B","C","D#","F#","G#"),
             "tensions": ("13","b7","b9","3","#11"), "order": 90},
        ]},
    ],

    "A7#11": [
        {"notes": ("A","C#","E","G","D#")},
        {"scales": [
            {"scale": "E Whole Tone",
             "notes": ("E","G#","A#","B#","D"),
             "tensions": ("5","b7","R","9","3"), "order": 10},

            {"scale": "B Major b6",
             "notes": ("G#","B","C#","D#","F#"),
             "tensions": ("b7","9","3","#11","5"), "order": 20},

            {"scale": "F# minor 6",
             "notes": ("F#","A","B","C#","D#"),
             "tensions": ("13","R","9","3","#11"), "order": 30},
        ]},
    ],

    "A7b9sus": [
        {"notes": ("A","D","E","G","Bb")},
        {"scales": [
            {"scale": "G minor 6",
             "notes": ("G","Bb","C","D","E"),
             "tensions": ("b7","b9","#9","11","13"), "order": 20},
        ]},
    ],

    "A7nat9b13": [
        {"notes": ("A","C#","E","G","B","F")},
        {"scales": [
            {"scale": "C# Whole Tone",
             "notes": ("C#","E","F#","G#","B"),
             "tensions": ("3","b13","b7","R","9"), "order": 10},
        ]},
    ],

    "A7alt": [
        {"notes": ("A","C#","Eb","E#","G","Bb","B")},
        {"scales": [
            {"scale": "A Whole Tone",
             "notes": ("A","C#","D#","F","G"),
             "tensions": ("R","3","#11","#5","b7"), "order": 10},

            {"scale": "F Major b6",
             "notes": ("C","F","G","A","B"),
             "tensions": ("3","#5","b7","R","#9"), "order": 20},

            {"scale": "G minor 6",
             "notes": ("G","Bb","C","D","E"),
             "tensions": ("b9","3","b5","#5","b7"), "order": 30},

            {"scale": "A minor",
             "notes": ("A","C","D","E","G"),
             "tensions": ("#9","b5","#5","b7","b9"), "order": 40},

            {"scale": "A minor 6",
             "notes": ("A","C","D","E","F#"),
             "tensions": ("#9","b5","#5","b7","R"), "order": 50},

            {"scale": "E minor 7b5",
             "notes": ("E","G","A","Bb","D"),
             "tensions": ("b7","b9","#9","b5","#5"), "order": 60},
        ]},
    ],

    # Bb
    "BbMaj7": [
        {"notes": ("Bb","D","F","A")},
        {"scales": [
            {"scale": "G minor",
             "notes": ("G","Bb","D","Eb","F"),
             "tensions": ("13","R","3","11","5"), "order": 10},

            {"scale": "D minor",
             "notes": ("D","F","G","A","C"),
             "tensions": ("3","5","13","7","9"), "order": 20},

            {"scale": "A minor",
             "notes": ("A","C","D","E","G"),
             "tensions": ("7","9","3","#11","13"), "order": 30},
        ]},
    ],

    "BbMaj7#11": [
        {"notes": ("Bb","D","F","A","E")},
        {"scales": [
            {"scale": "G minor 6",
             "notes": ("G","Bb","C","D","E"),
             "tensions": ("13","R","9","3","#11"), "order": 10},

            {"scale": "D minor",
             "notes": ("D","F","G","A","C"),
             "tensions": ("7","9","3","#11","13"), "order": 20},

            {"scale": "E Whole Tone",
             "notes": ("E","G#","A#","C","D"),
             "tensions": ("#11","7","R","9","3"), "order": 30},
        ]},
    ],

    "BbMaj7#5": [
        {"notes": ("Bb","D","F#","A")},
        {"scales": [
            {"scale": "D Major b6",
             "notes": ("Bb","D","E","F#","A"),
             "tensions": ("R","3","#11","#5","7"), "order": 10},

            {"scale": "A minor 6",
             "notes": ("A","C","D","E","F#"),
             "tensions": ("7","9","3","#11","#5"), "order": 20},
        ]},
    ],

    "BbMaj7b5": [
        {"notes": ("Bb","D","Fb","A")},
        {"scales": [
            {"scale": "Fb minor 7b5",
             "notes": ("Fb","Abb","Bbb","Cb","Ebb"),
             "tensions": ("b5","13","7","R","3"), "order": 10},
        ]},
    ],

    "Bbmin7": [
        {"notes": ("Bb","Db","F","Ab")},
        {"scales": [
            {"scale": "Bb minor",
             "notes": ("Bb","Db","Eb","F","Ab"),
             "tensions": ("R","b3","11","5","b7"), "order": 10},

            {"scale": "F minor",
             "notes": ("F","Ab","Bb","C","Eb"),
             "tensions": ("5","b7","R","9","11"), "order": 20},

            {"scale": "C minor",
             "notes": ("C","Eb","F","G","Bb"),
             "tensions": ("9","11","5","13","R"), "order": 30},

            {"scale": "Ab minor",
             "notes": ("Ab","Cb","Db","Eb","Gb"),
             "tensions": ("b7","b9","b3","11","13"), "order": 40},
        ]},
    ],

    "Bbmin6": [
        {"notes": ("Bb","Db","F","G")},
        {"scales": [
            {"scale": "Bb minor 6",
             "notes": ("Bb","Db","Eb","F","G"),
             "tensions": ("R","b3","11","5","13"), "order": 10},

            {"scale": "G minor 7b5",
             "notes": ("G","Bb","C","Db","F"),
             "tensions": ("13","R","9","b3","5"), "order": 20},
        ]},
    ],

    "Bbmin/Maj7": [
        {"notes": ("Bb","Db","F","A")},
        {"scales": [
            {"scale": "F Major b6",
             "notes": ("Db","F","G","A","C"),
             "tensions": ("b3","5","13","7","9"), "order": 10},

            {"scale": "A Whole Tone",
             "notes": ("A","C#","D#","F","G"),
             "tensions": ("7","b3","11","5","13"), "order": 20},
        ]},
    ],

    "Bbmin7b5": [
        {"notes": ("Bb","Db","Fb","Ab")},
        {"scales": [
            {"scale": "Db minor 6",
             "notes": ("Db","Fb","Gb","Ab","Bb"),
             "tensions": ("b3","5","13","b7","R"), "order": 10},

            {"scale": "Bb minor 7b5",
             "notes": ("Bb","Db","Eb","Fb","Ab"),
             "tensions": ("R","b3","11","b5","b7"), "order": 20},

            {"scale": "Eb minor",
             "notes": ("Eb","Gb","Ab","Bb","Db"),
             "tensions": ("11","13","b7","R","b3"), "order": 30},
        ]},
    ],

    "Bbmin7b5nat9": [
        {"notes": ("Bb","Db","Fb","Ab","C")},
        {"scales": [
            {"scale": "G Major b6",
             "notes": ("E","G","A","B","D"),
             "tensions": ("b5","b7","R","9","11"), "order": 10},
        ]},
    ],

    "Bb7": [
        {"notes": ("Bb","D","F","Ab")},
        {"scales": [
            {"scale": "F minor 6",
             "notes": ("F","Ab","Bb","C","D"),
             "tensions": ("5","b7","R","9","3"), "order": 10},

            {"scale": "C minor",
             "notes": ("C","Eb","F","G","Bb"),
             "tensions": ("9","11","5","13","R"), "order": 20},

            {"scale": "G minor",
             "notes": ("G","Bb","C","D","F"),
             "tensions": ("13","R","9","3","5"), "order": 30},

            {"scale": "D minor 7b5",
             "notes": ("D","F","G","Ab","C"),
             "tensions": ("3","5","13","b7","9"), "order": 40},

            {"scale": "Ab minor",
             "notes": ("Ab","Cb","Db","Eb","Gb"),
             "tensions": ("#9","b5","#5","b7","b9"), "order": 50},

            {"scale": "Bb Major b2",
             "notes": ("Bb","Cb","D","F","G"),
             "tensions": ("R","b9","3","5","13"), "order": 60},

            {"scale": "Db Major b2",
             "notes": ("Db","Ebb","Gb","Bb","C"),
             "tensions": ("#9","3","5","b7","R"), "order": 70},

            {"scale": "E Major b2",
             "notes": ("E","F","G#","B","C#"),
             "tensions": ("#11","5","b7","b9","#9"), "order": 80},

            {"scale": "G Major b2",
             "notes": ("G","Ab","B","D","E"),
             "tensions": ("13","b7","b9","3","#11"), "order": 90},
        ]},
    ],

    "Bb7#11": [
        {"notes": ("Bb","D","F","Ab","E")},
        {"scales": [
            {"scale": "F Whole Tone",
             "notes": ("F","A","B","C#","Eb"),
             "tensions": ("5","b7","R","9","3"), "order": 10},

            {"scale": "C Major b6",
             "notes": ("A","C","D","E","G"),
             "tensions": ("b7","9","3","#11","5"), "order": 20},

            {"scale": "G minor 6",
             "notes": ("G","Bb","C","D","E"),
             "tensions": ("13","R","9","3","#11"), "order": 30},
        ]},
    ],

    "Bb7b9sus": [
        {"notes": ("Bb","Eb","F","Ab","Bbb")},
        {"scales": [
            {"scale": "Ab minor 6",
             "notes": ("Ab","Cb","Db","Eb","F"),
             "tensions": ("b7","b9","#9","11","13"), "order": 20},
        ]},
    ],

    "Bb7nat9b13": [
        {"notes": ("Bb","D","F","Ab","C","Gb")},
        {"scales": [
            {"scale": "D Whole Tone",
             "notes": ("D","F#","G#","A#","C"),
             "tensions": ("3","b13","7","R","9"), "order": 10},
        ]},
    ],

    "Bb7alt": [
        {"notes": ("Bb","D","Fb","F#","Ab","Bbb","B")},
        {"scales": [
            {"scale": "Bb Whole Tone",
             "notes": ("Bb","D","E","F#","Ab"),
             "tensions": ("R","3","#11","#5","b7"), "order": 10},

            {"scale": "F Major b6",
             "notes": ("D","F","G","A","B"),
             "tensions": ("3","#5","b7","R","#9"), "order": 20},

            {"scale": "Ab minor 6",
             "notes": ("Ab","Cb","Db","Eb","F"),
             "tensions": ("b9","3","b5","#5","b7"), "order": 30},

            {"scale": "Bb minor",
             "notes": ("Bb","Db","Eb","F","Ab"),
             "tensions": ("#9","b5","#5","b7","b9"), "order": 40},

            {"scale": "Bb minor 6",
             "notes": ("Bb","Db","Eb","F","G"),
             "tensions": ("#9","b5","#5","b7","R"), "order": 50},

            {"scale": "Eb minor 7b5",
             "notes": ("Eb","Gb","Ab","Bbb","Db"),
             "tensions": ("b7","b9","#9","b5","#5"), "order": 60},
        ]},
    ],

    # B
    "BMaj7": [
        {"notes": ("B","D#","F#","A#")},
        {"scales": [
            {"scale": "G# minor",
             "notes": ("G#","B","D#","E","F#"),
             "tensions": ("13","R","3","11","5"), "order": 10},

            {"scale": "D# minor",
             "notes": ("D#","F#","G#","A#","C#"),
             "tensions": ("3","5","13","7","9"), "order": 20},

            {"scale": "A# minor",
             "notes": ("A#","C#","D#","E#","G#"),
             "tensions": ("7","9","3","#11","13"), "order": 30},
        ]},
    ],

    "BMaj7#11": [
        {"notes": ("B","D#","F#","A#","E#")},
        {"scales": [
            {"scale": "G# minor 6",
             "notes": ("G#","B","C#","D#","E#"),
             "tensions": ("13","R","9","3","#11"), "order": 10},

            {"scale": "D# minor",
             "notes": ("D#","F#","G#","A#","C#"),
             "tensions": ("7","9","3","#11","13"), "order": 20},

            {"scale": "E# Whole Tone",
             "notes": ("E#","G##","A##","C##","D##"),
             "tensions": ("#11","7","R","9","3"), "order": 30},
        ]},
    ],

    "BMaj7#5": [
        {"notes": ("B","D#","Fx","A#")},
        {"scales": [
            {"scale": "D# Major b6",
             "notes": ("B","D#","E#","Fx","A#"),
             "tensions": ("R","3","#11","#5","7"), "order": 10},

            {"scale": "A# minor 6",
             "notes": ("A#","C#","D#","E#","Fx"),
             "tensions": ("7","9","3","#11","#5"), "order": 20},
        ]},
    ],

    "BMaj7b5": [
        {"notes": ("B","D#","F","A#")},
        {"scales": [
            {"scale": "F minor 7b5",
             "notes": ("F","Ab","Bbb","Cb","Eb"),
             "tensions": ("b5","13","7","R","3"), "order": 10},
        ]},
    ],

    "Bmin7": [
        {"notes": ("B","D","F#","A")},
        {"scales": [
            {"scale": "B minor",
             "notes": ("B","D","E","F#","A"),
             "tensions": ("R","b3","11","5","b7"), "order": 10},

            {"scale": "F# minor",
             "notes": ("F#","A","B","C#","E"),
             "tensions": ("5","b7","R","9","11"), "order": 20},

            {"scale": "C# minor",
             "notes": ("C#","E","F#","G#","B"),
             "tensions": ("9","11","5","13","R"), "order": 30},

            {"scale": "A minor",
             "notes": ("A","C","D","E","G"),
             "tensions": ("b7","b9","b3","11","13"), "order": 40},
        ]},
    ],

    "Bmin6": [
        {"notes": ("B","D","F#","G#")},
        {"scales": [
            {"scale": "B minor 6",
             "notes": ("B","D","E","F#","G#"),
             "tensions": ("R","b3","11","5","13"), "order": 10},

            {"scale": "G# minor 7b5",
             "notes": ("G#","B","C#","D","F#"),
             "tensions": ("13","R","9","b3","5"), "order": 20},
        ]},
    ],

    "Bmin/Maj7": [
        {"notes": ("B","D","F#","A#")},
        {"scales": [
            {"scale": "F# Major b6",
             "notes": ("D","F#","G#","A#","C#"),
             "tensions": ("b3","5","13","7","9"), "order": 10},

            {"scale": "A# Whole Tone",
             "notes": ("A#","C##","D##","F","G"),
             "tensions": ("7","b3","11","5","13"), "order": 20},
        ]},
    ],

    "Bmin7b5": [
        {"notes": ("B","D","F","A")},
        {"scales": [
            {"scale": "D minor 6",
             "notes": ("D","F","G","A","B"),
             "tensions": ("b3","5","13","b7","R"), "order": 10},

            {"scale": "B minor 7b5",
             "notes": ("B","D","E","F","A"),
             "tensions": ("R","b3","11","b5","b7"), "order": 20},

            {"scale": "E minor",
             "notes": ("E","G","A","B","D"),
             "tensions": ("11","13","b7","R","b3"), "order": 30},
        ]},
    ],

    "Bmin7b5nat9": [
        {"notes": ("B","D","F","A","C#")},
        {"scales": [
            {"scale": "G Major b6",
             "notes": ("E","G","A","B","D"),
             "tensions": ("b5","b7","R","9","11"), "order": 10},
        ]},
    ],

    "B7": [
        {"notes": ("B","D#","F#","A")},
        {"scales": [
            {"scale": "F# minor 6",
             "notes": ("F#","A","B","C#","D#"),
             "tensions": ("5","b7","R","9","3"), "order": 10},

            {"scale": "C# minor",
             "notes": ("C#","E","F#","G#","B"),
             "tensions": ("9","11","5","13","R"), "order": 20},

            {"scale": "G# minor",
             "notes": ("G#","B","C#","D#","F#"),
             "tensions": ("13","R","9","3","5"), "order": 30},

            {"scale": "D# minor 7b5",
             "notes": ("D#","F#","G#","A","C#"),
             "tensions": ("3","5","13","b7","9"), "order": 40},

            {"scale": "A minor",
             "notes": ("A","C","D","E","G"),
             "tensions": ("#9","b5","#5","b7","b9"), "order": 50},

            {"scale": "B Major b2",
             "notes": ("B","C","D#","F#","G#"),
             "tensions": ("R","b9","3","5","13"), "order": 60},

            {"scale": "D Major b2",
             "notes": ("D","Eb","F#","A","B"),
             "tensions": ("#9","3","5","b7","R"), "order": 70},

            {"scale": "G Major b2",
             "notes": ("G","Ab","B","D","E"),
             "tensions": ("#11","5","b7","b9","#9"), "order": 80},

            {"scale": "A Major b2",
             "notes": ("A","Bb","C#","E","F#"),
             "tensions": ("13","b7","b9","3","#11"), "order": 90},
        ]},
    ],

    "B7#11": [
        {"notes": ("B","D#","F#","A","E#")},
        {"scales": [
            {"scale": "F# Whole Tone",
             "notes": ("F#","A#","B#","D","E"),
             "tensions": ("5","b7","R","9","3"), "order": 10},

            {"scale": "C# Major b6",
             "notes": ("A#","C#","D#","E#","G#"),
             "tensions": ("b7","9","3","#11","5"), "order": 20},

            {"scale": "G# minor 6",
             "notes": ("G#","B","C#","D#","E#"),
             "tensions": ("13","R","9","3","#11"), "order": 30},
        ]},
    ],

    "B7b9sus": [
        {"notes": ("B","E","F#","A","C")},
        {"scales": [
            {"scale": "A minor 6",
             "notes": ("A","C","D","E","F#"),
             "tensions": ("b7","b9","#9","11","13"), "order": 20},
        ]},
    ],

    "B7nat9b13": [
        {"notes": ("B","D#","F#","A","C#","G")},
        {"scales": [
            {"scale": "D# Whole Tone",
             "notes": ("D#","F##","G##","A##","C#"),
             "tensions": ("3","b13","7","R","9"), "order": 10},
        ]},
    ],

    "B7alt": [
        {"notes": ("B","D#","F","F##","A","C","C#")},
        {"scales": [
            {"scale": "B Whole Tone",
             "notes": ("B","D#","E#","F##","A#"),
             "tensions": ("R","3","#11","#5","b7"), "order": 10},

            {"scale": "G Major b6",
             "notes": ("D#","G","A","B","C#"),
             "tensions": ("3","#5","b7","R","#9"), "order": 20},

            {"scale": "A minor 6",
             "notes": ("A","C","D","E","F#"),
             "tensions": ("b9","3","b5","#5","b7"), "order": 30},

            {"scale": "B minor",
             "notes": ("B","D","E","F#","A"),
             "tensions": ("#9","b5","#5","b7","b9"), "order": 40},

            {"scale": "B minor 6",
             "notes": ("B","D","E","F#","G#"),
             "tensions": ("#9","b5","#5","b7","R"), "order": 50},

            {"scale": "F# minor 7b5",
             "notes": ("F#","A","B","C","E"),
             "tensions": ("b7","b9","#9","b5","#5"), "order": 60},
        ]},
    ],
}
