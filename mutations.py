#produces a sequence with an insertion mutation at the given position
import random

def insertion(sequence: str, position: int) -> str:
    bases = ['g', 'c', 't', 'a']

    new_base = random.choice(bases)

    sequence = sequence[:position] + new_base + sequence[position:] 
        
    return sequence


def deletion(sequence: str, position: int) -> str:

    sequence = sequence[:position] + sequence[position+1:] 
        
    return sequence


def mismatch(sequence: str, position: int) -> str:

    bases = ['g', 'c', 't', 'a']

    while True:
        new_base = random.choice(bases)

        try:
            if new_base != sequence[position]:
                break
        except IndexError as e:
            print(sequence[position])
            print(e)

    sequence = list(sequence)

    sequence[position] = new_base

    return ''.join(sequence)



