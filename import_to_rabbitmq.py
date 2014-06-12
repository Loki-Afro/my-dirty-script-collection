import sys
import getopt
import pika


def main(argv):
        amqp_queue = ''
        failed_messages_file = ''
        try:
                opts, args = getopt.getopt(argv, "hq:f:", ["queue=", "failedMessages="])
        except getopt.GetoptError:
                print_help(2)
        for opt, arg in opts:
                if opt == '-h':
                        print_help(0)
                elif opt in ("-q", "--queue"):
                        amqp_queue = arg
                elif opt in ("-f", "--failedMessages"):
                        failed_messages_file = arg
        print 'queue is ', amqp_queue
        print 'failedMessages is ', failed_messages_file
        if not failed_messages_file or not amqp_queue:
                print_help(2)

        publish_messages(failed_messages_file, amqp_queue)


def print_help(exit_code):
    print 'import_to_rabbitmq.py -q <queueName> -f <failedMessagesFile>'
    sys.exit(exit_code)


def publish_messages(failed_messages_file, amqp_queue):
    credentials = pika.PlainCredentials('admin', 'admin')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
    channel = connection.channel()
    lines = tuple(open(failed_messages_file, 'r'))
    for message in lines:
        channel.basic_publish(exchange='', routing_key=amqp_queue, body=message)


if __name__ == "__main__":
    main(sys.argv[1:])
