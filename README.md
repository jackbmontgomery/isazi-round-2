# Jack Montgomery - Pandemic Forecasting

## Structure

- pandemic_forecasting.ipynb : This contains code that creates and evalutes the model
- improvements.txt : Paragraph about future system improvements
- artifacts : Folder containing the forecasting image as well as the forecast csv file
- pandemic_forecasting : Folder that runs the local webapp

## Notebook requirements:

```
uvicorn[standard]==0.20.0
fastapi[all]==0.88.0
bs4
requests
pandas
statsmodels
```

## Webapp

[docker](https://docs.docker.com/get-started/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/) are required to run the webapp and api

Once installed, navigate to /pandemic_forecasting in your command line and run the following command:

```sh
docker compose up --build -d
```

Once the fastapi has started and the nuxt is running. This will be displayed in the CLI. You can navigate [here](http://localhost:3000/) to view the webapp

When you are done, navigate back to the command line and ensure that you are still in /pandemic_forecasting and run:

```sh
docker compose down
```
