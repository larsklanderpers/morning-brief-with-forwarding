<#
Builds the trimmed public Brief Desk and pushes it to the GitHub Pages repo.
The Pages repo is a separate clone so this project's working tree never goes public.

Usage:
    .\publish_pages.ps1 -Repo OWNER/brief-desk [-CloneDir D:\vc-personal-projects\brief-desk-pages]
#>
param(
    [Parameter(Mandatory = $true)][string]$Repo,
    [string]$CloneDir = "D:\vc-personal-projects\brief-desk-pages"
)

$ErrorActionPreference = "Stop"
$root = Resolve-Path (Join-Path $PSScriptRoot "..\..")

if (-not (Test-Path (Join-Path $CloneDir ".git"))) {
    gh repo clone $Repo $CloneDir
    if ($LASTEXITCODE -ne 0) { throw "Could not clone $Repo into $CloneDir" }
}

# Pages serves from gh-pages so the daily refresh never commits to main.
# A brand-new repo has no remote branch yet, so there is nothing to pull on the first run.
$branch = "gh-pages"
git -C $CloneDir ls-remote --exit-code --heads origin $branch | Out-Null
if ($LASTEXITCODE -eq 0) {
    git -C $CloneDir fetch --quiet origin $branch
    git -C $CloneDir checkout --quiet -B $branch "origin/$branch"
    if ($LASTEXITCODE -ne 0) { throw "Could not check out $branch in $CloneDir" }
} else {
    git -C $CloneDir checkout --quiet -B $branch
}

$env:PYTHONIOENCODING = "utf-8"
python (Join-Path $root "heinlein\scripts\build_dashboard.py") --public --repo $Repo --out (Join-Path $CloneDir "index.html")
if ($LASTEXITCODE -ne 0) { throw "Public build failed" }

# Pages would otherwise run Jekyll over the page for no benefit.
$nojekyll = Join-Path $CloneDir ".nojekyll"
if (-not (Test-Path $nojekyll)) { New-Item -ItemType File $nojekyll | Out-Null }

git -C $CloneDir add index.html .nojekyll
git -C $CloneDir diff --cached --quiet
if ($LASTEXITCODE -eq 0) { Write-Output "No change to publish."; exit 0 }

$stamp = Get-Date -Format "yyyy-MM-dd HH:mm"
git -C $CloneDir commit --quiet -m "chore(desk): refresh $stamp"
git -C $CloneDir push --quiet -u origin "HEAD:$branch"
if ($LASTEXITCODE -ne 0) { throw "Push failed" }
Write-Output "Published to https://$($Repo.Split('/')[0].ToLower()).github.io/$($Repo.Split('/')[1])/"
