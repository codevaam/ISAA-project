import os
import time
from convertCSV import replaceNull

while True:
    if(os.path.isfile('tardigate-data-collector/nDP/test.csv')):
        replaceNull('test.csv')
        # temporary tags and fields choosen
        os.system('export_csv_to_influx -c test.csv -db _internal -m protocol -fc src_ip')
        os.remove('test_influx.csv')
    # update every 10 sec
    time.sleep(10)