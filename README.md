# python-api-takehomeproject


[x] Create a Python fastAPI endpoint that takes in an English letter and returns a poet with a first name that begins with that letter (https://poetrydb.org/author can be used as a free backend API call).

[x] Write a Dockerfile to create an image for the API.

[x] Create a Terraform file for a potential infrastructure option if the API was to be hosted in the cloud.

```
# Build a container image with the included Dockerfile
docker build -t poetlist-fastapi .

# Run the container, forward requests from host port 80 to container port 8000
docker run -d -p 80:8000 --name poetlist-app poetlist-fastapi

# A random poet name with the matching first letter will be returned.
curl localhost/a
["Anne Killigrew"]

curl localhost/a
[]"Anne Bronte"]

# Response if a poet name isn't found.
curl localhost/z
{"detail":"Poet Not found with first name starting with the letter Z."}

# Only single letter values are accepted
curl localhost/aa
{"detail":"aa is not a single english letter :(, Try again."}

curl localhost/5
{"detail":"5 is not a single english letter :(, Try again."}

curl localhost/!
{"detail":"! is not a single english letter :(, Try again."}
```