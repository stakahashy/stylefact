Introduction to ARCH Models
---------------------------
ARCH models are a popular class of volatility models that use observed values
of returns or residuals as volatility shocks.  A basic GARCH model is specified
as

.. math::
   :nowrap:

   \begin{eqnarray}
      r_t    & = & \mu + \epsilon_t \\
      \epsilon_t & = & \sigma_t e_t \\
      \sigma^2_t & = & \omega + \alpha \epsilon_{t-1}^2 + \beta \sigma^2_{t-1}
   \end{eqnarray}

A complete ARCH model is divided into three components:
