from contaBancaria import ContaBancaria

murilo = ContaBancaria('Murilo')

murilo.depositar(40)
murilo.mostrar_saldo()
murilo.depositar(20)
murilo.mostrar_saldo()
murilo.depositar(100)

murilo.sacar(200)
murilo.mostrar_saldo()