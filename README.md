# DSpace Python REST Client Library
This client library allows Python 3 scripts (Python 2 probably compatible but not officially supported) to interact with
DSpace 7+ repositories, using the DSpace REST API.

This library is a work in progress and so far offers basic create, update, retrieve functionality for
Community, Collection, Bundle, Item, Bitstream, Group and User (EPerson) objects.

Help with extending the scope and improving the code is always welcome!

## Requirements
* Python 3.x (developed using Python 3.8.5)
* Python Requests module (see `requirements.txt`)
* Working DSpace 7 repository with an accessible REST API

## Installation
To install, clone this repository and install the requirements:
```commandline
git clone https://github.com/the-library-code/dspace-rest-python.git
pip install -r requirements.txt
```

## Usage
After installing dependencies, you're ready to run the script.
Set your API token and base URL in the config.ini file, following the `config.ini.example` template.

Refer to the `example.py` script for an illustration of community, collection, item, bundle, and bitstream creation. 
For an example of querying items in the repository, consult the `search_example.py` script.

The output from the `example.py` script should look something like:

```commandline
╰─$ python example.py                                                                                                                                                                                                              1 ↵
Authenticated successfully
API Post: Updating token to b44f91c2-5386-4c11-a1ca-1ea06613fae4
{"timestamp":"2022-02-10T05:44:12.758+00:00","status":403,"error":"Forbidden","message":"Access is denied. Invalid CSRF token.","path":"/server/api/core/communities"}
API Post: Retrying request with updated CSRF token
community 31264734-49c0-4bff-8ed7-e09e3abbfe7a created successfully!
New community created! Handle: 123456789/10
collection c010ef9c-2483-47c3-83af-8a8c1f72e888 created successfully!
New collection created! Handle: 123456789/11
item e59dfc7a-f96e-4897-a913-e962b220132b created successfully!
New item created! Handle: 123456789/12
New bundle created! UUID: 528d1dd9-ca62-4609-bb2e-1ab367299447
New bitstream created! UUID: 4740048b-25fa-4040-b0d1-4b27f13de75d
All finished with example data creation. Visit your test repository to review created objects
```

## Credits

Created by [Kim Shepherd](https://www.github.com/kshepherd) for [The Library Code GmbH](https://www.lib-co.de) with support from Universität Hohenheim

## License

This work is licensed under the [BSD 3-Clause License](https://github.com/the-library-code/dspace-rest-python/blob/088169cdcb1a92ff33589b1af8c08a17f9885bbf/LICENSE)

Copyright 2021 The Library Code GmbH
