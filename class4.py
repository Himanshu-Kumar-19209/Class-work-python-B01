
import matplotlib.pyplot as plt
import math
def binomial_pmf(n, p, k):
    return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
def plot_binomial(n_values, p_values, x_range):
    for n in n_values:
        for p in p_values:
            y_values = [binomial_pmf(n, p, x) for x in x_range]
            plt.plot(x_range, y_values, label=f'n={n}, p={p}')
    plt.title("Binomial Distribution PMF")
    plt.xlabel('Successes (k)')
    plt.ylabel('Probability')
    plt.legend()
    plt.show()
n_values = [22, 28]
p_values = [0., 0.7, 0.3]
x_range = range(21)
plot_binomial(n_values, p_values, x_range)
