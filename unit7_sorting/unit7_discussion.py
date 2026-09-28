"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""

# Author: Firaz Khan


class RatingItem:
    """Content record whose comparisons use only the numeric rating."""

    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

    def __gt__(self, other):
        return self.rating > other.rating

    def __le__(self, other):
        return self.rating <= other.rating

    def __repr__(self):
        return f"{self.title} ({self.rating})"


def bubble_sort(lst, metrics=None):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Work on a copy so sorting does not change a caller's playlist.
    result = list(lst)
    comparisons = 0
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            comparisons += 1
            # Strict comparison preserves the order of equal-rated items.
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = (
                    result[index + 1], result[index]
                )
                swapped = True
        # An unchanged pass proves the remaining range is already sorted.
        if not swapped:
            break
    if metrics is not None:
        metrics["comparisons"] = comparisons
    return result


def merge_sort(lst, metrics=None):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Lists of length zero or one are already sorted; copy either case.
    if len(lst) <= 1:
        return list(lst)

    middle = len(lst) // 2
    # Independent halves illustrate divide-and-conquer and can be parallelized.
    left = merge_sort(lst[:middle], metrics)
    right = merge_sort(lst[middle:], metrics)
    return merge(left, right, metrics)


def merge(left, right, metrics=None):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if metrics is not None:
            metrics["comparisons"] = metrics.get("comparisons", 0) + 1
        # Taking the left item on equality makes this merge stable.
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # One side may contain an already-sorted remainder.
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


def display_comparison(label, values):
    """Run both algorithms, verify agreement, and display comparison counts."""
    original = list(values)
    bubble_metrics = {}
    merge_metrics = {"comparisons": 0}
    bubble_result = bubble_sort(values, bubble_metrics)
    merge_result = merge_sort(values, merge_metrics)
    assert values == original, "Sorting functions changed the input list"
    assert bubble_result == merge_result, "Sorting algorithms disagreed"
    print(f"{label} original: {values}")
    print(f"Bubble Sort: {bubble_result}")
    print(f"Merge Sort:  {merge_result}")
    print(f"Comparisons: Bubble={bubble_metrics['comparisons']:,}, "
          f"Merge={merge_metrics['comparisons']:,}")
    return bubble_result, merge_result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    # TODO: Create an unsorted dataset and test both sorting algorithms.
    ratings = [91, 72, 88, 65, 95, 79, 84, 70]
    expected = [65, 70, 72, 79, 84, 88, 91, 95]
    bubble_result, merge_result = display_comparison("Ratings", ratings)
    assert bubble_result == expected and merge_result == expected
    print("Both algorithms produced the same ascending rating order.")

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    # TODO: Create a second dataset and compare sorting results.
    # Equal ratings model recommendations whose original order must be retained.
    content = [
        RatingItem("Documentary", 4),
        RatingItem("Live Sports", 5),
        RatingItem("Comedy", 4),
        RatingItem("Drama", 3),
        RatingItem("Season Premiere", 5),
        RatingItem("News", 3),
        RatingItem("Animation", 4),
    ]
    bubble_result, merge_result = display_comparison("Content", content)
    expected_titles = [
        "Drama", "News", "Documentary", "Comedy", "Animation",
        "Live Sports", "Season Premiere"
    ]
    assert [item.title for item in bubble_result] == expected_titles
    assert [item.title for item in merge_result] == expected_titles
    print("Equal-rated titles retained their original relative order.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    # TODO: Demonstrate and explain edge cases.
    cases = [
        ("Empty list", []),
        ("Single item", [81]),
        ("Already sorted", [1, 2, 3, 4, 5]),
        ("Reverse sorted", [5, 4, 3, 2, 1]),
        ("Duplicate values", [4, 2, 4, 1, 2]),
        ("Negative values", [3, -1, 0, -5, 3]),
    ]
    for label, values in cases:
        bubble_result, merge_result = display_comparison(label, values)
        assert bubble_result == sorted(values)
        assert merge_result == sorted(values)

    print("\n=== SCALING COMPARISON ===")
    large_reverse = list(range(2_048, 0, -1))
    bubble_metrics = {}
    merge_metrics = {"comparisons": 0}
    assert bubble_sort(large_reverse, bubble_metrics) == sorted(large_reverse)
    assert merge_sort(large_reverse, merge_metrics) == sorted(large_reverse)
    print("Reverse-sorted values: 2,048")
    print(f"Bubble comparisons: {bubble_metrics['comparisons']:,}")
    print(f"Merge comparisons:  {merge_metrics['comparisons']:,}")
    print("Bubble Sort used quadratic comparisons; Merge Sort divided the list.")
    print("Merge Sort can process independent halves in parallel, although this")
    print("single-process demonstration did not benchmark parallel execution.")
    print("All demonstration checks passed.")




if __name__ == "__main__":
    main()
