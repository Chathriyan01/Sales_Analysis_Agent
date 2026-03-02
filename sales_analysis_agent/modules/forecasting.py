from prophet import Prophet

def train_forecast_model(df):
    model_df = df.rename(columns={"date":"ds","sales":"y"})
    model = Prophet()
    model.fit(model_df[["ds","y"]])
    return model

def forecast_sales(model, periods):
    future = model.make_future_dataframe(periods=periods)
    return model.predict(future)