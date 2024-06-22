# Tool for imperva log visualization using grafana

## How to use

```
git clone https://github.com/Chmele/grafana-imperva-stats.git .
docker compose build
docker compose up
```

Api endpoint at `localhost:8000/` to upload single archive with 4000 files to the desired measurement (specify name in text field on html form) in influxdb

Grafana is up on `localhost:3000`, the user is default - admin, admin

Volumes mounted, so container remove/rebuild would not affect data in database.
