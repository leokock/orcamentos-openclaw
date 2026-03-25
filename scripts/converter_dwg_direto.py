#!/usr/bin/env python3.11
"""
Converte DWG para DXF usando ODA File Converter via subprocess (chamada direta)
"""
import sys
import subprocess
from pathlib import Path
import tempfile
import shutil

# Caminho do ODA File Converter
ODA_EXEC = Path.home() / "bin/ODAFileConverter.app/Contents/MacOS/ODAFileConverter"

def converter_dwg_para_dxf(dwg_path, dxf_path=None):
    """
    Converte DWG para DXF usando ODA File Converter (chamada direta)
    
    Args:
        dwg_path: Caminho do arquivo DWG de entrada
        dxf_path: Caminho do arquivo DXF de saída (None = mesmo nome)
    """
    
    dwg_path = Path(dwg_path).resolve()
    
    if not dwg_path.exists():
        print(f"❌ Arquivo não encontrado: {dwg_path}")
        sys.exit(1)
    
    if dxf_path is None:
        dxf_path = dwg_path.with_suffix('.dxf')
    else:
        dxf_path = Path(dxf_path).resolve()
    
    # Criar diretórios temporários para conversão
    temp_in = Path(tempfile.mkdtemp())
    temp_out = Path(tempfile.mkdtemp())
    
    try:
        print(f"🔄 Convertendo DWG → DXF...")
        print(f"  Entrada:  {dwg_path}")
        print(f"  Saída:    {dxf_path}")
        
        # Verificar se ODA File Converter existe
        if not ODA_EXEC.exists():
            print(f"❌ ODA File Converter não encontrado em: {ODA_EXEC}")
            sys.exit(1)
        
        print(f"\n✅ ODA File Converter encontrado")
        
        # Copiar DWG para pasta temporária
        temp_dwg = temp_in / dwg_path.name
        shutil.copy2(dwg_path, temp_dwg)
        
        # Sintaxe do ODA File Converter (CLI):
        # ODAFileConverter <input_folder> <output_folder> <output_version> <output_type> <recursive> <audit>
        # Versões: ACAD9, ACAD10, ACAD12, ACAD13, ACAD14, ACAD2000, ACAD2004, ACAD2007, ACAD2010, ACAD2013, ACAD2018
        # Tipos: DWG, DXF, DXB
        
        cmd = [
            str(ODA_EXEC),
            str(temp_in),      # Input folder
            str(temp_out),     # Output folder
            "ACAD2018",        # Output version
            "DXF",             # Output type
            "0",               # Recursive (0=false, 1=true)
            "1"                # Audit (0=false, 1=true)
        ]
        
        print(f"\n⏳ Executando conversão...")
        print(f"   Comando: {' '.join(cmd)}")
        
        # Executar conversão
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300  # 5 minutos de timeout
        )
        
        print(f"\n📋 Saída do ODA File Converter:")
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("⚠️  Erros/avisos:")
            print(result.stderr)
        
        # Verificar se a conversão foi bem-sucedida
        converted_dxf = temp_out / dwg_path.with_suffix('.dxf').name
        
        if not converted_dxf.exists():
            print(f"\n❌ Conversão falhou — arquivo DXF não foi gerado")
            print(f"   Esperado: {converted_dxf}")
            sys.exit(1)
        
        # Criar diretório de saída se não existir
        dxf_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Copiar arquivo convertido para destino final
        shutil.copy2(converted_dxf, dxf_path)
        
        print(f"\n✅ Conversão concluída com sucesso!")
        print(f"📄 Arquivo DXF salvo em: {dxf_path}")
        
        # Verificar tamanho do arquivo gerado
        if dxf_path.exists():
            size_mb = dxf_path.stat().st_size / (1024 * 1024)
            print(f"📊 Tamanho: {size_mb:.2f} MB")
        
        return dxf_path
        
    except subprocess.TimeoutExpired:
        print("\n❌ Conversão excedeu o tempo limite (5 minutos)")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        # Limpar arquivos temporários
        try:
            shutil.rmtree(temp_in)
            shutil.rmtree(temp_out)
        except:
            pass

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python3.11 converter_dwg_direto.py <arquivo.dwg> [arquivo.dxf]")
        print("\nExemplo:")
        print("  python3.11 converter_dwg_direto.py projeto.dwg")
        print("  python3.11 converter_dwg_direto.py projeto.dwg saida.dxf")
        sys.exit(1)
    
    dwg_file = sys.argv[1]
    dxf_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    converter_dwg_para_dxf(dwg_file, dxf_file)
