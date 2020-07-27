# stylefact

[![Travis Build Status](https://travis-ci.org/stakahashy/stakahashy.svg?branch=master)](https://travis-ci.org/stakahashy/stylefact)  


## Module Contents
- [Finance](#finance)
- [Language](#language)


### Python 3
  `stylefact` only supports Python 3

## Documentation
  Not ready

## Examples
<a id="finance"></a>
### Finance

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

<a id="language"></a>
### Language
- Vocabulary Population
  - Zipf's law
  - Heaps' law 
- Temporal Structure
  - Ebeling and Neiman's method

## Requirements

These requirements reflect the testing environment. It is possible
that arch will work with older versions.

- Python (3.6+)
- NumPy (1.14+)
- SciPy (1.0.1+)
- matplotlib (2.0+), optional

