@echo off
setlocal

REM List of folder names (as they currently exist)
set folders=T02-invalid-api-key.md T03-rate-limit.md T04-internal-server-error.md T05-forbidden.md T06-not-found.md T07-timeout.md T08-conflict.md T09-payload_too_large.md T10-unprocessable-entity.md

REM Loop through each folder and create 4 empty PNGs
for %%F in (%folders%) do (
    echo Creating placeholders in screenshots\%%F...

    type nul > "screenshots\%%F\network.png"
    type nul > "screenshots\%%F\headers.png"
    type nul > "screenshots\%%F\payload.png"
    type nul > "screenshots\%%F\response.png"
)

echo Done.
pause
