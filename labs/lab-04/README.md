# Desafio de Projeto - Microsoft Azure AZ-900
### Construindo Arquiteturas no Azure

Componentes da Arquitetura do Azure:

- [Infraestrutura Global do Azure](#infraestrutura-global-do-azure)
- [Microsoft Datacenters](#microsoft-datacenters)
- [SQL Server em VMs do Azure](#sql-server-em-vms-do-azure)

#### Infraestrutura Global do Azure
A Azure dispõe de uma ampla rede global, que contribui para reduzir a latência e garantir a acessibilidade dos serviços aos clientes. Ela oferece opções de conformidade, mecanismos de tolerância a falhas e modelos de precificação que ajudam a identificar a localização mais adequada às exigências dos usuários. Conforme o tipo de serviço requisitado, existe uma área geográfica pronta para suprir essa necessidade, aproximando os recursos da plataforma dos usuários dos consumidores da Azure.

#### Microsoft Datacenters
Os datacenters oferecem a base física necessária para sustentar as tecnologias atuais. Eles impulsionam a Microsoft Cloud, permitindo que você utilize com praticidade os serviços digitais para guardar documentos, obter programas e rodar aplicações. Os datacenters da Microsoft contam com extensas fileiras de servidores, responsáveis por entregar as informações aos usuários finais. A empresa dispõe de uma equipe altamente capacitada que, mesmo diante de imprevistos ou calamidades, atua nos bastidores para manter o funcionamento contínuo dos centros de dados. Isso inclui a implementação de sistemas redundantes, ou seja, quando um datacenter enfrenta falhas e se torna inacessível, outro entra em ação imediatamente, assegurando a continuidade dos serviços sem que os consumidores percebam qualquer interrupção.

A Microsoft Cloud também disponibiliza mecanismos para duplicar dados entre diversos datacenters, garantindo aos consumidores um acesso mais estável às suas informações, mesmo em caso de falhas em uma região específica. A Microsoft administra uma malha de centenas de centros de dados protegidos, distribuídos por dezenas de nações e interligados por centenas de milhares de quilômetros de cabos de fibra óptica, permitindo que os serviços estejam fisicamente próximos ao ponto de acesso do usuário. Além disso, a empresa segue investindo fortemente em infraestrutura de centros de dados para atender à crescente procura por soluções de inteligência artificial (IA) e serviços em nuvem, com mais de 70 milhões de regiões já anunciadas.

#### Grupo de recursos
Um Grupo de Recursos funciona como um agrupador que permite administrar elementos vinculados a uma solução no Azure. Utilizar esse agrupamento facilita a sincronização de modificações entre os componentes associados. É possível aplicar uma atualização ao grupo e garantir que todos os itens sejam modificados de forma integrada. Quando a solução não for mais necessária, o grupo pode ser removido, eliminando automaticamente todos os seus elementos.

Cada item só pode pertencer a um único grupo por vez, mas pode ser incluído, retirado ou transferido entre grupos conforme necessário. Embora os recursos possam estar distribuídos em diferentes localidades, é aconselhável mantê-los na mesma região. O grupo também pode delimitar o alcance de permissões administrativas. É possível atribuir marcadores (tags) ao grupo, embora os recursos internos não herdem essas marcações, servindo como uma forma de localizar os grupos com mais facilidade. Um recurso pode interagir com outros em grupos distintos, especialmente quando estão relacionados, mas possuem ciclos de vida diferentes. Além disso, é permitido configurar até 800 unidades de um mesmo tipo de recurso por grupo, com exceções para determinados tipos que não seguem esse limite.

**Referências:**
1. [Global Infrastructure](https://azure.microsoft.com/pt-br/explore/global-infrastructure/)
2. [Datacenters](https://datacenters.microsoft.com/)
3. [Grupo de Recursos](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview#resource-groups)

---

⭐ Este desafio faz parte das atividades do bootcamp [Microsoft - Azure AZ-900 da DIO](https://web.dio.me/track/microsoft-azure-az-900).