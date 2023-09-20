import random
import matplotlib.pyplot as plt
import mutations 
from collections import defaultdict, namedtuple


import mutations

INSERTION = 'insertion'
DELETION = 'deletion'
MISMATCH = 'mismatch'
SEQUENCE = 'sequence'
ERROR_PERCENTAGE = 'error percentage'

SEQUENCE_LENGTH = 100
GC_PERCENTAGE = 60
AT_PERCENTAGE = 40

Sequence_And_Errors = namedtuple('Person', ['name', 'age', 'city'])


# Create a random DNA sequence of 100 bases with a GC content of 60%. This will be used as a
# template sequence.
def create_template_sequence() -> str:

    gc_content = random.choices(['g','c'], k = int((GC_PERCENTAGE / 100) * SEQUENCE_LENGTH))
    at_content = random.choices(['a','t'], k = int((AT_PERCENTAGE / 100) * SEQUENCE_LENGTH))

    template_sequence = gc_content + at_content

    random.shuffle(template_sequence)

    return ''.join(template_sequence)

# Generate 3 sets of 100 sequences based on the template sequence with different error rates
# of 2%, 5% and 10%.
def create_mutant_sequences(template_sequence:str, error_rate:int) -> list:
    dna_positions = list(range(1, SEQUENCE_LENGTH))
    weights = [i*2 for i in range(1, SEQUENCE_LENGTH)]
    
    total_weight = sum(weights)
    normalized_weights = [weight / total_weight for weight in weights]
    
    biased_sequence = random.choices(dna_positions, weights=normalized_weights, k=error_rate)

    biased_sequence.sort()

    error_positions = set(biased_sequence)

    error_types = [INSERTION, DELETION, MISMATCH]

    error_types_and_locations = defaultdict(list)

    for position in error_positions:

        mutation_type = random.choice(error_types)

        if mutation_type == INSERTION:
            template_sequence = mutations.insertion(template_sequence, position)
        
        if mutation_type == DELETION:
            template_sequence = mutations.deletion(template_sequence, position)

        if mutation_type == MISMATCH:
            template_sequence = mutations.mismatch(template_sequence, position)
        

        error_types_and_locations[mutation_type].append(position)

    # Keep track of the positions and type of errors and plot error position distribution per
    # error type.
    error_types = list(error_types_and_locations.keys())
    fig, ax = plt.subplots()

    colors = ['red', 'blue', 'green', 'yellow']  # You can customize these colors

    for i, error_type in enumerate(error_types):
        positions = error_types_and_locations[error_type]
        
        ax.hist(positions, bins=20, edgecolor='k', alpha=0.7, color=colors[i], label=error_type)

    plt.xlabel('Error Position')
    plt.ylabel('Frequency')
    plt.title('Distribution of error types for error rate ' + str(error_rate))
    
    ax.legend()
 
    plt.show()

    return (error_rate, template_sequence, error_types_and_locations)

# Plot one figure to show the sequence length distribution per error rate.
def plot_sequence_length_distribution(sequences_and_errors: list):

    error_counts = []
    sequence_names = []

    for data in sequences_and_errors:

        error_rate = data[0]
        sequence = data[1]

        error_counts.append(len(sequence))
        sequence_names.append(error_rate)



    plt.bar(range(len(error_counts)), error_counts, tick_label=sequence_names)
    plt.xlabel('Error rate of Sequence')
    plt.ylabel('Length')
    # I'm a little unsure about this being a log scale, but the difference isn't really easy to see with a normal scale...
    plt.yscale('log')
    plt.title('Sequence Length Distribution per Error Rate')
    plt.show()

# Plot one figure to show the GC content per error rate.
def plot_gc_content(sequences_and_errors: list):

    gc_contents = []

    sequence_names = []

    for data in sequences_and_errors:

        error_rate = data[0]
        sequence = data[1]

        g_count = sequence.count('g')
        c_count = sequence.count('c')

        gc_total = g_count + c_count

        gc_content = (gc_total / len(sequence)) * 100
        
        gc_contents.append(gc_content)

        sequence_names.append(error_rate)


    plt.bar(range(len(gc_contents)), gc_contents,tick_label=sequence_names)
    plt.xlabel('Error rate of Sequence')
    plt.ylabel('GC Content (%)')
    plt.title('GC Content of Sequences')
    plt.show()


if __name__ == '__main__':
    seq = create_template_sequence()

    two_percent = create_mutant_sequences(seq, 2)
    five_percent = create_mutant_sequences(seq, 5)
    ten_percent = create_mutant_sequences(seq, 10)
    
    plot_sequence_length_distribution([two_percent, five_percent, ten_percent])


    plot_gc_content([two_percent, five_percent, ten_percent])