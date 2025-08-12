# vm-creation-automation-for-netbox
# 🖥️ Script Interno do NetBox - Criar VM Completa

Este projeto contém um **script interno para o NetBox** que permite criar uma máquina virtual (**Virtual Machine**) já com todos os seus atributos básicos:

- Nome da VM  
- Tenant  
- Site  
- Cluster  
- CPU, Memória e Disco  
- Interface de Rede  
- Endereço IP (alocado automaticamente a partir de um prefixo existente no NetBox)  

Ele é executado diretamente na interface web do NetBox, na aba **Extensões → Scripts**.

---

## 📂 Estrutura do Projeto

O diretório do script no NetBox é:

/opt/netbox/netbox/scripts/

yaml
Copiar
Editar

Dentro dele, o arquivo do script deve ser salvo (por exemplo `criar_vm.py`) com a lógica de criação da VM, interface e IP.

---

## 🚀 Requisitos

- NetBox **4.x** ou superior
- Acesso ao diretório `scripts/` do NetBox
- Tenant, Site, Cluster e Prefix já cadastrados no NetBox
- Permissões para executar scripts internos

---

## 📥 Instalação

> **Atenção**: O diretório `scripts/` do NetBox precisa estar **gravável** (não pode estar somente leitura).  
> Se estiver usando Docker ou Kubernetes, monte um volume para `/opt/netbox/netbox/scripts/`.

### Instalação em Servidor Local
```bash
sudo cp criar_vm.py /opt/netbox/netbox/scripts/
sudo chown netbox:netbox /opt/netbox/netbox/scripts/criar_vm.py
sudo systemctl restart netbox
Instalação em Docker
bash
Copiar
Editar
docker cp criar_vm.py netbox_container:/opt/netbox/netbox/scripts/
docker restart netbox_container
Instalação em Kubernetes
Crie um ConfigMap com o script:

bash
Copiar
Editar
kubectl create configmap netbox-custom-scripts --from-file=criar_vm.py
Monte-o no pod do NetBox em /opt/netbox/netbox/scripts/ e reinicie:

bash
Copiar
Editar
kubectl rollout restart deployment netbox
🛠 Como Usar
Acesse o NetBox.

Vá em Extensões → Scripts.

Selecione Criar VM Completa.

Preencha os campos:

Nome da VM

Tenant

Site

Cluster

CPU, Memória e Disco

Prefixo para IP (ex.: 10.0.0.0/24)

Nome da Interface (opcional)

Clique em Executar.

O NetBox criará automaticamente:

A máquina virtual

Interface de rede

IP atribuído a partir do prefixo selecionado

📌 Observações
O script não cria Prefixos, Sites ou Tenants — eles devem existir previamente.

Caso não haja IP disponível no prefixo escolhido, será exibido um erro.

Campos adicionais como Sistema Operacional podem ser incluídos via Custom Fields no NetBox.

📜 Licença
Este projeto está sob a licença MIT — use e modifique livremente.
