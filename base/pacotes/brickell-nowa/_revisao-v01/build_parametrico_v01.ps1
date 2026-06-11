# Builds brickell-nowa-parametrico-v01.xlsx from v00 via Excel COM:
# - CUB atual 3850 -> 3064.10 (Sinduscon CUB/SC residencial medio mai/2026)
# - Updates FONTES_PROJETO row + appends AJUSTES row documenting the v01 fix
# - Full recalc + save
$ErrorActionPreference = 'Stop'
$pkg = 'C:\Users\leona\orcamentos-openclaw\base\pacotes\brickell-nowa'
$src = Join-Path $pkg 'brickell-nowa-parametrico-v00-final.xlsx'
$dst = Join-Path $pkg 'brickell-nowa-parametrico-v01.xlsx'
Copy-Item $src $dst -Force

$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$excel.DisplayAlerts = $false
try {
    $wb = $excel.Workbooks.Open($dst)

    $wsDados = $wb.Worksheets.Item('DADOS_PROJETO')
    $wsDados.Range('B12').Value2 = 3064.10

    $wsFontes = $wb.Worksheets.Item('FONTES_PROJETO')
    $wsFontes.Range('B18').Value2 = 'R$ 3.064,10/m²'
    $wsFontes.Range('C18').Value2 = 'CUB/SC residencial medio Sinduscon, mai/2026 (confirmado em ampli_indexers SC 2026-05 = 3.064,10 e serie Sinduscon publica). v00 usava R$ 3.850, valor sem respaldo na fonte citada.'

    $wsAj = $wb.Worksheets.Item('AJUSTES_V00')
    $wsAj.Range('A9').Value2 = 'DADOS_PROJETO!B12'
    $wsAj.Range('B9').Value2 = 'CUB atual (correcao v01)'
    $wsAj.Range('C9').Value2 = 'R$ 3.850,00 -> R$ 3.064,10'
    $wsAj.Range('D9').Value2 = 'v01: CUB/SC residencial medio Sinduscon mai/2026. O 3.850 do v00 nao existe na fonte citada (ampli_indexers SC 2026-05 = 3.064,10; Comercial = 3.263,60). Corrige Instalacoes (PUs escalam com CUB) e o CUB ratio do painel.'

    $excel.CalculateFullRebuild()
    Start-Sleep -Milliseconds 500
    $wb.Save()
    $wb.Close($true)
    Write-Output 'V01_BUILD_OK'
} finally {
    $excel.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($excel) | Out-Null
    [GC]::Collect(); [GC]::WaitForPendingFinalizers()
}

# Read-back verification
$excel2 = New-Object -ComObject Excel.Application
$excel2.Visible = $false
$excel2.DisplayAlerts = $false
try {
    $wb2 = $excel2.Workbooks.Open($dst, 0, $true)
    $cm = $wb2.Worksheets.Item('CUSTOS_MACROGRUPO')
    $painel = $wb2.Worksheets.Item('PAINEL')
    $inst = $wb2.Worksheets.Item('Instalações')
    Write-Output ("TOTAL_V01={0}" -f $cm.Range('D22').Value2)
    Write-Output ("RSM2_V01={0}" -f $cm.Range('B22').Value2)
    Write-Output ("INSTALACOES_V01={0}" -f $inst.Range('G2').Value2)
    Write-Output ("IMPREVISTOS_V01={0}" -f $cm.Range('D21').Value2)
    Write-Output ("CUBRATIO_V01={0}" -f $painel.Range('B6').Value2)
    Write-Output ("CUSTO_UR_V01={0}" -f $painel.Range('B7').Value2)
    $wb2.Close($false)
} finally {
    $excel2.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($excel2) | Out-Null
    [GC]::Collect(); [GC]::WaitForPendingFinalizers()
}
