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
        for i in range(len(self.fastq_records) - 1):
            for j in range(len(self.fastq_records) - i - 1):
                q1 = self.fastq_records[j].mean_quality()
                q2 = self.fastq_records[j + 1].mean_quality()

                ll1 = len(self.fastq_records[j].read_sequence)
                ll2 = len(self.fastq_records[j + 1].read_sequence)

                gc1 = self.fastq_records[j].gc()
                gc2 = self.fastq_records[j + 1].gc()

                idd1 = self.fastq_records[j].read_id
                idd2 = self.fastq_records[j + 1].read_id

                if (q1, ll1, gc1, idd1) < (q2, ll2, gc2, idd2):
                    self.fastq_records[j], self.fastq_records[j + 1] = self.fastq_records[j + 1], self.fastq_records[j]

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
