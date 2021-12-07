from mercupy_parser import Mercupy


def main():
    api_endpoint = "http://0.0.0.0:4000/parser"
    headers = '{"Cookie": "VISITOR_INFO1_LIVE=p-LCKo9eugA; '\
              'YSC=j-j8cbZlUV8; GPS=1; CONSENT=YES+cb.20210406-12-p0.es+FX+603;", '\
              '"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) '\
              'AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"}'
    content_type = "markdown"


    with open("urls.txt") as f:
        urls = f.readlines()
    urls = [url.strip() for url in urls]

    mercupy = Mercupy(api_endpoint=api_endpoint)

    responses = mercupy.parser(urls[4])  #, headers=headers, content_type=content_type)
    print(responses)
    print(responses[0].json())


if __name__ == "__main__":
    main()

