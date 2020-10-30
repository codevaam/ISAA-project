import os
import time
from convertCSV import replaceNull

while True:
    try:
        # if(os.path.isfile('./data-collectors/nDPI/debug.csv')):
        #     print('seeding')
        #     replaceNull('./data-collectors/nDPI/debug.csv')
            # temporary tags and fields choosen
        if(os.path.isfile('./final.csv')):
            print('seeding')
            replaceNull('./final.csv')
            os.system('export_csv_to_influx -c final.csv -db _internal -m ndpi_proto -fc src_ip,dst_ip,predicted -tc ndpi_proto')
            os.remove('test_influx.csv')
    except:
        print('skip')
    # update every 10 sec
    time.sleep(10)
    