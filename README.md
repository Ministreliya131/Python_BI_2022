# FASTQ-files reader
This is the module for reading FASTQ-file

# Contents

This module have two classes **Read** and **FASTQFile** and function **read_fastq**.

## Class **Read**

### Attributes:
- **read_id**: contains the read ID from FASTQ-file without @;
- **read_sequence**: contains the sequence of read;
- **comment**: contains the comment string (the 3-rd string after read ID);
- **quality**: contains the quality string.

### Methods:
- **gc**: calculate GC-content of read;
- **mean_quality**: calculate the mean quality of read;
- **len** function was overloaded.

## Class **FASTQFile**

### Attributes:
- **fileanme**: contains the path to FASTQ-file;
- **fastq_records**: contains the list of inastances of class Read created from current FASTQ-file.

### Methods:
- **sort_reads**: sorts objects (reads) in the **fastq_records** attribute by average quality; if average quality is equal, sorting occurs by read length, if equal to length by GC-composition, with equal GC-composition lexicographically by read ID. The method returns nothing, only changes the fastq_records attribute. **It might be optimized**;
- **write_to_file**: create FASTQ-file from **fastq_records** attribute.

## Function **read_fastq**
Creates Read-objects from current FASTQ-file and one object named FASTQFile.

To create this script "test.fastq" file from **Homework 2** was used

