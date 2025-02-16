# Tanks RESTful API Server

## Summary

This is a RESTful API that allows each IoT enabled water tank to interface with a server so that the measured values
can be represented visually on a web page.Each tank will have an embedded circuit attached that will measure the 
height of the water in the tank and report on the tank's current stored volume as a percentage of its maximum 
capacity.

The server is able to perform the actions of a simple HTTP web server. The server is able to perform actions on a 
resource such as Create, Read, Update and Delete. This is done with the use of a locally stored list variable for 
the purpose of prototyping a proof of concept.The server is designed to host five specific HTTP routes. They are:

```RESTful API
    GET /tank

    GET /tank/{id}

    POST /tank

    PATCH /tank/{id}

    DELETE /tank/{id}
```
**A Tank entity will consist of the following attributes:**

- id (to automatically inserted by web application)
- location - The Tank’s location description
- lat - The latitudinal coordinate of the tank
- long - The Longitudinal coordinate of the tank

## Routes & Expected Behaviour

`GET /tank`


*Expected Response. If an object has not been POSTed yet*

```json
[]
```

*Expected Response.  If an object had been previously POSTed*

```json

[
    {
	"id": "0cf996c3-d9ca-4c0b-ab01-52b26c9050ec",
        "location": "Engineering department",
        "lat": "18.0051862",
        "long": "-76.7505108",
    },
    .
    .
    .
]

```



## Purpose

This code was written to fulfill the course requirements of 'ECSE3038 Engineering Internet of Things Systems' and to
learn the Python programming language and RESTful API server.

## Two Truths & A Lie

- I know kickboxing 
- I have more than five dogs
- I only have one pair of sneakers