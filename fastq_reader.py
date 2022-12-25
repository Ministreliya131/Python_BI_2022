#!/usr/bin/env python3

class Read:
    def __init__(self, read_id, read_sequence, comment, quality):
        self.read_id = read_id.lstrip("@").rstrip("\n")
        self.read_sequence = read_sequence.rstrip("\n")
        self.comment = comment.rstrip("\n")
        self.quality = quality.rstrip("\n")

    def __len__(self):
        return len(self.read_sequence)

    def gc(self):
        gc_sum = 0
        for nucl in self.read_sequence:
            if nucl == "G" or nucl == "C":
                gc_sum += 1
        gc_content = gc_sum / len(self.read_sequence) * 100

        return gc_content

    def mean_quality(self):
        q_scores_sum = 0
        for val in self.quality:
            q_scores_sum += (ord(val) - 33)

        return q_scores_sum / len(self.quality)


class FASTQFile:
    def __init__(self, path_to_file, fastq_records):
        self.filename = path_to_file
        self.fastq_records = fastq_records

    def sort_reads(self):
        sorted_reads = sorted(self.fastq_records, key= lambda x: (x.mean_quality(), x.read_sequence, x.gc(), x.read_id), reverse=True)
        return sorted_reads

    def write_to_file(self, fastq_file_name):
        with open(fastq_file_name, 'w') as fq_fle:
            for read in self.fastq_records:
                print('@' + read.read_id, file=fq_fle)
                print(read.read_sequence, file=fq_fle)
                print(read.comment, file=fq_fle)
                print(read.quality, file=fq_fle)


def read_fastq(fastq_file_name):
    with open(fastq_file_name) as fastq:
        fastq_lines = fastq.readlines()

    my_reads = []
    for ind in range(0, len(fastq_lines), 4):
        readd = Read(*fastq_lines[ind:ind + 4])
        my_reads.append(readd)

    my_fq = FASTQFile(fastq_file_name, my_reads)
    return my_fq
