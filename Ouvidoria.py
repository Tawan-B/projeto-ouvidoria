from operacoesbd import *

opcao = 1

conexao = criarConexao("localhost", "root", "12345", "unxyz")

while opcao != 7:
    print("Universidade XYZ ~ Ouvidoria:"
          "\n1) Listagem das Manifestações"
          "\n2) Criar uma nova Manifestação"
          "\n3) Excluir Manifestação"
          "\n4) Alterar Manifestação"
          "\n5) Pesquisar uma manifestação por código"
          "\n6) Pesquisar manifestação por nome"
          "\n7) Sair do Sistema")

    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        consultaListar = "select * from Universidade"
        print("Lista das Manifestações:")
        manifestacoes = listarBancoDados(conexao, consultaListar)

        if len(manifestacoes) == 0:
            print("Não existem manifestações para serem exibidas!")

        else:
            print("Lista de Manifestações:")
            for item in manifestacoes:
                print(f"- Manifestação: {item[1]} | Criador: {item[2]}")
                ##print(f"Até o momento, o sistema possui exatas {len(manifestacoesTamanho)} manifestações")

    elif opcao == 2:
        consultaInsercao = "insert into Universidade(manifestacao, criador) values (%s,%s)"
        novaManifestacao = input("Descreva a nova Manifestação: ")
        criador = input("Digite o nome do autor: ")
        dados = [ novaManifestacao, criador]
        codigonovo = insertNoBancoDados(conexao, consultaInsercao, dados )
        print(f"Manifestação cadastrada com sucesso. O seu código é", codigonovo)

    elif opcao == 3:
        consultaExcluir = "delete from Universidade where codigo = %s"
        codigoRemover = int(input("Por favor, informe o código da manifestação a remover: "))
        valor = [codigoRemover]
        exclusao = excluirBancoDados(conexao, consultaExcluir, valor)

        if exclusao > 0:
            print(f"Manifestação {codigoRemover} excluída!")

        else:
            print("Manifestação não existe!")

    elif opcao == 4:
        consultaAlterar = "update Universidade set manifestacao = %s where codigo = %s"
        codigoAlterar = int(input("Por favor, informe o código da manifestação a alterar: "))
        manifestacaoAlterada = input("Digite a nova manifestação: ")
        valor = [manifestacaoAlterada, codigoAlterar]
        manifestacoes = atualizarBancoDados(conexao, consultaAlterar, valor)

        if manifestacoes > 0:
            print(f"Manifestação {codigoAlterar} alterada com sucesso!")

        else:
            print("Não há manifestação com esse código.")

    elif opcao == 5:
        codigoManifestacao = int(input("Por favor, informe o código da manifestação: "))

        consultaListar = "select * from Universidade where codigo = %s"
        valor = [codigoManifestacao]
        manifestacoes = listarBancoDados(conexao, consultaListar, valor)

        if len(manifestacoes) == 0:
            print("Não há manifestação com esse código.")

        else:
            for item in manifestacoes:
                print("Manifestação:", item[1], "\nCriador:", item[2])

    elif opcao == 6:
        criador = input("Por favor, informe o criador da manifestação: ")

        consultaListar = "select * from Universidade where criador = %s"
        valor = [criador]
        manifestacoes = listarBancoDados(conexao, consultaListar, valor)

        if len(manifestacoes) == 0:
            print("Não há manifestação com esse criador.")

        else:
            for item in manifestacoes:
                print("Manifestação:", item[1])

    elif opcao == 7:
        print("Agradecemos sua contribuição! Sua opinião é essencial para a melhoria da nossa universidade.")
        encerrarConexao(conexao)
        break

    else:
        print("Opção inválida.")