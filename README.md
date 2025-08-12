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


📜 Licença
Este projeto está sob a licença MIT — use e modifique livremente.
