# Auth Files Management for Locals Scripts for Google Apis.

Supports JSON secrets for both service account and OAuth.
Files are stored in ~/.google/<name>.json.

## Motivation

This is intended to be imported to get credentials, that given a script name,
will know where to find the secrets and automatically cache the credentials so
we can easily run command-line scripts with cached credentials to the various
Google APIs.

Ideally, a script should just have to do something like this:

    import gapis
    ...
    creds = gapis.get_credentials('my-script-unique-key')
    service = discovery.build(..., credentials=creds)

Clients just have to download the corresponding secrets files to their
`~/.google` directory, under the name for their script, e.g.,
`my-script-unique-key.json`.

This should work for both OAuth and Service Accounts.

## History

I found myself replicating bad, incomplete versions of this all over the place
over the years. This is intended to be an as-simple-as-possible library that I
use in common for all those scripts.

I think something like this ought to exit inside the google.auth project.


## Author

Martin Blais <blais@furius.ca>
