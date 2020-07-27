Autocorrelation
---------------

Description
^^^^^^^^^^^
The autocorrelation function :math:`C(k)` is a standard statistical tool to evaluate the temporal dependence of financial time-series.


.. math::
   :nowrap:

   \begin{equation}
      C(k) = \frac{E[(x_{t}-\mu)(x_{t+k}-\mu)]}{\sigma^{2}}
   \end{equation}

:math:`x_{t}` is the value at time-step :math:`t` and :math:`\mu` and :math:`\sigma^{2}` are the mean and variance of the time-series :math:`\{x_{t}\}`

For the price return series, it is expected that the autocorrelation value takes :math:`C(k)\approx 0` for any lag :math:`k\neq0`. It implies the linear unpredictability of financial time-series.

For the magnitude (i.e., absolute value, squared value) time-series, it is expected to observe volatility clustering,  the slow decay of the autocorrelation function.

.. image:: ../images/acf_averaged.png
   :width: 400
   :alt: Alternative text
   :align: center

.. image:: ../images/acf_abs_averaged.png
   :width: 400
   :alt: Alternative text
   :align: center

Code Example
^^^^^^^^^^^^

References
^^^^^^^^^^

