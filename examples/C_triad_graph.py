"""Example of chord graph creation."""

from music21.scale import MajorScale
from numpy import inf
from numpy import linalg as la
from orbichord.chordinate import EfficientVoiceLeading
from orbichord.graph import createGraph, convertGraphToData
from orbichord.generator import Generator
from orbichord.symbol import chordSymbolFigure

scale = MajorScale('C')

chord_generator = Generator(
    pitches = scale.getPitches('C','B'),
    select = lambda chord: chord.isTriad()
)

max_norm_vl = EfficientVoiceLeading(
    scale = scale,
    metric = lambda delta: la.norm(delta, inf)
)

graph, _ = createGraph(
    generator = chord_generator,
    voice_leading = max_norm_vl,
    tolerance = lambda x: x == 1.0,
    label = lambda chord: chordSymbolFigure(chord, inversion=0)
)

for node, neighbors in graph.adjacency():
    string = node + ': '
    for neighbor, edge in neighbors.items():
        string = string + ' {} ({}),'.format(
            neighbor, edge['distance']
        )
    print(string[:-1])
