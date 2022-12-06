# -*- coding: UTF-8 -*-
import sys
import argparse

from workflow import Workflow3
from generator import (
    get_raddom_inn_fl,
    get_random_inn_ul,
    get_random_kpp,
    get_random_ogrn,
    get_random_snils,
    get_random_guid,
    get_random_ogrnip
)

LOG = None


def log_result(f):
    def wrapped(*args, **kwargs):
        res = f(*args, **kwargs)
        LOG.info("Returning result is %s", res)
        return res
    
    return wrapped

def get_result(args):
    if args.innul:
        return get_random_inn_ul()
    if args.innfl:
        return get_raddom_inn_fl()
    if args.snils:
        return get_random_snils()
    if args.ogrn:
        return get_random_ogrn()
    if args.kpp:
        return get_random_kpp()
    if args.guid:
        return get_random_guid()
    if args.ogrnip:
        return get_random_ogrnip()
    return None

@log_result
def main(wf):
    # command line parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--inn', dest='innul', action='store_true', default=False)
    parser.add_argument('--innfl', dest='innfl', action='store_true', default=False)
    parser.add_argument('--snils', dest='snils', action='store_true', default=False)
    parser.add_argument('--ogrn', dest='ogrn', action='store_true', default=False)
    parser.add_argument('--ogrnip', dest='ogrnip', action='store_true', default=False)
    parser.add_argument('--kpp', dest='kpp', action='store_true', default=False)
    parser.add_argument('--guid', dest='guid', action='store_true', default=False)
    args = parser.parse_args(wf.args)
    LOG.info(args)

    res = get_result(args)
    print(res)
    return 0


if __name__ == u"__main__":
    wf = Workflow3()
    LOG = wf.logger
    sys.exit(wf.run(main))
