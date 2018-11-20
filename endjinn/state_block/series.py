import csv
import numpy as np
import scipy
import scipy.signal
from scipy.signal import savgol_filter


class Series(object):
    """
    Main class for instantiating time series state/data objects, with helper methods attached for convenience.

    Series is assumed to 1D.
    """
    def __init__(self, data=None):
        """

        :param data: Either list of ints/floats or list of tuples. If tuples, first argument is assumed to be
        timestamp and second argument

        Examples:
        series = Series([0.4, 0.5, 0.6, 0.7])
        series = Series([(1537491719, 5.1), (1537491721, 5.4), (1537491723, 4.2)])
        """
        self.index = 0
        self.format = None

        if data:
            if all([hasattr(thing, '__len__') for thing in data]):
                # Tuples of (timestamp, data)
                self.format = "tuple"
            else:
                self.format = "list"

            self.data = data

    def get_and_tick(self):
        ret = None

        if self.format == "tuple":
            ret = self.data[self.index][1]
        elif self.format == "list":
            ret = self.data[self.index]

        self.index += 1

        return ret

    def get_slice(self, start, end):
        ret = None

        if self.format == "tuple":
            ret = [thing[1] for thing in self.data[start:end]]
        elif self.format == "list":
            ret = self.data[start:end]

        return ret

    def load_from_csv(self, path, _format):
        """
        Set data from CSV file in specified path.

        If format is list, CSV should be single line with comma-separated values:
        1,5,21,5,7

        If format is tuple, CSV should be multiple lines with timestamp/date string, value in each line:
        2018-01-01,111.2
        2018-01-02,113.4
        2018-01-03,110.9

        :param path: Path of CSV file to load
        :param _format: Either 'tuple' or 'list'
        :return:
        """
        self.format = _format
        self.data = []
        row_count = 0

        with open(path, 'rb') as csvfile:
            reader = csv.reader(csvfile)
            row_count = sum(1 for row in reader)

        with open(path, 'rb') as csvfile:
            reader = csv.reader(csvfile)

            if row_count == 1:
                for row in reader:
                    self.data.append([float(thing) for thing in row])

            elif row_count > 1:
                for row in reader:
                    row[1] = float(row[1])
                    self.data.append(tuple(row))

    def get_values(self):
        ret = None

        if self.format == "tuple":
            ret = [thing[1] for thing in self.data]
        elif self.format == "list":
            ret = self.data

        return ret

    def savgol_filtered(self, window_size, poly_order=2):
        """
        Return the Savitzky-Golay filter of the data. Useful for smoothing, reducing noise.
        Read more here: https://en.wikipedia.org/wiki/Savitzky%E2%80%93Golay_filter

        :param window_size: Size of the window to run the filter over. Optimal value will vary by application and
        length of series.
        :param poly_order: Order ofthe polynomial to use in filter. Defaults to 2 (quadratic). 3 is cubic, 4 is quartic,
        and so on.
        :return: Filtered data
        """
        assert poly_order != 1

        ret = None

        if self.format == "tuple":
            ret = [thing[1] for thing in self.data]
        elif self.format == "list":
            ret = self.data

        ret = savgol_filter(ret, window_size, poly_order)

        return ret

    def get_standard_deviation(self):
        return np.std(self.get_values())

    def get_mean(self):
        return np.mean(self.get_values())

    def get_variance(self):
        return np.var(self.get_values())

    def get_dispersion_index(self):
        return self.get_variance() / self.get_mean()

    def add_value(self, val):
        """
        Append a new value to the end of the series.

        :param val: Float if scalar, tuple if (timestamp, value)
        :return:
        """
        self.data.append(val)
