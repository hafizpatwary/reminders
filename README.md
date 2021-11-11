# reminders

Simple web service that stores reminders

### Prerequisites
- [Git ](https://git-scm.com/downloads)
- [Docker](https://docs.docker.com/get-docker/)
- Docker Compose (Will already be installed if you are using MacOS or Windows) click here for [Linux](https://docs.docker.com/compose/install/)

### Setup
Open up a terminal and run the commands shown below to get setup.

#### Clone the Repository
```bash
$ git clone https://github.com/hafizpatwary/reminders.git
$ cd reminders
```

#### Build & Run the app
```bash
docker-compose up -d --build
```

### Check application
```bash
$ curl http://localhost/api/reminders
[]

$ curl -H"Content-Type: application/json" \
       -XPOST \
       -d '{"time": "07:30", "message": "hello world"}' \
       http://localhost/api/reminders
       
$ curl http://localhost/api/reminders
[
  {
    "message": "hello world",
    "time": "07:30"
  }
]
```