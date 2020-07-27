Coarse-Fine Volatility
----------------------

Description
^^^^^^^^^^^

The coarse-fine volatility correlation is a multi-time-scale analysis of volatility. 

.. math::
   :nowrap:

   \begin{eqnarray}
      v_{c}^{\tau}(t)&=&\bigg{|}\sum_{i=1}^{\tau}{r_{t-i}}\bigg{|}\\
      v_{f}^{\tau}(t)&=&\sum_{i=1}^{\tau}{|r_{t-i}|}.
   \end{eqnarray}

While the coarse volatility is the absolute value of the price movement in :math:`\tau` days, 
the fine volatility is the sum of the absolute price return in :math:`\tau` days. :math:`\tau=5` is starndard as it stands for day-week time-scales.

.. math::
   :nowrap:

   \begin{equation}
      \rho_{cf}^{\tau}(k)=Corr(v_{c}^{\tau}(t+k),v_{f}^{\tau}(t)).
   \end{equation}

Muller et al., Rydberg et al., and Gavrishchaka et al. reported that there exists the negative asymmetry of the lead-lag correlation quantified by the difference

.. math::
   :nowrap:
   
   \begin{equation}
      \Delta\rho_{cf}^{\tau}(k)=\rho_{cf}^{\tau}(k)-\rho_{cf}^{\tau}(-k).
   \end{equation}



.. image:: ../images/asymmetry_averaged.png
   :width: 400
   :alt: Alternative text
   :align: center

Code Example
^^^^^^^^^^^^

References
^^^^^^^^^^
