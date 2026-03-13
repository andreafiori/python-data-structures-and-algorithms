"""
Array merge
"""
class ArrayMerge:
    """ Array merge utils """

    def merge_two_arrays(self, arr1: list[int], arr2: list[int]) -> list[int]:
        """ Merge two sorted arrays into a single sorted array """
        arr1_sorted = sorted(arr1)
        arr2_sorted = sorted(arr2)
        merged = []
        i = j = 0
        while i < len(arr1_sorted) and j < len(arr2_sorted):
            if arr1_sorted[i] < arr2_sorted[j]:
                merged.append(arr1_sorted[i])
                i += 1
            else:
                merged.append(arr2_sorted[j])
                j += 1
        # Add remaining elements
        merged.extend(arr1_sorted[i:])
        merged.extend(arr2_sorted[j:])
        return merged

    def merge_k_arrays(self, arrays: list[list[int]]) -> list[int]:
        """ Merge k sorted arrays into a single sorted array """
        if not arrays:
            return []
        while len(arrays) > 1:
            merged_arrays = []
            for i in range(0, len(arrays), 2):
                arr1 = arrays[i]
                arr2 = arrays[i + 1] if i + 1 < len(arrays) else []
                merged_arrays.append(self.merge_two_arrays(arr1, arr2))
            arrays = merged_arrays
        return arrays[0]
