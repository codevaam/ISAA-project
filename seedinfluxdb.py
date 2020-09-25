import os
import time
from convertCSV import replaceNull

while True:
    try:
        if(os.path.isfile('tardigate-data-collector/nDP/debug.csv')):
            replaceNull('tardigate-data-collector/nDP/debug.csv')
            # temporary tags and fields choosen
            os.system('export_csv_to_influx -c debug.csv -db _internal -m ndpi_proto -fc ddos_score,infiltration_score,src_ip,dst_ip -tc ndpi_proto')
            os.remove('test_influx.csv')
    except:
        print('skip')
    # update every 10 sec
    time.sleep(10)
    