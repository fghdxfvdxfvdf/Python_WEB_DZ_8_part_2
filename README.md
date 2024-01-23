# Python_WEB_DZ_8_part_2
1)
зайшов на сайл
    https://cloud.mongodb.com

включив MongoDB Compass 


підключаю RabbitMQ

запускаю в терміналі
    docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management
або в Docker Desktop

захожу на 
    http://localhost:15672
там ввожу
Username: guest
Password: guest

2)
запускаю
consumer.py
а далі
producer.py
