# PowerShell script to launch gemini-cli using npx

Write-Host "Launching gemini-cli via npx..." -ForegroundColor Green
# Using npx (no installation required)
npx https://github.com/google-gemini/gemini-cli $args
