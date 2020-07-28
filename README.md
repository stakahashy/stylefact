# stylefact


| Metric                     |                                                                                                                                          |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| **Continuous Integration** | [![Travis Build Status](https://travis-ci.org/stakahashy/stylefact.svg)](https://travis-ci.org/stakahashy/stylefact)                     |
| **Documentation**          | [![Documentation Status](https://readthedocs.org/projects/stylefact/badge/?version=latest)](http://stylefact.readthedocs.org/en/latest/) |

### Python 3
  `stylefact` only supports Python 3

### Documentation
[stylefact documentation](https://stylefact.readthedocs.io/en/latest/)


## Supported Stylized Facts

- probability distribution
- autocorrelation function
- leverage effect
- coarse-fine volatility
- gain/loss asymmetry

## Example

```python
import datetime as dt
import pandas_datareader.data as web
import numpy as np
import stylefact.finance as sff
import stylefact.visualize as sfv
st = dt.datetime(1990,1,1)
en = dt.datetime(2020,1,1)
data = web.get_data_yahoo('GM', start=st, end=en)
prices = data['Adj Close'].to_numpy()
log_prices = np.log(prices)
returns = np.diff(log_prices)

x,y = sff.linear_distribution(returns)
sfv.linear_distribution(x,y,'linear_distribution')
x,y = sff.log_distribution(returns,'positive')
sfv.log_distribution(x,y,'log_positive_distribution')
x,y = sff.log_distribution(returns,'negative')
sfv.log_distribution(-x,y,'log_negative_distribution')

x,y = sff.autocorrelation(returns)
sfv.autocorrelation(x,y,'autocorrelation',scale='linear')
x,y = sff.autocorrelation(np.abs(returns))
sfv.autocorrelation(x,y,'abs_autocorrelation',scale='log')

x,y = sff.leverage_effect(returns)
sfv.leverage_effect(x,y,'leverage_effect')

x,y = sff.coarsefine_volatility(returns)
sfv.coarsefine_volatility(x,y,'coarsefine')

positive_dist,negative_dist = sff.gainloss_asymmetry(returns)
sfv.gainloss_asymmetry(positive_dist,negative_dist,'gainloss_asymmetry')

```

## Requirements

These requirements reflect the testing environment. It is possible
that stylefact will work with older versions.

- Python (3.6+)
- NumPy (1.14+)
- matplotlib (2.0+)

