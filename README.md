## Backend local development

* For ease of use the .env file already exists with the correct variables although this is not a good practice

* Start the stack with Docker Compose:

```bash
docker-compose up
```

* Now you can open your browser and interact with these URLs:

    * /customers/birthday
    * /customers/last-order-per-customer
    * /top-selling-products/{year}

## Database initialisation

On the first docker-compose will run a python script 'app/initial_data.py' in order to 
populate the db with the given data. This can be turned off to stop running that script on each
start of the docker by setting the env var in .env to 'INIT_DB_DATA=off'