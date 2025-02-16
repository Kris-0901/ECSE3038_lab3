# Tanks RESTful API Server

## Summary

This is a RESTful API that allows each IoT enabled water tank to interface with a server so that the measured values
can be represented visually on a web page.Each tank will have an embedded circuit attached that will measure the 
height of the water in the tank and report on the tank's current stored volume as a percentage of its maximum 
capacity.

The server is able to perform the actions of a simple HTTP web server. The server is able to perform actions on a 
resource such as Create, Read, Update and Delete. This is done with the use of a locally stored list variable for 
the purpose of prototyping a proof of concept.The server is designed to host five specific HTTP routes(**RESTful API**). They are:

- GET `/tank`

- GET `/tank/{id}`

- POST `/tank`

- PATCH `/tank/{id}`

- DELETE `/tank/{id}`

**A Tank entity will consist of the following attributes:**

- id (to automatically inserted by web application)
- location - The Tank’s location description
- lat - The latitudinal coordinate of the tank
- long - The Longitudinal coordinate of the tank

## Routes & Expected Behaviour

### GET `/tank`
___


*Expected Response. If an object has not been POSTed yet*

- Status Code: `200 OK`

```json
[]
```

*Expected Response.  If an object had been previously POSTed*

- Status Code: `200 OK`

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



### GET `/tank/{id}`
___

*Expected Response:*

- Status Code: `200 OK`

```json
{
    "id": "0cf996c3-d9ca-4c0b-ab01-52b26c9050ec",
    "location": "Engineering department",
    "lat": "18.0051862",
    "long": "-76.7505108",
}

```

*Expected Response if API is unable to locate object:*

- Status Code: `404 Not Found`

```json
{
	"detail":"Tank not found"
}

```

### POST `/tank`
___

*Expected Request:*

```json
{
    "location": "Physics department",
    "lat": 18.004741066082236,
    "long": -76.74875280426826
}

```

*Expected Response:*

- Status Code: `201 Created`

```json
{
    "id": "2ecc8f75-7594-4383-ac59-a24aff085cb3"
    "location": "Physics department",
    "lat": "18.004741066082236",
    "long": "-76.74875280426826"
}

```
### PATCH `/tank/{id}`
___

*Expected Request:*

```json
{
    "location": "<new location>", //optional
    "lat": "<new lat>", //optional
    "long": "<new long>", //optional
}

```

*Expected Response:*

- Status Code: `200 OK`

```json
{
    "id": "<id>",
    "location": "<updated location>",
    "lat": "<updated lat>",
    "long": "<updated long>",
}

``` 
*Expected Response if API is unable to locate object:*

- Status Code: `404 Not Found`

```json
{
	"detail":"Tank not found"
}

```

### DELETE `/tank/{id}`
___

*Expected Response:*

- Status Code: `204 NO CONTENT`

*Expected Response if API is unable to locate object:*

- Status Code: `404 Not Found`

```json
{
	"detail":"Tank not found"
}

```

## Purpose

This code was written to fulfill the course requirements of 'ECSE3038 Engineering Internet of Things Systems' and to
learn the Python programming language and RESTful API server.

## Two Truths & A Lie

- I know kickboxing 
- I have more than five dogs
- I only have one pair of sneakers