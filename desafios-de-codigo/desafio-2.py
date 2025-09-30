# Os desafios apresentados aqui têm como objetivo principal exercitar os conceitos aprendidos e proporcionar um primeiro contato com lógica de programação.

# Desafio: Associando Componentes e Serviços do Azure com Lógica de Programação
# Descrição: Neste desafio, você vai associar os principais serviços de identidade, acesso e segurança da Azure com suas respectivas definições. O objetivo é reforçar o entendimento de como o Azure lida com proteção, autenticação e gerenciamento de identidades.

# Entrada: A entrada consistirá no nome de um serviço ou recurso de segurança/identidade da Azure, para o qual você deve retornar a descrição correspondente.

# Saída: A saída esperada é a descrição associada ao serviço fornecido como entrada.

# Dicionário com os serviços de segurança e identidade do Azure e suas descrições
servicos = {
    "Azure Active Directory": "gerenciamento de identidades e acessos na nuvem",
    "Azure Key Vault": "armazenamento seguro de chaves, segredos e certificados",
    "Azure Security Center": "monitoramento e gerenciamento centralizado da segurança no Azure",
    "Azure Multi-Factor Authentication": "proteção adicional exigindo múltiplas formas de autenticação"
}


# Leitura da entrada
entrada = input()


# Imprime a descrição correspondente
print(servicos[entrada])
