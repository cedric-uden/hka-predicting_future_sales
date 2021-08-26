# Predicting Future Sales
Repo for my 5th semester research project

Planing is done on a miro board: https://miro.com/app/board/o9J_lNamDng=/


# 🛠 Troubleshooting


## Issues on Apple Silicon (M1)

Some issues were encountered after setting up the conda environment 
with poetry. Following fixes were applied

First, check that the right conda environment is active
```bash
conda activate rp
```

### Issues with `XGBoost`

#### Issue: *XGBoost Library (libxgboost.dylib) could not be loaded.*

```bash
conda install -c conda-forge py-xgboost
```


#### Issue: *cannot import name 'CUDF_concat' from 'xgboost.compat'*

```bash
brew install xgboost
```