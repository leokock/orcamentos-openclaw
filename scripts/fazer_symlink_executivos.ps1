# fazer_symlink_executivos.ps1
# Converte C:\Users\leona\orcamentos-openclaw\executivos em SYMLINK -> _Executivo_IA (Drive).
# O merge ja foi feito (29/05/2026): o Drive _Executivo_IA contem tudo do local (superset).
# Rodar com a pasta OCIOSA: feche Excel/Explorer apontando pra executivos; ideal logo apos reiniciar.
# Mantem backup local (executivos_PRE-SYMLINK-bak) como rede de seguranca - apague depois de validar.

$ErrorActionPreference = "Stop"
$jct    = "C:\Users\leona\openclaw\data\executivos"          # junction do openclaw
$parent = "C:\Users\leona\orcamentos-openclaw"
$locE   = Join-Path $parent "executivos"
$bak    = Join-Path $parent "executivos_PRE-SYMLINK-bak"
$drvE   = "G:\Drives compartilhados\03 CTN Projetos\2. Projetos em Andamento\_Executivo_IA"

if (-not (Test-Path $drvE)) { Write-Error "Drive _Executivo_IA inacessivel - monte o G: primeiro"; exit 1 }
if (Test-Path $bak) { Write-Error "backup ja existe ($bak) - resolva antes"; exit 1 }

# 1) remover a junction do openclaw (so o reparse point)
if (Test-Path $jct) { cmd /c rmdir "$jct" | Out-Null }

# 2) backup-rename do executivos local
try {
  Rename-Item -Path $locE -NewName "executivos_PRE-SYMLINK-bak" -ErrorAction Stop
} catch {
  Write-Host "FALHA no rename (pasta ainda em uso): $($_.Exception.Message)"
  Write-Host "Feche tudo que acessa C:\...\orcamentos-openclaw\executivos (Excel, Explorer, bot Cartesiano) e tente de novo."
  if (-not (Test-Path $jct)) { cmd /c mklink /J "$jct" "$locE" | Out-Null }  # religa junction
  exit 1
}

# 3) criar o symlink executivos -> Drive
try {
  New-Item -ItemType SymbolicLink -Path $locE -Target $drvE -ErrorAction Stop | Out-Null
} catch {
  Write-Host "FALHA no symlink: $($_.Exception.Message) -> revertendo"
  Rename-Item -Path $bak -NewName "executivos"
  if (-not (Test-Path $jct)) { cmd /c mklink /J "$jct" "$locE" | Out-Null }
  exit 1
}

# 4) recriar a junction do openclaw apontando pro executivos (agora symlink -> Drive)
if (-not (Test-Path $jct)) { cmd /c mklink /J "$jct" "$locE" | Out-Null }

# 5) verificar
$i = Get-Item $locE -Force
Write-Host "OK: executivos -> $($i.LinkType) -> $($i.Target -join '')"
Write-Host "junction openclaw: $((Get-Item $jct -Force).LinkType)"
Write-Host "teste leitura: $(Test-Path (Join-Path $locE 'villa-vauban-r01\04-relatorios\RELATORIO-FINAL.md'))"
Write-Host "Backup local preservado em: $bak  (apague apos validar que tudo abre pelo Drive)"
