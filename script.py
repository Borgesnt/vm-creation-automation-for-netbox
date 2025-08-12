
Código:

```python
from extras.scripts import Script, StringVar, IntegerVar, ObjectVar
from tenancy.models import Tenant
from virtualization.models import VirtualMachine, Cluster, VMInterface
from dcim.models import Site
from ipam.models import IPAddress, Prefix

class CriarVMCompleta(Script):
    class Meta:
        name = "Criar VM Completa"
        description = "Cria uma VM com interface e IP no NetBox."

    nome_vm = StringVar(description="Nome da VM")
    tenant = ObjectVar(description="Tenant", queryset=Tenant.objects.all())
    site = ObjectVar(description="Site", queryset=Site.objects.all())
    cluster = ObjectVar(description="Cluster", queryset=Cluster.objects.all())
    cpu = IntegerVar(description="CPUs", default=2)
    memoria = IntegerVar(description="Memória (MB)", default=4096)
    disco = IntegerVar(description="Disco (GB)", default=50)
    prefixo = ObjectVar(description="Prefixo para o IP", queryset=Prefix.objects.all())
    nome_iface = StringVar(description="Nome da Interface", default="eth0")

    def run(self, data, commit):
        # Criar VM
        vm = VirtualMachine.objects.create(
            name=data['nome_vm'],
            tenant=data['tenant'],
            site=data['site'],
            cluster=data['cluster'],
            vcpus=data['cpu'],
            memory=data['memoria'],
            disk=data['disco']
        )
        self.log_success(f"VM '{vm.name}' criada.")

        # Criar interface de rede
        iface = VMInterface.objects.create(
            virtual_machine=vm,
            name=data['nome_iface']
        )
        self.log_success(f"Interface '{iface.name}' criada.")

        # Alocar IP livre do prefixo
        ip_livre = data['prefixo'].available_ips.first()
        if not ip_livre:
            self.log_failure(f"Não há IPs livres no prefixo {data['prefixo']}.")
            return

        ip = IPAddress.objects.create(
            address=str(ip_livre),
            assigned_object=iface
        )
        self.log_success(f"IP '{ip.address}' atribuído à interface '{iface.name}'.")
