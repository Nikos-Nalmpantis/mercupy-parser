# MercuPy Parser
Python wrapper for [mercury-parser](https://github.com/postlight/mercury-parser)

---

## Installation
`docker-compose.yml` contains the configuration to run [mercury-parser](https://github.com/postlight/mercury-parser) with [nginx](https://www.nginx.com/) as the load blancer.

```bash
# n is the number of instances of mercury-parser
docker-compose up -d --scale mercury-parser=n
```
Then you can access the service at [http://localhost:4000](http://localhost:4000).

```bash
pip install mercupy-parser
```

---

## Usage
```python
from mercupy_parser import Mercupy

# api_endpoint = "http://localhost:4000/parser"
mercupy = Mercupy(api_endpoint=api_endpoint, verbose=True)

# parse single url
responses = mercupy.parser(url, headers=headers, content_type=content_type)

# parse multiple urls
responses = mercupy.parser(urls, headers=headers, content_type=content_type)

print(responses[0].json())
```
