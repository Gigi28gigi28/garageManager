from django.shortcuts import render
from django.http import HttpResponse
import requests
import pika
import json
# Create your views here.


def faireReparation(request,id,duree):
    piece=requests.get(f"http://localhost:8000/api/piece/{id}").json()
    reparation={"piece":piece["id"],"duree":duree}
    with pika.BlockingConnection(pika.ConnectionParameters("localhost")) as con:
        ch=con.channel()
        ch.basic_publish(exchange="", routing_key="garage",body=json.dumps(reparation))
        return HttpResponse("Done!")