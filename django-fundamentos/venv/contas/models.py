from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


# Colocamos essa função para que o nome da categoria

class Transacao(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)  # max de dígitos e casas decimais
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True,
                                   blank=True)  # o null e o blank tiram a obrigatoriedade de preencher o campo
    # observacoes

    class Meta:
        verbose_name_plural = 'Transações'
        # Esta classe é criada para que o plural de transacao apareça da forma correta.

    def __str__(self):
        return self.descricao
# Esta função trata-se de definir o campo (descricao) que queremos mostrar na aba transação


