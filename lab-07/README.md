# Desafio de Projeto - Microsoft Azure AZ-900
### Entendendo sobre Segurança e Identidade na Azure

- [Microsoft Entra ID](#microsoft-entra-id)
- [Conceitos Fundamentais de Identidade e Acesso](#conceitos-fundamentais-de-identidade-e-acesso)
- [Criação de Usuários](#criação-de-usuários)

#### Microsoft Entra ID
O Microsoft Entra ID é o produto principal da plataforma Microsoft Entra. Trata-se de um serviço de gerenciamento de identidade e acesso baseado em nuvem que oferece os recursos essenciais de autenticação, políticas e proteção para garantir a segurança de usuários, dispositivos, aplicativos e recursos. Cada novo diretório do Microsoft Entra inclui um domínio inicial, como contoso.onmicrosoft.com, sendo possível adicionar os domínios da sua organização.

Assinantes do Microsoft 365, Azure ou Dynamics CRM Online já utilizam o Microsoft Entra ID, pois todo locatário dessas plataformas é automaticamente um locatário do Entra. Assim, é possível começar a gerenciar o acesso aos aplicativos em nuvem integrados imediatamente.

#### Conceitos Fundamentais de Identidade e Acesso
O gerenciamento de identidade e acesso garante que as pessoas, máquinas e componentes de software certos acessem os recursos adequados no momento certo. Primeiro, o usuário ou sistema precisa provar sua identidade. Em seguida, o acesso é concedido ou negado conforme as permissões definidas.

**Tipos de usuários em locatários corporativos:**
- Membro interno: geralmente funcionários em tempo integral da organização.
- Convidado interno: possui conta no locatário, mas com privilégios de convidado.
- Membro externo: autentica com conta externa, mas tem acesso como membro.
- Convidado externo: autentica externamente e possui privilégios de convidado.

A função de menor privilégio recomendada varia conforme o tipo de usuário e a necessidade de atribuição de funções no Entra. Sempre que possível, deve-se optar pela função menos privilegiada.

#### Criação de Usuários
**Informações básicas para criação de usuário:**
Na aba "Básico", são definidos os campos essenciais para criar um novo usuário.

- Nome principal do usuário: insira um nome único e selecione o domínio após o símbolo @.
- Apelido de e-mail: se diferente do nome principal, desmarque a opção de derivação e insira manualmente.
- Nome de exibição: insira o nome completo do usuário.
- Senha: defina uma senha para o primeiro acesso, desmarcando a geração automática se quiser personalizar.
- Conta habilitada: marcada por padrão; desmarque para impedir o acesso inicial. Essa opção substitui o antigo "Bloquear acesso".

**Referências:**
1. [What is Microsoft Entra?](https://learn.microsoft.com/en-us/entra/fundamentals/what-is-entra)
2. [Identity and access management fundamental concepts](
https://learn.microsoft.com/en-us/entra/fundamentals/identity-fundamental-concepts)
3. [Usuários](
https://learn.microsoft.com/en-us/entra/fundamentals/how-to-create-delete-users)


---

⭐ Este desafio faz parte das atividades do bootcamp [Microsoft - Azure AZ-900 da DIO](https://web.dio.me/track/microsoft-azure-az-900).