# Hello

Refer to [this](https://www.youtube.com/watch?v=c-QsfbznSXI) vid for more info on the setup

## Building the image and running the container

```bash
# backend
docker build -t django-temp-be .

docker run -p 8000:8000 --name django-temp-be django-temp-be

# frontend
docker build -t django-temp-fe .

docker run -p 3000:80 --name django-temp-fe django-temp-fe
```
