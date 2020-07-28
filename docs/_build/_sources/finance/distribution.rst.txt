Probability Distribution
________________________

Description
^^^^^^^^^^^

The probability distribution function of the price returns :math:`P(r_{t})` has been extensively studied in different financial markets over different time scales :cite:`Bachelier_1900,Cont_2001,Chakraborti_2011`. 
It has been empirically verified that the probability distribution :math:`P(r_{t})` consistently has a power-law decay in the tails

.. math::
   :nowrap:

   \begin{equation}
      P(r_{t})\propto r_{t}^{-\alpha}.
   \end{equation}

.. image:: ../images/pos_dist.png
   :width: 400
   :align: center

.. centered::
   Fig. Averaged result for S&P500 firms daily price return


The power-law exponent satisfies :math:`\alpha\approx3` for stock markets (i.e., S&P500, NewYork Stock Exchange...) at daily scale.

Code Example
^^^^^^^^^^^^

.. literalinclude:: ../../examples/distribution.py
   :lines: 1-3,6-
   :language: python

References
^^^^^^^^^^

.. bibliography:: refs.bib
   :filter: docname in docnames