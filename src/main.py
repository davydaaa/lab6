def boyer_moore_search(haystack, needle):
    def calculate_bad_char_shift(needle):
        bad_char_shift = dict()
        needle_length = len(needle)

        for i in range(needle_length - 1):
            bad_char_shift[needle[i]] = needle_length - 1 - i

        return bad_char_shift

    def boyer_moore(haystack, needle):
        needle_length = len(needle)
        haystack_length = len(haystack)
        bad_char_shift = calculate_bad_char_shift(needle)

        i = 0
        while i <= haystack_length - needle_length:
            j = needle_length - 1

            while j >= 0 and needle[j] == haystack[i + j]:
                j -= 1

            if j < 0:
                return i

            bad_char = haystack[i + j]
            if bad_char in bad_char_shift:
                i += max(1, j - bad_char_shift[bad_char])
            else:
                i += needle_length

        return -1

    indices = []
    index = boyer_moore(haystack, needle)

    while index != -1:
        indices.append(index)
        index = boyer_moore(haystack[index + 1:], needle)
        if index != -1:
            index += indices[-1] + 1

    return indices

