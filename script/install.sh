#!/usr/bin/env bash


# switch to script directory
cd "$(dirname "$0")"

main() {
    git clone https://github.com/Hoppix/allagan/
    pushd allagan
    pip install -r requirements.txt
    pip install .
    popd
    allagan --help
}

# call function with all given parameters
main "$@"