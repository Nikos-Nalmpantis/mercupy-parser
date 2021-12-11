import cProfile
import pstats

from mercupy_parser import Mercupy


def main():
    print(f"Running {__file__}")
    mercupy = Mercupy(verbose=True)

    headers = '{"Cookie": "VISITOR_INFO1_LIVE=p-LCKo9eugA; '\
                  'YSC=j-j8cbZlUV8; GPS=1; CONSENT=YES+cb.20210406-12-p0.es+FX+603;", '\
                  '"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) '\
                  'AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"}'

    with open("tests/urls.txt") as f:
        urls = f.readlines()
    urls = [url.strip() for url in urls]

    with cProfile.Profile() as pr:
        mercupy.parser(urls, headers=headers)

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.dump_stats(filename="needs_profiling.prof")
    # Run: snakeviz needs_profiling.prof


if __name__ == "__main__":
    main()

