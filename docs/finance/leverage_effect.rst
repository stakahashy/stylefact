Leverage Effect
_______________

Description
^^^^^^^^^^^

The leverage effects refer to the tendency that past price return has the negative correlation with future volatility \cite{Bouchaud_2001}.
According to Bouchaud et al. and Qiu et al., this statistical property is quantified by the following lead-lag correlation function 

.. math::
   :nowrap:
   
   \begin{equation}
      L(k)=\frac{E[r(t){|r(t+k)|}^{2}-r(t){|r(t)|}^{2}]}{E[|r(t)|^{2}]^{2}}.
   \end{equation}

In contrast to other statistical properties, this property is market dependent according to Qiu et al.
While the negative correlation (leverage effect) is observed in German DAX, the positive correlation (so-called anti-leverage effect) is detected in Chinese markets.

Code Example
^^^^^^^^^^^^

.. literalinclude:: ../codes/leverage.py
   :language: python
   :emphasize-lines: 12,15-18
   :linenos:

References
^^^^^^^^^^

1. Bouchaud
2. Qiu 
