import sys
from pathlib import Path

# Add parent directory to path to find anml module
sys.path.insert(0, str(Path(__file__).parent.parent))

from AnLOF.AnLOF_module import AnLOF
from sample_data import X_train, X_val, y_train, y_val, features
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

anlof = AnLOF(
    X_train, X_val, y_train, y_val,
    features,
    base_model=LinearRegression,
    metric=mean_squared_error,
    higher_is_better=False
)

best_X_train, best_X_val, best_method, performance_df = anlof.forward()

print("Best method:",best_method)
print("Best X_train :", best_X_train.head())
print("Best X_val :", best_X_val.head())    
print(performance_df)
