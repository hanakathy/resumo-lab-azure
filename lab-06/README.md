# Desafio de Projeto - Microsoft Azure AZ-900
### Dominando o Armazenamento na Azure

#### Contas de Armazenamento:
Uma conta de armazenamento do Azure reúne todos os objetos de dados como blobs, arquivos, filas e tabelas, oferecendo um espaço exclusivo acessível globalmente via HTTP/HTTPS. Os dados são seguros, altamente disponíveis, duráveis e escaláveis. Existem diferentes tipos de contas com recursos e preços variados, como Data Lake para análise de grandes volumes, contas premium com SSDs para alto desempenho, e opções com redundância geográfica. Após a criação, não é possível alterar o tipo da conta, sendo necessário criar uma nova e migrar os dados.

As cargas de trabalho suportadas incluem: aplicações nativas em nuvem (web, mobile, serverless), análises de dados (real-time, preditiva, emocional), computação de alto desempenho (HPC), backup e arquivamento para recuperação de desastres, e inteligência artificial/machine learning com uso intensivo de GPU e acesso rápido aos dados. A Microsoft recomenda configurações específicas para cada tipo de carga, como ZRS para análises e camadas de acesso frio para backups, com impacto direto nos custos.

Cada conta possui um namespace único com endpoints que formam os endereços dos dados. Há dois tipos: padrão (até 500 contas por região com aumento de cota) e zona DNS (até 5500 contas por região). É possível configurar domínios personalizados e recomenda-se evitar dependência de IPs em cache e respeitar o TTL dos registros DNS para garantir estabilidade no acesso.

Os endpoints padrão do Azure Storage seguem um formato fixo com protocolo (preferencialmente HTTPS), nome da conta como subdomínio e domínio do serviço. Isso permite criar URLs previsíveis para acessar objetos, como blobs. Cada endpoint está ligado a uma cadeia de registros DNS (CNAME e A), que podem mudar sem aviso, afetando configurações de DNS privadas. Por isso, recomenda-se não depender da estrutura desses registros e respeitar o TTL para evitar falhas.

A conta de armazenamento pode ser migrada ou atualizada conforme necessário, e a Microsoft oferece ferramentas para importar dados de ambientes locais ou outras nuvens. Todos os dados são criptografados automaticamente. A cobrança é feita com base em fatores como região, tipo de conta, camada de acesso, capacidade, redundância, transações e transferência de dados entre regiões. O Azure Cost Management ajuda a controlar gastos com alertas e análises.

Contas legadas e modelos clássicos foram descontinuados, sendo recomendada a migração para o modelo Azure Resource Manager. A conta GPv2 é indicada para a maioria dos casos, com possibilidade de upgrade sem interrupções. Os limites de escalabilidade (ingresso e egresso de dados) podem ser ampliados mediante solicitação ao suporte.

**Referências:**
[Storage Account Overview](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview)

---

⭐ Este desafio faz parte das atividades do bootcamp [Microsoft - Azure AZ-900 da DIO](https://web.dio.me/track/microsoft-azure-az-900)