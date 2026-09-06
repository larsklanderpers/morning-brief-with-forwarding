# Starts the Heinlein bot in the foreground. Used directly for a dry run, and by the scheduled task.
# No em-dashes in this file: Windows PowerShell 5.1 misreads them.

$ErrorActionPreference = "Stop"
$botDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$root = Resolve-Path (Join-Path $botDir "..\..")

if (-not (Test-Path (Join-Path $botDir ".env"))) {
    Write-Error "heinlein/bot/.env is missing. Copy .env.example and fill in the two Slack tokens."
}

$python = (Get-Command python).Source
Write-Host "Heinlein bot starting from $root using $python"
Set-Location $root
& $python (Join-Path $botDir "app.py")
