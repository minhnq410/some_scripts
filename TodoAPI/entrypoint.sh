#!/bin/bash
set -e
run-cmd="dotnet TodoAPI.dll"

until dotnet ef database update; do
>&2 echo "SQL Server is starting up"
sleep 1
done

>&2 echo "SQL Server is up - Executing command"
exec $run-cmd