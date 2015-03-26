#!/usr/bin/env python
# encoding: utf-8
"""

Author:
    Kian Ho <hui.kian.ho@gmail.com>

Description:
    ...

Usage:
    run.py [options]

Options:
    -h, --help              Display this message.
    --credentials FILE      JSON file containing the Twitter API credentials
                            [default: credentials.json].

"""

import os
import sys
import json
import tweepy

from docopt import docopt


def main(opts):
    """The driver function.

    """

    with open(opts["--credentials"], "rb") as f:
        creds = json.load(f)

    auth = tweepy.OAuthHandler(creds["consumer_key"], creds["consumer_secret"])
    auth.set_access_token(creds["access_token"], creds["access_token_secret"])

    api = tweepy.API(auth)

    # Add twitter search here.

    return


if __name__ == '__main__':
    opts = docopt(__doc__)
    main(opts)
