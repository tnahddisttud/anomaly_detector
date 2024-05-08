import numpy as np
import pandas as pd
import datetime


def load_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    return get_relevant_df(data)


def get_relevant_df(data: pd.DataFrame) -> pd.DataFrame:
    data = data.rename(columns={'values': 'metrics'})
    data['metrics'] = data['metrics'].apply(eval)
    data[['memory_usage', 'memory_virtual', 'cpu_percent', 'cpu_time', 'disk_io', 'memory_percent']] = data[
        'metrics'].apply(lambda x: pd.Series(x, dtype=np.float128) if len(x) == 6 else pd.Series([np.nan] * 6))
    final_data = data.drop(columns=['resource', 'type', 'resource_attributes', 'metrics'])
    final_data = final_data.sort_values(by='ts')
    final_data['ts'] = final_data['ts'].apply(lambda x: datetime.datetime.fromtimestamp(x / 1000))
    final_data['ts'] = pd.to_datetime(final_data['ts'])
    final_data.set_index('ts', inplace=True)
    return final_data
