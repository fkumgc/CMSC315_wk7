# Unit 7: Sorting Algorithms

## Overview

This assignment compared Bubble Sort and Merge Sort through a streaming-content recommendation application.

## Learning Objectives

- Implemented stable Bubble Sort
- Implemented recursive Merge Sort
- Applied divide-and-conquer
- Compared time and space efficiency
- Evaluated stability and parallelization potential

## Requirements

1. Tested Bubble Sort and Merge Sort.
2. Used two different datasets.
3. Demonstrated six edge cases.
4. Analyzed performance using element comparisons.
5. Created a real-world streaming recommendation scenario.

## Implementation Summary

**Author: Firaz Khan**

All six TODO blocks were completed, and the original comments and prompts were preserved. Placeholder output statements were retained as comments. Bubble Sort copied the source list, compared adjacent values, and exchanged values that were out of order. Each completed pass moved the largest remaining value to its final position. An early-exit flag stopped the algorithm when a pass made no swaps.

Merge Sort copied lists of length zero or one as its recursive base case. Larger lists were divided at the midpoint and sorted recursively. The merge function compared the first unmerged value from each half, appended the smaller value, and then appended the remaining values after one side was exhausted. Both algorithms returned new lists and left their inputs unchanged.

The optional metrics dictionaries counted element comparisons in the actual implementations without changing their ordinary one-argument use. Counts were deterministic operation measurements rather than elapsed-time benchmarks. Bubble Sort used O(n²) comparisons in the average and worst cases, with an O(n) best case because of early exit. Merge Sort used O(n log n) time in the best, average, and worst cases. The implementations created output copies as required; Bubble Sort used O(n) space for its returned copy, while Merge Sort used O(n) auxiliary merging space plus O(log n) recursion depth.

Both implementations were stable. Bubble Sort exchanged only strictly out-of-order adjacent values. Merge Sort selected the left-side value when ratings were equal. These decisions preserved the original relative order of recommendations with identical ratings.

## Program Output and Testing

The starter was run and displayed only TODO messages. Dataset 1 sorted eight numeric ratings into ascending order. Dataset 2 sorted seven named content records by rating. Both algorithms preserved the original order of titles with equal ratings: Drama before News, Documentary before Comedy before Animation, and Live Sports before Season Premiere.

Tests covered empty, single-item, already-sorted, reverse-sorted, duplicate, and negative-value lists. Every result was checked against Python's `sorted` result, both algorithms were required to agree, and each source list was verified as unchanged. Additional deterministic tests covered generated lists, stability, input preservation, and the merge helper. Test code and captured output were retained separately from the submission files.

For 2,048 reverse-sorted values, Bubble Sort performed 2,096,128 element comparisons, while Merge Sort performed 11,264. These counts illustrated the difference between quadratic and O(n log n) growth for the implemented algorithms. They did not measure elapsed time, memory allocation, network transfer, or actual parallel execution.

The program was executed with Python 3. The equivalent command from this folder was:

```text
python unit7_discussion.py
```

## Real-World Interpretation

The application modeled a streaming platform that ordered recommendations by rating. Stable sorting preserved editorial or personalized order among equal-rated items. Bubble Sort remained understandable and could stop early for very small, nearly sorted personal playlists, but quadratic growth made it unsuitable for large trending lists.

Merge Sort was the stronger choice for large recommendation batches because its O(n log n) bound remained predictable for random, sorted, and reverse-sorted data. Independent halves also created opportunities for parallel work across processors or servers. A distributed implementation would still have incurred partitioning, communication, coordination, and final-merge costs, so parallel execution was not automatically faster for small inputs.

This list-based Merge Sort required additional memory for slices and merged results. A production platform could reduce copying, use an external merge strategy when data exceeded memory, and rely on the language or data-processing framework's tested stable sort. Bubble Sort would primarily remain useful for education or tiny inputs rather than a large-scale recommendation service.

## Reflection Essay

Implementing the streaming recommendation example strengthened understanding of adjacent-exchange sorting, recursive decomposition, stability, and operation-based performance analysis. Bubble Sort was easier to trace because each pass compared neighboring values. Merge Sort required more care because its base case, recursive halves, indices, and remaining values all had to cooperate correctly.

The main challenge involved preserving the order of content with identical ratings. Swapping only when the left rating was greater kept Bubble Sort stable. During merging, choosing the left record when ratings were equal kept Merge Sort stable. Named content records made this behavior visible instead of testing duplicate numbers that could not reveal reordered identities.

The scaling comparison showed why Merge Sort suited massive trending lists: 2,048 reverse-sorted values required 2,096,128 Bubble Sort comparisons but only 11,264 Merge Sort comparisons. Bubble Sort offered simpler code and early exit for small, nearly sorted playlists. Merge Sort offered predictable O(n log n) performance and parallelization potential, at the cost of additional memory and implementation complexity. Algorithm selection therefore depended on input size, existing order, memory limits, stability, and the overhead of distributing work.
