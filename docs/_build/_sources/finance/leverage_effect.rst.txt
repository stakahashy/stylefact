Leverage Effect
_______________

Description
^^^^^^^^^^^

The leverage effects refer to the tendency that past price return has the negative correlation with future volatility :cite:`Bouchaud_2001`.
According to :cite:`Bouchaud_2001,Qiu_2006`, this statistical property is quantified by the following lead-lag correlation function 

.. math::
   :nowrap:
   
   \begin{equation}
      L(k)=\frac{E[r(t){|r(t+k)|}^{2}-r(t){|r(t)|}^{2}]}{E[|r(t)|^{2}]^{2}}.
   \end{equation}

In contrast to other statistical properties, this property is market dependent according to :cite:`Qiu_2006`
While the negative correlation (leverage effect) is observed in German DAX, the positive correlation (so-called anti-leverage effect) is detected in Chinese markets.

.. image:: ../images/lev_averaged.png
   :width: 400
   :align: center

.. centered::
   Fig. Averaged result for S&P500 firms daily price return


Code Example
^^^^^^^^^^^^

.. literalinclude:: ../../examples/leverage_effect.py
   :lines: 1-3,6-
   :language: python

References
^^^^^^^^^^

.. bibliography:: refs.bib
   :filter: docname in docnames
