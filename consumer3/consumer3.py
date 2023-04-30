import pika
import mysql.connector
import json

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.126', 5672, '/', credentials))

channel = connection.channel()
channel.exchange_declare(exchange='deletion', exchange_type='direct')
channel.queue_declare(queue='deletion_queue')
channel.queue_bind(exchange='deletion', queue='deletion_queue')

mydb = mysql.connector.connect(
    host="192.168.0.126",
    user="root",
    database="student_project",
    password="password"
)
c = mydb.cursor()

def callback(ch, method, properties, body):
    print("Received message for deleting record: {}".format(body))
    srn = body.decode()
    # delete the record from the database
    c.execute("DELETE FROM STUDENTS_DETAILS WHERE srn=%s", (srn,))
    mydb.commit()
    # acknowledge that the message has been received
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='deletion_queue', on_message_callback=callback)
channel.start_consuming()



