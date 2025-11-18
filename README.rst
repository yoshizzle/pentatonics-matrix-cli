Pentatonics Matrix Command Line Interface
=========================================

.. highlight:: python

.. image:: https://img.shields.io/github/license/Naereen/StrapDown.js.svg
   :target: https://github.com/Naereen/StrapDown.js/blob/master/LICENSE

A Command Line Interface (CLI) tool for choosing
which pentatonic scales to play over chords.


Motivation
----------

I am a lifelong musician and had always struggled to find an
effective system for learning which pentatonic scales to play
over various chords. After leaning on the
knowledge of jazz heavyweights such as Barry Greene,
Jerry Bergonzi, McCoy Tyner, and many others,
I came up with the idea of a matrix.

For those of you who may not know, a pentatonic scale is simply
a scale comprised of five distinct notes. The pentatonic scale
is widely considered one of the major cornerstones of blues,
jazz, and rock music. Dare I say it's one of *the* most significant
improvisation tools in all of music! A bold statement, for sure,
but I stand by it.

Covered in this CLI are what I consider to be the most obvious
and “important” (I use the word loosely) pentatonic scales that
you can use to improvise. Because the possibilities are literally
endless, I left out some of the more advanced concepts such as
bitonal and polytonal pentatonics. I encourage you to explore
any and all possible pentatonic combinations to enrich your
musical journey.

Lastly, of course music is subjective, so your mileage may vary as to
what scales sound good over different chords. This is intended
to be a general guide and by no means an official rulebook for
playing music. Ultimately, my goal is to help other musicians
find new and exciting ways to express themselves. I hope you
enjoy this project as much as I have enjoyed creating it.


**This project is currently in ALPHA.**


Installation
------------

Editable Install (recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clone the repository, then from the project root:

::

    pip install -e .

This will install the ``pentatonics`` command system-wide.


Running the CLI
---------------

Once installed, you can run the CLI from **any directory**:

::

    pentatonics <ChordName>

Examples:

::

    pentatonics cmaj7
    pentatonics Ab7alt
    pentatonics F#min7b5
    pentatonics Dbmaj7#11

The CLI is case-insensitive:

::

    pentatonics CMaj7
    pentatonics cMAJ7
    pentatonics Cmaj7


Showing the Help Menu
---------------------

To view usage information, simply run:

::

    pentatonics

This displays:

- Valid key centers
- Valid chord types
- Example commands
- Usage format


Usage Explanation
-----------------

For a given chord (e.g., ``Cmaj7``), the CLI displays:

- The chord tones
- A list of pentatonic scales that can be played over the chord
- Each scale’s note content
- Each scale’s tensions (their function relative to the chord root)

Example output:

::

    === cmaj7 ===
    Chord tones: C, E, G, B

    Scale                     Notes                Tensions
    --------------------------------------------------------
    a minor                   A C E F G            13, R, 3, 11, 5
    e minor                   E G A B D            3, 5, 13, 7, 9
    ...

These scales are ordered from “inside” to “outside” according
to their tension relationships.


A Note About Enharmonics
------------------------

I paid particular attention to enharmonics and avoided taking
the easy route unless musically appropriate. This was done
purposely to help demonstrate the functional relationship
between the chord and the suggested pentatonic scale.

For example, over a ``Db7alt`` chord:

It would be simpler to display an ``A Major b6`` pentatonic,
but that creates a misleading interpretation. The correct
functional choice is the Major b6 pentatonic built on the
*b6* degree of the chord—hence the naming ``Bbb Major b6`` in
the output.

Enharmonic spellings for chord roots (e.g., ``C#`` vs ``Db``)
are also supported.


Dependencies
------------

- Python >= 3.8 (recommended)
- No external dependencies
