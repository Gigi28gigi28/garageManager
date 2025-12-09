import requests
import pika

def traiterreparation(ch, method, properties, body):
    reparation=body.decode()
    print(reparation)
    res=requests.post("http://localhost:8000/api/reparation/",data=reparation)
    if res.status_code==200:
        ch.basic_ack(delivery_tag=method.delivery_tag)
    else:
        ch.basic_ack(delivery_tag=method.delivery_tag,requests=True)
    
with pika.BlockingConnection(pika.ConnectionParameters("localhost")) as con:
    ch=con.channel()
    ch.basic_consume("garage",traiterreparation,auto_ack=False)
    ch.start_consuming()