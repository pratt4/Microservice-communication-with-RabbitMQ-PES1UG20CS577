import pika
import mysql.connector
import json

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.126', 5672, '/', credentials))

channel = connection.channel()
channel.exchange_declare(exchange='read', exchange_type='direct')
channel.queue_declare(queue='read_queue')
channel.queue_bind(exchange='read', queue='read_queue')

channel.exchange_declare(exchange='read_response', exchange_type='direct')
channel.queue_declare(queue='read_queue_response')
channel.queue_bind(exchange='read_response', queue='read_queue_response')


mydb = mysql.connector.connect(
    host="192.168.0.126",
    user="root",
    database="student_project",
    password="password"
)
def callback(ch, method, properties, body):
    print("Received message for reading record.")
    c = mydb.cursor()
    c.execute("SELECT * FROM STUDENTS_DETAILS")
    records = c.fetchall()
    print(json.dumps(records))
    mydb.commit()
    ch.basic_publish(exchange='read_response', routing_key='read_queue_response', body=json.dumps(records))
    # acknowledge that the message has been received
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue='read_queue', on_message_callback=callback)
print('Waiting for messages.')

channel.start_consuming()



