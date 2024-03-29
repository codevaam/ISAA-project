import redis
import base64
from finalcheck import predict_output
import time
conn = redis.Redis(host='localhost', port=6379)


def read_and_decode_from_redis(msg):
    print('Updating File')
    with open("debug.csv", "wb") as f:
        f.write(msg[0][1][-1][1][b'csv'])


def flow_classify(filename):
    print(predict_output(filename))


def subscription_loop():
        while True:
            try:
                message = conn.xread({'DATASTREAM': b"0-0"})
                last = message
                read_and_decode_from_redis(message)
                time.sleep(10)
                flow_classify("debug.csv")
            except Exception as e:
                print(e, 'Trying old data')
                try:
                    read_and_decode_from_redis(last)
                    time.sleep(10)
                    flow_classify("debug.csv")
                except Exception as e:
                    print(e)
                
            


if __name__ == "__main__":
    subscription_loop()
