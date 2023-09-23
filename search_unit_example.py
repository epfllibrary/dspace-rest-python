# This software is licenced under the BSD 3-Clause licence
# available at https://opensource.org/licenses/BSD-3-Clause
# and described in the LICENCE file in the root of this project

"""
Example using the dspace.py API client library 
"""
import pprint

from dspace_rest_client.client import DSpaceClient

# Instantiate DSpace client
d = DSpaceClient()

# Authenticate against the DSpace client
authenticated = d.authenticate()
if not authenticated:
    print(f'Error logging in! Giving up.')
    exit(1)

query = "laboratory"
configuration = "orgunit"

dsos = d.search_objects(query=query, configuration=configuration)
for dso in dsos:
    pprint.pprint(dso.metadata)


