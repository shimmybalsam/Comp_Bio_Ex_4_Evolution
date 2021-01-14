import numpy as np
import matplotlib.pyplot as plt

bases_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}


def one_2_a(t, a):
    same_a = 0.25 * (1 + 3 * np.exp(-4 * 0.25 * t))
    a = a.upper()
    prob = [(1 - same_a) / 3] * 4
    prob[bases_dict[a]] = same_a
    return np.random.choice(['A', 'C', 'G', 'T'], 1, p=prob)[0]


def one_2_b():
    for t in [0.15, 0.4, 1.1]:
        for N in [10, 100, 1000]:
            results = [0, 0, 0, 0]
            for i in range(N):
                results[bases_dict[one_2_a(t, 'a')]] += 1
            for j in range(len(results)):
                results[j] = results[j] / N
            print('for t = {} N = {} - {}'.format(t, N, results))


def one_3_a(t):
    a = np.random.choice(['A', 'C', 'G', 'T'])
    return a, one_2_a(t, a)


def generate_sequence(N, t):
    seq_a = ''
    seq_b = ''
    for i in range(N):
        to_append_a, to_append_b = one_3_a(t)
        seq_a += to_append_a
        seq_b += to_append_b
    return seq_a, seq_b


def estimate_t(seq_a, seq_b):
    m = 0
    n = 0
    for i in range(len(seq_a)):
        if seq_a[i] == seq_b[i]:
            m += 1
        else:
            n += 1
    return np.log(3 * m + 3 * n) - np.log(3 * m - n)


def one_3_b():
    data = []
    ts = [0.15, 0.4, 1.1]
    for t in ts:
        estimated_ts = []
        for i in range(100):
            seq_a, seq_b = generate_sequence(N=500, t=t)
            estimated_ts.append(estimate_t(seq_a, seq_b))
        data.append(estimated_ts)
    fig1, ax1 = plt.subplots()
    ax1.set_title('Estimation of Evolutionary Distance')
    ax1.boxplot(data)
    plt.xticks([i for i in range(1, len(ts) + 1)], ts)
    plt.xlabel('Real t')
    plt.ylabel('Estimated t')
    plt.show()


one_3_b()
