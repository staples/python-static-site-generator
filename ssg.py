import typer

import ssg.parsers
from ssg.site import Site
import ssr.parsers

def main(source='content', dest='dest'):
    config = {
        'source': source,
        'dest': dest,
        'parsers': [ssg.parsers.ResourceParser(), ],
    }

    Site(**config).build()


typer.run(main)
