class FuncionarioCRUD:
    def __init__(self, connection):
        self.connection = connection

    def adicionar_funcionario(self):
        nome = input("Nome do Funcionário: ")
        especialidade = input("Especialidade do Funcionário: ")

        # Exibe os procedimentos disponíveis
        print("Escolha os procedimentos para associar ao funcionário (Digite os IDs, separados por vírgula):")
        self.visualizar_procedimentos()
        procedimento_ids = input("IDs dos procedimentos: ").split(',')

        # Adiciona o funcionário
        sql = "INSERT INTO funcionarios (nome, especialidade) VALUES (%s, %s)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (nome, especialidade))
        self.connection.commit()
        id_funcionario = cursor.lastrowid  # Captura o ID do novo funcionário
        print(f"Funcionário {nome} adicionado com sucesso!")

        # Associa múltiplos procedimentos ao funcionário
        self.associar_procedimentos(id_funcionario, procedimento_ids)

        # Associa disponibilidades ao funcionário
        self.associar_disponibilidade(id_funcionario)

    def editar_funcionario(self):
        id_funcionario = int(input("Digite o ID do funcionário para editar: "))
        novo_nome = input("Novo Nome do Funcionário: ")
        nova_especialidade = input("Nova Especialidade do Funcionário: ")

        # Exibe os procedimentos disponíveis
        print("Escolha os procedimentos para associar ao funcionário (Digite os IDs, separados por vírgula):")
        self.visualizar_procedimentos()
        procedimento_ids = input("IDs dos procedimentos: ").split(',')

        # Atualiza os dados do funcionário
        sql = "UPDATE funcionarios SET nome = %s, especialidade = %s WHERE id = %s"
        cursor = self.connection.cursor()
        cursor.execute(sql, (novo_nome, nova_especialidade, id_funcionario))
        self.connection.commit()
        print(f"Funcionário {id_funcionario} atualizado com sucesso!")

        # Associa múltiplos procedimentos ao funcionário
        self.associar_procedimentos(id_funcionario, procedimento_ids)

        # Associa novas disponibilidades ao funcionário
        self.associar_disponibilidade(id_funcionario)

    def associar_procedimentos(self, id_funcionario, procedimento_ids):
        cursor = self.connection.cursor()
        for id_procedimento in procedimento_ids:
            sql = """
            INSERT INTO funcionarios_procedimentos (funcionario_id, procedimentos_id) 
            VALUES (%s, %s)
            """
            cursor.execute(sql, (id_funcionario, int(id_procedimento)))
        self.connection.commit()
        print(f"Procedimentos associados ao funcionário {id_funcionario} com sucesso!")

    def associar_disponibilidade(self, id_funcionario):
        print("Escolha as disponibilidades para associar ao funcionário (Digite os IDs, separados por vírgula):")
        self.visualizar_disponibilidades()  # Exibe as disponibilidades existentes
        disponibilidades_ids = input("IDs das disponibilidades: ").split(',')

        cursor = self.connection.cursor()
        for id_disponibilidade in disponibilidades_ids:
            sql = """
            INSERT INTO funcionarios_disponibilidades (funcionario_id, disponibilidade_id) 
            VALUES (%s, %s)
            """
            cursor.execute(sql, (id_funcionario, int(id_disponibilidade)))
        self.connection.commit()
        print(f"Disponibilidades associadas ao funcionário {id_funcionario} com sucesso!")

    def visualizar_funcionarios(self):
        sql = "SELECT * FROM funcionarios"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        funcionarios = cursor.fetchall()
        for funcionario in funcionarios:
            print(f"ID: {funcionario[0]}, Nome: {funcionario[1]}, Especialidade: {funcionario[2]}")

    def deletar_funcionario(self):
        id_funcionario = int(input("Digite o ID do funcionário para deletar: "))
        sql = "DELETE FROM funcionarios WHERE id = %s"
        cursor = self.connection.cursor()
        cursor.execute(sql, (id_funcionario,))
        self.connection.commit()
        print(f"Funcionário {id_funcionario} deletado com sucesso!")

    def visualizar_procedimentos(self):
        sql = "SELECT * FROM procedimentos"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        procedimentos = cursor.fetchall()
        for procedimento in procedimentos:
            print(f"ID: {procedimento[0]}, Nome: {procedimento[1]}, Descrição: {procedimento[2]}, Valor: {procedimento[3]}")

    def adicionar_procedimento(self):
        nome = input("Nome do Procedimento: ")
        descricao = input("Descrição do Procedimento: ")
        valor = float(input("Valor do Procedimento: "))

        sql = "INSERT INTO procedimentos (nome, descricao, valor) VALUES (%s, %s, %s)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (nome, descricao, valor))
        self.connection.commit()
        print(f"Procedimento {nome} adicionado com sucesso!")

    def editar_procedimento(self):
        id_procedimento = int(input("Digite o ID do procedimento para editar: "))
        novo_nome = input("Novo Nome do Procedimento: ")
        nova_descricao = input("Nova Descrição do Procedimento: ")
        novo_valor = float(input("Novo Valor do Procedimento: "))

        sql = "UPDATE procedimentos SET nome = %s, descricao = %s, valor = %s WHERE id = %s"
        cursor = self.connection.cursor()
        cursor.execute(sql, (novo_nome, nova_descricao, novo_valor, id_procedimento))
        self.connection.commit()
        print(f"Procedimento {id_procedimento} atualizado com sucesso!")

    def deletar_procedimento(self):
        id_procedimento = int(input("Digite o ID do procedimento para deletar: "))
        sql = "DELETE FROM procedimentos WHERE id = %s"
        cursor = self.connection.cursor()
        cursor.execute(sql, (id_procedimento,))
        self.connection.commit()
        print(f"Procedimento {id_procedimento} deletado com sucesso!")

    def visualizar_disponibilidades(self):
        sql = "SELECT * FROM disponibilidade"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        disponibilidades = cursor.fetchall()
        for disponibilidade in disponibilidades:
            print(f"ID: {disponibilidade[0]}, Turno: {disponibilidade[1]}, Dia: {disponibilidade[2]}")

