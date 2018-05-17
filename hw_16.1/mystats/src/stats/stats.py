from collections import Counter
from math import floor
import matplotlib.pyplot as plt


def mean(x):
    """Calculates mean.

    :param x: sample (iterable object with numeric values).
    :return: float -- mean of the sample.
    """
    return sum(x) / len(x)


def median(x):
    """Calculates median.

    :param x: sample (iterable object with numeric values).
    :return: float -- median of the sample.
    """
    n = len(x)
    sorted_x = sorted(x)
    mid = n // 2
    if n % 2 == 1:
        return sorted_x[mid]
    else:
        return (sorted_x[mid - 1] + sorted_x[mid]) / 2


def quantile(x, p):
    """Calculates quantile.

    :param x: sample (iterable object with numeric values).
    :param p: float from 0 to 1
    :return: float -- p-quantile.
    """
    if 0 <= p <= 1:
        p_idx = int(p * len(x))
        return sorted(x)[p_idx]
    else:
        raise ValueError('p should be between 0 and 1')


def mode(x):
    """Calculates mode.

    :param x: sample (iterable object).
    :return: the same type as elements of mode -- median of the sample.
    """
    counts = Counter(x)
    max_val = max(counts.values())
    return [k for k, count in counts.items() if count == max_val]


def data_range(x):
    """Calculates range.

    :param x: sample (iterable object with numeric values).
    :return: float -- range of the sample.
    """
    return max(x) - min(x)


def box_plot(x):
    """Plots boxplot.

    :param x: sample (iterable object with numeric values).
    :return: None
    """
    plt.boxplot(x)


def variance(x):
    """Calculates variance.

    :param x: sample (iterable object with numeric values).
    :return: float -- variance of the sample.
    """

    m = mean(x)
    return sum([(d - m) ** 2 for d in x]) / (len(x) - 1)


def std(x):
    """Calculates standard deviation.

    :param x: sample (iterable object with numeric values).
    :return: float -- standard deviation of the sample.
    """

    return variance(x) ** 0.5


def dot(x, y):
    """Calculates dot product.

    :param x: sample (iterable object with numeric values).
    :param y: sample (iterable object with numeric values).
    :return: float
    """
    if len(x) != len(y):
        raise ValueError('length mismatch')
    return sum([i * j for i, j in zip(x, y)])


def covariance(x, y):
    """Calculates covariance.

    :param x: sample (iterable object with numeric values).
    :param y: sample (iterable object with numeric values).
    :return: float
    """
    if len(x) != len(y):
        raise ValueError('length mismatch')

    m_x = mean(x)
    m_y = mean(y)
    dev_x = [i - m_x for i in x]
    dev_y = [i - m_y for i in y]
    return dot(dev_x, dev_y) / (len(x) - 1)


def correlation(x, y):
    """Calculates correlation.

    :param x: sample (iterable object with numeric values).
    :param y: sample (iterable object with numeric values).
    :return: float
    """
    if len(x) != len(y):
        raise ValueError('length mismatch')

    std_x = std(x)
    std_y = std(y)
    if std_x > 0 and std_y > 0:
        return covariance(x, y) / std_x / std_y
    return 0


def make_buckets(x, bucket_size):
    """Makes buckets.

    :param x: sample (iterable object with numeric values).
    :param bucket_size: int -- bucket_size.
    :return: counter -- amount of samples in each bucket.
    """
    return Counter([bucket_size * floor(i / bucket_size) for i in x])


def hist(x, bucket_size, title=""):
    """Plots histogram.

    :param x: sample (iterable object with numeric values).
    :param bucket_size: int -- bucket_size.
    :param title: str -- title of the plot.
    :return: None
    """
    hist_data = make_buckets(x, bucket_size)
    plt.bar(hist_data.keys(), hist_data.values(), width=bucket_size,)
    plt.title(title)
    plt.show()

