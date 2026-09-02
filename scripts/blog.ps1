param(
  [ValidateSet("build", "serve")]
  [string]$Command = "serve",

  [Parameter(ValueFromRemainingArguments = $true)]
  [string[]]$JekyllArguments
)

$repositoryRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")).Path
$rubyEnvironmentRoot = Join-Path (Split-Path $repositoryRoot) "blog_github_venv"
$bundleExecutable = Join-Path $rubyEnvironmentRoot "bin\bundle.bat"

if (-not (Test-Path -LiteralPath $bundleExecutable)) {
  throw "Ruby environment not found at $rubyEnvironmentRoot"
}

$env:PATH = "$rubyEnvironmentRoot\bin;$rubyEnvironmentRoot\msys64\ucrt64\bin;$env:PATH"

Push-Location $repositoryRoot
try {
  & $bundleExecutable exec jekyll $Command @JekyllArguments
  if ($LASTEXITCODE -ne 0) {
    throw "Jekyll $Command failed with exit code $LASTEXITCODE"
  }
}
finally {
  Pop-Location
}
