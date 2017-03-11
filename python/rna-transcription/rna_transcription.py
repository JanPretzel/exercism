DNA_TO_RNA = {
    'A': 'U',
    'G': 'C',
    'C': 'G',
    'T': 'A',
}


def to_rna(dna_strand):
    rna_strand = ''
    for ch in dna_strand:
        if ch not in DNA_TO_RNA:
            return ''
        rna_strand += DNA_TO_RNA[ch]
    return rna_strand
