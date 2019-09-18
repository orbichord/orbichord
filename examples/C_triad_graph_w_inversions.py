import itertools
from music21.scale import MajorScale
from networkx import connected_components
from numpy import inf
from numpy import linalg as la
from orbichord.chordinate import VoiceLeading
from orbichord.graph import createGraph, convertGraphToData
from orbichord.generator import Generator
import orbichord.identify as identify

def combinator(iterable, dimension):
    return itertools.product(iterable, repeat = dimension)

scale = MajorScale('C')

chord_generator = Generator(
    pitches = scale.getPitches('C','B'),
    combinator = combinator,
    identify = identify.chordSymbolFigureWithPitchName,
    select = lambda chord: chord.isTriad()
)

max_norm_vl = VoiceLeading(
    scale = scale,
    metric = lambda delta: la.norm(delta, inf)
)

graph = createGraph(
    generator = chord_generator,
    voice_leading = max_norm_vl,
    tolerance = lambda x: x <= 1.0
)

for node, neighbors in graph.adjacency():
    string = node + ': '
    for neighbor, edge in neighbors.items():
        string = string + ' {} ({}),'.format(
            neighbor, edge['distance']
        )
    print(string[:-1])

good_twin, evil_twin = (graph.subgraph(c) for c in connected_components(graph))

print()
print('Evil twin graph component')

for node, neighbors in evil_twin.adjacency():
    string = node + ': '
    for neighbor, edge in neighbors.items():
        string = string + ' {} ({}),'.format(
            neighbor, edge['distance']
        )
    print(string[:-1])
