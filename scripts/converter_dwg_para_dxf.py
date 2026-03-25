#!/usr/bin/env python3.11
"""
Converte arquivos DWG para DXF usando ODA File Converter via ezdxf
"""
import sys
import ezdxf
from ezdxf.addons import odafc
from pathlib import Path

# Configurar caminho do ODA File Converter para macOS
odafc.unix_exec_path = str(Path.home() / "bin/ODAFileConverter.app/Contents/MacOS/ODAFileConverter")

def converter_dwg_para_dxf(dwg_path, dxf_path=None, version="ACAD2018"):
    """
    Converte DWG para DXF usando ODA File Converter
    
    Args:
        dwg_path: Caminho do arquivo DWG de entrada
        dxf_path: Caminho do arquivo DXF de saída (None = mesmo nome)
        version: Versão DXF de saída (ACAD2018, ACAD2013, etc.)
    """
    
    dwg_path = Path(dwg_path)
    
    if not dwg_path.exists():
        print(f"❌ Arquivo não encontrado: {dwg_path}")
        sys.exit(1)
    
    if dxf_path is None:
        dxf_path = dwg_path.with_suffix('.dxf')
    else:
        dxf_path = Path(dxf_path)
    
    print(f"🔄 Convertendo DWG → DXF...")
    print(f"  Entrada:  {dwg_path}")
    print(f"  Saída:    {dxf_path}")
    print(f"  Versão:   {version}")
    
    try:
        # Verificar se o executável existe
        exec_path = Path(odafc.unix_exec_path)
        if not exec_path.exists():
            print(f"❌ ODA File Converter não encontrado em: {odafc.unix_exec_path}")
            print("   Verifique a instalação ou o caminho configurado")
            sys.exit(1)
        
        print(f"\n✅ ODA File Converter encontrado em: {odafc.unix_exec_path}")
        
        # Converter usando ezdxf
        print("\n⏳ Processando...")
        odafc.convert(
            source=str(dwg_path),
            dest=str(dxf_path),
            version=version,
            audit=True,
            replace=True
        )
        
        print(f"\n✅ Conversão concluída com sucesso!")
        print(f"📄 Arquivo DXF salvo em: {dxf_path}")
        
        # Verificar tamanho do arquivo gerado
        if dxf_path.exists():
            size_mb = dxf_path.stat().st_size / (1024 * 1024)
            print(f"📊 Tamanho: {size_mb:.2f} MB")
        
        return dxf_path
        
    except odafc.ODAFCNotInstalledError:
        print("❌ ODA File Converter não está instalado ou não está no PATH")
        sys.exit(1)
    except odafc.UnsupportedVersion:
        print(f"❌ Versão DXF não suportada: {version}")
        print("   Versões válidas: ACAD2018, ACAD2013, ACAD2010, ACAD2007, ACAD2004, ACAD2000")
        sys.exit(1)
    except odafc.UnknownODAFCError as e:
        print(f"❌ Erro ao converter: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python3.11 converter_dwg_para_dxf.py <arquivo.dwg> [arquivo.dxf] [versao]")
        print("\nExemplo:")
        print("  python3.11 converter_dwg_para_dxf.py projeto.dwg")
        print("  python3.11 converter_dwg_para_dxf.py projeto.dwg saida.dxf")
        print("  python3.11 converter_dwg_para_dxf.py projeto.dwg saida.dxf ACAD2013")
        sys.exit(1)
    
    dwg_file = sys.argv[1]
    dxf_file = sys.argv[2] if len(sys.argv) > 2 else None
    version = sys.argv[3] if len(sys.argv) > 3 else "ACAD2018"
    
    converter_dwg_para_dxf(dwg_file, dxf_file, version)
