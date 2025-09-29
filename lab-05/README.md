# Desafio de Projeto - Microsoft Azure AZ-900
### Configurando Recursos e Dimensionamentos em Máquinas Virtuais na Azure


- [Criando uma VM](#criando-uma-vm)
- [Conectando via Área de Trabalho Remota](#conectando-via-área-de-trabalho-remota-e-instalando-o-iis)
- [Finalizando](#finalizando-limpando-recursos-ou-configurando-auto-desligamento)

#### Criando uma VM:
Após acessar a conta no portal da Azure, basta buscar por “Máquinas Virtuais”, clicar em “Criar” e configurar os detalhes da instância, como nome, o sistema operacional sugerido, credenciais de administrador e as regras de acesso (RDP e HTTP). Finalize a criação após a validação e acesse a VM pelo botão “Ir para o recurso”.

#### Conectando via Área de Trabalho Remota e Instalando o IIS
Com a VM criada, conecte-se a ela usando o protocolo RDP. Baixe o arquivo de conexão, insira suas credenciais e acesse o ambiente virtual. Dentro da VM, abra o PowerShell e execute o comando 'Install-WindowsFeature -name Web-Server -IncludeManagementTools' para instalar o servidor web IIS. Após a instalação, copie o IP da VM e cole no navegador para visualizar a página padrão do IIS.


#### Finalizando: Limpando Recursos ou Configurando Auto-Desligamento
Quando terminar o uso, você pode excluir o grupo de recursos para remover a VM e todos os componentes associados. Se quiser manter a VM, configure o recurso de desligamento automático para evitar cobranças desnecessárias. Basta acessar a opção “Auto-shutdown”, definir o horário desejado e salvar.

**Referências:**
[Quickstart: Create a Windows virtual machine in the Azure portal](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/quick-create-portal)


---

⭐ Este desafio faz parte das atividades do bootcamp [Microsoft - Azure AZ-900 da DIO](https://web.dio.me/track/microsoft-azure-az-900).