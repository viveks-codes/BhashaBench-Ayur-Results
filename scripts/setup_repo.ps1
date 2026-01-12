# PowerShell Script to Setup Git LFS and Push Benchmark Results

$ErrorActionPreference = "Stop"

Write-Host "Checking for Git..." -ForegroundColor Cyan
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error "Git is not installed or not in your PATH. Please install Git for Windows and try again."
    exit 1
}

Write-Host "Initializing Git Repository..." -ForegroundColor Cyan
git init

Write-Host "Setting up Git LFS..." -ForegroundColor Cyan
# Install LFS configuration for this repo
git lfs install

# Track heavy CSV files (benchmark results are large text files)
git lfs track "*.csv"
git add .gitattributes

Write-Host "Adding Files..." -ForegroundColor Cyan
git add .

Write-Host "Committing..." -ForegroundColor Cyan
git commit -m "Initial commit: Benchmark results and analysis (via LFS)"

Write-Host "Setting up Remote..." -ForegroundColor Cyan
git branch -M main
# Using the URL from the blog post
$repoUrl = "https://github.com/viveks-codes/BhashaBench-Ayur-Results.git"

# Check if remote exists, remove if so to be safe
git remote remove origin 2>$null
git remote add origin $repoUrl

Write-Host "Pushing to GitHub..." -ForegroundColor Cyan
Write-Host "NOTE: You may be asked to log in via a browser or token." -ForegroundColor Yellow
git push -u origin main

Write-Host "✅ Done! Results are live at " + $repoUrl -ForegroundColor Green
