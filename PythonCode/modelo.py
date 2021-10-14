from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error



def estadisticas(y_predicted, y_holdout):
    print("R-Square Value", r2_score(y_holdout, y_predicted))
    print("\n")
    print("mean_absolute_error :", mean_absolute_error(y_holdout, y_predicted))
    print("\n")
    print("mean_squared_error : ", mean_squared_error(y_holdout, y_predicted))
    print("\n")
    print("root_mean_squared_error : ", mean_squared_error(y_holdout, y_predicted, squared=False))
