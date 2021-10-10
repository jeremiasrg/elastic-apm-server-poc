# Elasticsearch + Phyton + APM + PONY

## POC With:

- Elasticsearch
- Kibana
- APM Server
- Phyton
- Flask
- Pony ORM
- Mysql

### Steps to run:

1. Clone project
2. Run code below

```json
docker compose up -d
```

1. Run api-caller.py

```json
python3 api-caller.py
```

1. Acess Kibana and see the APM results

```json
http://localhost:5601
```
