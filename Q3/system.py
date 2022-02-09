import sys

class Rule:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.flag1 = False
        self.flag2 = False

    def follows(self, facts):
        for fact in self.left:
            if fact not in facts:
                return fact
        return None

    def __str__(self):
        premisses = []
        for item in self.left:
            temp = ""
            for key,value in item.items():
                temp = key + " = " + value
            premisses.append(temp)
        for value in self.right:
            conclusion = ""
            for key, value in value.items():
                conclusion = key + " = " + value
        return ",".join(premisses) + " -> " + conclusion

class MixedChaining:

    def __init__(self):
        self.iteration = 0
        self.obj_var = []
        self.facts = []

        self.rules, self.obj_var = self.read_data()
        self.controller(self.rules, self.facts, self.obj_var)

    def do_backward_chaining(self, goal):
        for rule in self.rules:
            for item in rule.right:
                value = item
            if value == goal:
                for new_goal in rule.left:
                    if new_goal not in self.facts:
                        new_goal_key = next(iter(new_goal))
                        if any(new_goal_key in d for d in self.facts):
                            continue
                        new_value = self.get_new_info(new_goal_key, goal)
                        if new_goal == new_value:
                            return True
                        else:
                            return False

    def get_new_info(self, item, goal):
        answer = input("Digite o valor de: {} ".format(item))

        while answer == "Porque?" or answer == 'porque?':
            temp = next(iter(goal))
            print("Para saber se {} é verdade, primeiro preciso saber de {}".format(temp, item))
            answer = input("Digite o valor de: {} ".format(item))

        new_value = {}
        new_value[item] = answer
        self.facts.append(new_value)
        return new_value

    def forward_chaining(self, rules, facts, goal):
        iteration = 0
        result = None

        while goal not in self.facts:
            rule_applied = False
            iteration += 1

            for rule in rules:
                for item in rule.right:
                    value = item

                if rule.flag1:
                    continue

                if rule.flag2:
                    continue

                if value in self.facts:
                    rule.flag2 = True
                    continue

                missing = rule.follows(self.facts)

                if missing is None:
                    rule_applied = True
                    rule.flag1 = True
                    self.facts.append(value)
                    result = value
                    break

            if not rule_applied:
                return False, None

        return True, result

    def controller(self, rules, facts, obj_var):
        result = None
        for item in obj_var:
            goal = item
            flag = False

            while True:
                flag, result = self.forward_chaining(rules, facts, goal)

                if flag:
                    result = next(iter(result))
                    print('Resultado: ',result)

                    while True:
                        question = input("Está satisfeito? ")
                        if question in ['Sim', 'sim', 'Não', 'não']:
                            break
                        else:
                            print("Tente novamente. Responda com sim ou não")
                    
                    if question == 'Sim' or question == 'sim':
                        print('Fim da execução')
                        exit()
                    
                    break
                
                flag_2 = self.do_backward_chaining(goal)
                if flag_2 == False or flag_2 == None:
                    break

    def read_data(self):
        rules = []
        obj_var = []

        right = []
        left = []
        while True:
            while True:
                print("1 - Premissa")
                print("2 - Conclusão")
                tipo = input('Insira o tipo de valor: ')
                if tipo in ['1','2']:
                    break
                else:
                    print("Tente novamente.")
            
            if tipo == '1':
                atomo = {}
                fato = input('Insira o nome da variável: ')
                valor = input('Insira o valor da variável: ')
                atomo[fato] = valor
                left.append(atomo)
            elif tipo == '2':
                atomo = {}
                fato = input('Insira o nome da variável: ')
                valor = input('Insira o valor da variável: ')
                atomo[fato] = valor
                right.append(atomo)
                obj_var.append(atomo)
                rules.append(Rule(left, right))
                right = []
                left = []

                while True:
                    question = input("Gostaria de continuar? ")
                    if question in ['Sim', 'sim', 'Não', 'não']:
                        break
                    else:
                        print("Tente novamente. Responda com sim ou não")

                if question == 'Não' or question == 'não':
                    return rules, obj_var 

if __name__ == '__main__':
    MixedChaining()