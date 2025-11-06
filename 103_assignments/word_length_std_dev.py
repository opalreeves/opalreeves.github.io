def word_length_std_dev(text):
    words = text.split()
    lengths = [len(word) for word in words]
    N = len(lengths)
    if N < 2:
        return 0
    mean = sum(lengths) / N
    squared_diffs = [(length - mean) ** 2 for length in lengths]
    s = (sum(squared_diffs) / (N-1)) ** 0.5
    return s

#tests
#text = "A by few hour shows should"
#print(word_length_std_dev(text))

