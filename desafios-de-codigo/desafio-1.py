# Os desafios apresentados aqui têm como objetivo principal exercitar os conceitos aprendidos e proporcionar um primeiro contato com lógica de programação.

# Desafio: Associando os Componentes de Arquitetura do Azure
# Descrição: Para fortalecer seus conhecimentos, complete o código deste desafio, associando os principais componentes de arquitetura do Azure com suas respectivas definições.

# Entrada: A entrada consistirá no nome de um componente do Azure, para o qual você deve retornar a descrição correspondente.

# Saída: A saída esperada é a descrição associada ao componente fornecido como entrada.

# Dicionário com componentes do Azure e suas descrições
componentes = {
    "Azure Virtual Machines": "máquinas virtuais na nuvem para hospedar sistemas e aplicações",
    "Azure Functions": "execução de código sob demanda sem necessidade de gerenciar servidores",
    "Azure Blob Storage": "armazenamento escalável para grandes volumes de dados não estruturados",
    "Azure Virtual Network": "rede privada para conectar recursos de forma segura no Azure"
}

# Leitura da entrada
entrada = input()

# Imprime a descrição correspondente
print(componentes[entrada])