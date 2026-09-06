# Registers a Windows Scheduled Task that starts the Heinlein bot at logon and restarts it if it stops.
# Run once from an elevated PowerShell:  .\Install-HeinleinTask.ps1
# Remove with:  Unregister-ScheduledTask -TaskName "Heinlein Bot" -Confirm:$false
# No em-dashes in this file: Windows PowerShell 5.1 misreads them.

$ErrorActionPreference = "Stop"
$botDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$script = Join-Path $botDir "Start-Heinlein.ps1"
$taskName = "Heinlein Bot"

$action = New-ScheduledTaskAction -Execute "powershell.exe" `
    -Argument "-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File `"$script`"" `
    -WorkingDirectory $botDir

$trigger = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME

$settings = New-ScheduledTaskSettingsSet `
    -RestartCount 999 `
    -RestartInterval (New-TimeSpan -Minutes 1) `
    -ExecutionTimeLimit (New-TimeSpan -Days 0) `
    -MultipleInstances IgnoreNew `
    -StartWhenAvailable

if (Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue) {
    Unregister-ScheduledTask -TaskName $taskName -Confirm:$false
}

Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Settings $settings `
    -Description "Heinlein Slack bot for the writing pipeline. Runs as the logged-in user so the Claude Code login and the repo are visible." | Out-Null

Start-ScheduledTask -TaskName $taskName
Write-Host "Registered and started '$taskName'. Check heinlein/bot/logs/heinlein-bot.log and post /heinlein status in Slack."
