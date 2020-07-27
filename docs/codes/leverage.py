import stylefact.finance as sff
import stylefact.visualize as sfv
import numpy as np
returns = np.random.Normal(size=10000)
result = sff.leverage_effect(returns)
sfv.leverage_effect(result)