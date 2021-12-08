from mercupy_parser import Mercupy


with open("urls.txt") as f:
    urls = f.readlines()
URLS = [url.strip() for url in urls]
HEADERS = '{"Cookie": "VISITOR_INFO1_LIVE=p-LCKo9eugA; '\
          'YSC=j-j8cbZlUV8; GPS=1; CONSENT=YES+cb.20210406-12-p0.es+FX+603;", '\
          '"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) '\
          'AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"}'
CONTENT_TYPE = "markdown"


def test_parse_single_url():
    mercupy = Mercupy()
    responses = mercupy.parser(URLS[0])
    assert responses[0].status_code == 200


def test_parse_multiple_urls():
    mercupy = Mercupy()
    responses = mercupy.parser(URLS)
    assert len(responses) == 15
    for response in responses:
        assert response.status_code == 200


def test_parse_single_url_headers():
    mercupy = Mercupy()
    responses = mercupy.parser(URLS[0], headers=HEADERS)
    assert responses[0].status_code == 200


def test_parse_multiple_urls_headers():
    mercupy = Mercupy()
    responses = mercupy.parser(URLS, headers=HEADERS)
    assert len(responses) == 15
    for response in responses:
        assert response.status_code == 200


def test_parse_single_url_content_type():
    mercupy = Mercupy()
    responses = mercupy.parser(URLS[0], content_type=CONTENT_TYPE)
    assert responses[0].status_code == 200


def test_parse_multiple_urls_content_type():
    mercupy = Mercupy()
    responses = mercupy.parser(URLS, content_type=CONTENT_TYPE)
    assert len(responses) == 15
    for response in responses:
        assert response.status_code == 200


def test_parse_single_url_headers_content_type():
    mercupy = Mercupy()
    responses = mercupy.parser(URLS[0], headers=HEADERS, content_type=CONTENT_TYPE)
    assert responses[0].status_code == 200


def test_parse_multiple_urls_headers_content_type():
    mercupy = Mercupy()
    responses = mercupy.parser(URLS, headers=HEADERS, content_type=CONTENT_TYPE)
    assert len(responses) == 15
    for response in responses:
        assert response.status_code == 200
