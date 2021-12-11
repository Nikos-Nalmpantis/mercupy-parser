MercuPy Parser
==============

*Python wrapper for mercury-parser*

Installation
************

``docker-compose.yml`` contains the configuration to run `mercury-parser <https://github.com/postlight/mercury-parser>`_ with `nginx <https://www.nginx.com/>`_.


::

    docker-compose up -d --scale mercury-parser=n

where n is the number of instances of mercury-parser

Then you can access the service at `http://localhost:4000 <http://localhost:4000>`_.

::

    pip install mercupy-parser

Usage
*****

.. code:: python

    from mercupy_parser import Mercupy

    # api_endpoint = "http://localhost:4000/parser"
    mercupy = Mercupy(api_endpoint=api_endpoint, verbose=True)

    # parse single url
    responses = mercupy.parser(url, headers=headers, content_type=content_type)

    # parse multiple urls
    responses = mercupy.parser(urls, headers=headers, content_type=content_type)

    print(responses[0].json())
