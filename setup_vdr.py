import os

# --- ESTRUTURA DE PASTAS E ARQUIVOS DO VIRTUAL DATA ROOM ---
VDR_STRUCTURE = {
    "1_ESTRATEGIA_E_MERCADO": [
        "1.1_Plano_de_Negocios_MAUAX_v1.0.pdf"
    ],
    "2_FINANCEIRO": [
        "2.1_Modelo_Financeiro_Detalhado_MAUAX.xlsx",
        "2.2_Analise_de_Sensibilidade_e_Cenarios.pdf"
    ],
    "3_JURIDICO_E_GOVERNANCA": [
        "3.1_Acordo_de_Consorcio_MEXX.pdf",
        "3.2_Minuta_Contrato_Investimento_Seed.pdf",
        "3.3_Parecer_Juridico_Estrutura_PPP_e_Tokens.pdf"
    ],
    "4_TECNICO_E_OPERACIONAL": [
        "4.1_Sumario_Estudos_Tecnicos_Preliminares.pdf",
        "4.2_Roadmap_Tecnico_e_Sprints_MVP.pdf"
    ],
    "5_EQUIPE": [
        "5.1_CVs_Lideranca_e_Conselho_MAUAX.pdf"
    ],
    "6_PARCERIAS_ESTRATEGICAS": {
        "Siemens_Energy": [
            "Convite_Conselho_Consultivo_Siemens.pdf",
            "Proposta_Parceria_Estrategica_Siemens_v1.0.pdf"
        ]
        # Futuramente: "NVIDIA/", "Enel/", etc.
    }
}

def create_structure(base_path, structure):
    """
    Função recursiva para criar as pastas e arquivos placeholder.
    """

    for name, content in structure.items():
        current_path = os.path.join(base_path, name)

        if isinstance(content, dict):  # É uma pasta com subpastas
            os.makedirs(current_path, exist_ok=True)
            print(f"✔️  Pasta criada/verificada: {current_path}")
            create_structure(current_path, content)
        
        elif isinstance(content, list): # É uma pasta com arquivos
            os.makedirs(current_path, exist_ok=True)
            print(f"✔️  Pasta criada/verificada: {current_path}")
            for filename in content:
                file_path = os.path.join(current_path, filename)
                if not os.path.exists(file_path):
                    # Cria um arquivo placeholder vazio
                    with open(file_path, 'w') as f:
                        pass 
                    print(f"  📄 Arquivo placeholder criado: {file_path}")

def main():
    print("🚀 Iniciando a estruturação do Virtual Data Room (VDR)...")
    base_directory = os.getcwd()
    
    # Verifica se o script está na pasta correta (deve conter um .git)
    if not os.path.isdir(os.path.join(base_directory, '.git')):
        print("❌ ERRO: Este script deve ser executado na raiz do repositório clonado 'MAUAX-VDR'.")
        return

    create_structure(base_directory, VDR_STRUCTURE)
    
    print("\n✅ Estrutura do Data Room criada com sucesso!")
    print("➡️ Próximo passo: Popule os arquivos placeholder com o conteúdo final e execute 'git push'.")

if __name__ == "__main__":
    main()
