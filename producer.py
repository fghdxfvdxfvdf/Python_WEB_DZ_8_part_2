import json
import logging

import pika
from faker import Faker
from pymongo.errors import ConfigurationError

from model import User

print('pika version: %s' % pika.__version__)

fake = Faker()
USER_NUMBERS = 5


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')


def fake_data(users_number: int) -> list:
    users = []
    for _ in range(users_number):
        full_name = fake.name()
        email = fake.email()
        address = fake.address()
        user = User(full_name=full_name, email=email, address=address)
        user.save()
        users.append(user)
    return users


def main():
    users = fake_data(USER_NUMBERS)
    print(f"Sending messages for {len(users)} users:")
    
    for user in users:
        channel.basic_publish(exchange='logs', routing_key='', body=json.dumps(str(user)).encode())
        print(f"Sent message for user: {user.full_name}")
    
    print("\nMessages sent. Closing connection.")
    connection.close()
    
if __name__=='__main__':
    # logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    try:
        main()

    except ConfigurationError as err:
        logging.error('Error:', err)