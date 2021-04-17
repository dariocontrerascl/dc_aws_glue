#!/usr/bin/env python3
#
# Declare IBH Solutions AWS infrastructure.
#

from src.app import create_app


if __name__ == "__main__":
    create_app().synth()
