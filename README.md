# stylefact




| Metric                     |                                                                                                                                                                                                                                          |
| :------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |                                                                                                                    |
| **Continuous Integration** | [![Travis Build Status](https://travis-ci.org/stakahashy/stylefact.svg)](https://travis-ci.org/stakahashy/stylefact)                                                                                                                       |
| **Documentation**          | [![Documentation Status](https://readthedocs.org/projects/stylefact/badge/?version=latest)](http://stylefact.readthedocs.org/en/latest/)                                                                                                           |


### Python 3
  `stylefact` only supports Python 3

## Documentation
  Not ready

## Supported Stylized Facts

- probability distribution

```python
import datetime as dt
import pandas_datareader.data as web
st = dt.datetime(1990,1,1)
en = dt.datetime(2020,1,1)
data = web.get_data_yahoo('^FTSE', start=st, end=en)
returns = 100 * data['Adj Close'].pct_change().dropna()
import stylefact as sf

```

## Requirements

These requirements reflect the testing environment. It is possible
that arch will work with older versions.

- Python (3.6+)
- NumPy (1.14+)
- SciPy (1.0.1+)
- matplotlib (2.0+), optional

