#!/bin/bash

db="LibraryDB.sqlite"
rm -f ${db}
touch ${db}

sqlite3 ${db} < LibraryDB.sql
