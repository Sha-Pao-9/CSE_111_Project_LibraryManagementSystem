#!/bin/bash

db="ships.sqlite"
rm -f ${db}
touch ${db}

sqlite3 ${db} < LibraryDB.sql
