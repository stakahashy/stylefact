Gain/Loss Asymmetry
___________________

Description
^^^^^^^^^^^

The gain/loss asymmetry refers to the observation that the speed of price fall is faster than that of the price rise.


.. math::
   :nowrap:

   \begin{equation}
      T^{t}(\theta) = \left\{ \begin{array}{ll}
      \inf{\{ t'| \log{p_{t+t'}}-\log{p_{t}} >=\theta,t'>0 \}} & (\theta>0) \\
      \inf{\{ t'| \log{p_{t+t'}}-\log{p_{t}} <=\theta,t'>0 \}} & (\theta<0).
      \end{array} \right.
   \end{equation}


.. image:: ../images/return_asymmetry_averaged.png
   :width: 400
   :alt: Alternative text
   :align: center


Code Example
^^^^^^^^^^^^


References
^^^^^^^^^^
1. Mogens H. Jensen, Anders Johansen, Ingve Simonsen.  Inverse Statistics in Economics : The gain-loss asymmetry. 324 (1-2) pp. 338-343  2003 
