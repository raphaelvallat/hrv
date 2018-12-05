# coding: utf-8
import numpy as np
from numbers import Number
from scipy import interpolate


# TODO: Refactor validation decorator
def validate_rri(func):
    def _validate(rri, *args, **kwargs):
        _validate_positive_numbers(rri)
        rri = _transform_rri(rri)
        return func(rri, *args, **kwargs)

    def _validate_positive_numbers(rri):
        if not all(map(lambda value: isinstance(value, Number) and value > 0,
                       rri)):
            raise ValueError('rri must be a list or numpy.ndarray of positive'
                             ' and non-zero numbers')

    return _validate


def _transform_rri(rri):
    rri = _transform_rri_to_miliseconds(rri)
    return np.array(rri)


# TODO: Refactor validation decorator
def validate_frequency_domain_arguments(func):
    def _check_frequency_domain_arguments(rri, fs=4.0, method='welch',
                                          interp_method='cubic', **kwargs):
        _validate_available_methods(method)
        return func(rri, fs, method, interp_method, **kwargs)

    def _validate_available_methods(method):
        available_methods = ('welch', 'ar')
        if method not in available_methods:
            raise ValueError('Method not supported! Choose among: {}'.format(
                ', '.join(available_methods)))

    return _check_frequency_domain_arguments


def _create_time_info(rri):
    rri_time = np.cumsum(rri) / 1000.0  # make it seconds
    return rri_time - rri_time[0]   # force it to start at zero


def _transform_rri_to_miliseconds(rri):
    if np.median(rri) < 1:
        rri *= 1000
    return rri


def _interpolate_rri(rri, time, fs=4, interp_method='cubic'):
    if interp_method == 'cubic':
        return _interp_cubic_spline(rri, time, fs)
    elif interp_method == 'linear':
        return _interp_linear(rri, time, fs)


def _interp_cubic_spline(rri, time, fs):
    time_rri_interp = _create_interp_time(time, fs)
    tck = interpolate.splrep(time, rri, s=0)
    rri_interp = interpolate.splev(time_rri_interp, tck, der=0)
    return rri_interp


def _interp_linear(rri, time, fs):
    time_rri_interp = _create_interp_time(time, fs)
    rri_interp = np.interp(time_rri_interp, time, rri)
    return rri_interp


def _create_interp_time(time, fs):
    time_resolution = 1 / float(fs)
    return np.arange(0, time[-1] + time_resolution, time_resolution)
