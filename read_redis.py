import redis
import base64
from finalcheck import predict_output
import time
conn = redis.Redis(host='localhost', port=6379)


def read_and_decode_from_redis(msg):
    # print(msg)
    decoded_fname = base64.b64decode(msg)
    with open("test.csv", "wb") as f:
        f.write(decoded_fname)


def flow_classify(filename):
    print(predict_output(filename))


def subscription_loop():

    # sub = conn.pubsub()
    # sub.subscribe("SAURAV")

    try:

        # while True:
            # print("ran")
        message = conn.xread({'SAURAV': b"0-0"})
        print(message[1][1])
            # message = sub.get_message()
            # print(message)
            # if message and message["type"] == "message":
            #     read_and_decode_from_redis(message['data'])
    # while True:
    #     time.sleep(10)
    #     flow_classify("./tardigate-data-collector/nDP/test.csv")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    subscription_loop()
