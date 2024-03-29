import pandas as pd
import json
import pickle
from  pred_data import la_triche
import sys
# import numpy

ACCEPTABILITY = {0: "Acceptable", 1: "Dangerous", 2: "Fun",
                 3: "Network", 4: "Safe", 5: "Unrated", 6: "Unsafe"}


# ignore all future warnings
from warnings import simplefilter
from pandas.core.common import SettingWithCopyWarning
simplefilter(action='ignore', category=FutureWarning)
simplefilter(action='ignore', category=UserWarning)
simplefilter(action='ignore', category=SettingWithCopyWarning)


def predict_output(filename):
    try:
        data = pd.read_csv(filename)
        print('Loaded File')
        loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
        features = ['ndpi_proto_num', 'src2dst_packets', 'src2dst_bytes', 'dst2src_packets', 'dst2src_bytes', 'data_ratio', 'iat_flow_min', 'iat_flow_avg', 'iat_flow_max', 'iat_flow_stddev', 'iat_c_to_s_min', 'iat_c_to_s_avg', 'iat_c_to_s_max', 'iat_c_to_s_stddev',
                    'iat_s_to_c_min', 'iat_s_to_c_avg', 'iat_s_to_c_max', 'iat_s_to_c_stddev', 'pktlen_c_to_s_min', 'pktlen_c_to_s_avg', 'pktlen_c_to_s_max', 'pktlen_c_to_s_stddev', 'pktlen_s_to_c_min', 'pktlen_s_to_c_avg', 'pktlen_s_to_c_max', 'pktlen_s_to_c_stddev']
        data['src2dst_packets'] = [0] * len(data)
        data['src2dst_bytes'] = [0] * len(data)
        data['dst2src_packets'] = [0] * len(data)
        data['dst2src_bytes'] = [0] * len(data)
        X = data[features]
        y_pred = loaded_model.predict(X)
        feat = ['src_ip', 'dst_ip', 'ndpi_proto']
        info = data[feat]
        y_pred = pd.DataFrame(y_pred)
        info['predicted'] = y_pred
        # df_ct = pd.concat([info, y_pred])
        info = la_triche(info)
        info.to_csv('final.csv')
        print(info)
        return info
    except Exception as e:
        print('Exception, skipping')
