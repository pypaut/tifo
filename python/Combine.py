import itertools


def combine(r, g, b):
    matrix = []
    for (r_line, g_line, b_line) in zip(r.matrix, g.matrix, b.matrix):
        line = []
        for (r_p, g_p, b_p) in zip(r_line, g_line, b_line):
            line.append((r_p, g_p, b_p))
        matrix.append(line)
    return matrix
