"""
Example of generator primitives.

This example generates the space of C chords identify by
their ordered pitch class string that are also triads.
"""

from orbichord.generator import Generator
from orbichord.symbol import chordSymbolFigure
from music21.scale import MajorScale

scale = MajorScale('C')

chord_generator = Generator(
    pitches = scale.getPitches('C','B'),
    select = lambda chord: chord.isTriad()
)

for chord in chord_generator.run():
    print('{} {} - {}'.format(
        chord,
        chord.orderedPitchClassesString,
        chordSymbolFigure(chord, inversion=0)
    ))
