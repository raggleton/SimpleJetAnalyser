# SimpleJetAnalyser

This is a little EDAnalyzer for looping over PF jets, and looking at offline JEC.

There are 3 configs, which will pull JEC from different places:

- [`run_GT.py`](python/run_GT.py) will take them from the GlobalTag

- [`run_DB.py`](python/run_DB.py) will take them from a SQL file

- [`run_DB_Service.py`](python/run_DB_Service.py) will take them from a SQL file, with ESProducers also added in case.

Reference jet et/corrected et/eta/phi values for 2 events are in [`76_Fall15_25nsV2.out`](python/76_Fall15_25nsV2.out) and [`76_Summer15_25nsV7.out`](python/76_Summer15_25nsV7.out). These are taken from running with `run_GT.py` so they must (should!) be correct. They were made in `CMSSW_7_6_4`.

## Installation

In `$CMSSW_BASE/src` do:

```
git clone git@github.com:raggleton/SimpleJetAnalyser.git Demo/JetAnalyser
scram b -j9
```

