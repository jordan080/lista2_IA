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
        return ",".join(self.left) + "->" + self.right

class MixedChaining:

    def __init__(self, file_name):
        self.iteration = 0

        self.current_goals = []
        self.found_facts = []
        self.road = []
        self.obj_var = []

        self.rules, self.facts, self.obj_var = self.read_data(file_name)

        result = self.controller(self.rules, self.facts, self.obj_var)

        if result == None:
            print('Fim da execução')
        else:
            print(result)

    def do_backward_chaining(self, goal):
        for rule in self.rules:
            if rule.right == goal:

                for new_goal in rule.left:
                    if new_goal not in self.facts:
                        flag = self.get_new_info(new_goal)
                        if flag == True:
                            return True
                        else:
                            return False

    def get_new_info(self, goal):
        while True:
            new_fact = input("Isto é verdade?: {} ".format(goal))
            if new_fact in ['Sim', 'sim', 'Não', 'não']:
                break
            else:
                print("Tente novamente. Responda com sim ou não")

        if new_fact == 'Sim' or new_fact == 'sim':
            self.facts.append(goal)
            return True
        elif new_fact == 'Não' or new_fact == 'não':
            return False

    def forward_chaining(self, rules, facts, goal):
        iteration = 0
        result = None

        while goal not in facts:
            rule_applied = False
            iteration += 1

            for rule in rules:

                if rule.flag1:
                    continue

                if rule.flag2:
                    continue

                if rule.right in facts:
                    rule.flag2 = True
                    continue

                missing = rule.follows(facts)

                if missing is None:
                    rule_applied = True
                    rule.flag1 = True
                    facts.append(rule.right)
                    result = rule.right
                    break

            if not rule_applied:
                return False, None

        return True, result

    def controller(self, rules, facts, obj_var):
        result = None
        for obj in obj_var:
            self.goal = obj
            flag = False

            while flag == False:
                flag, result = self.forward_chaining(rules, facts, self.goal)

                if flag:
                    print('Resultado: ', result)

                    while True:
                        question = input("Está satisfeito? ")
                        if question in ['Sim', 'sim', 'Não', 'não']:
                            break
                        else:
                            print("Tente novamente. Responda com sim ou não")
                    
                    if question == 'Sim' or question == 'sim':
                        exit()

                    break

                flag_2 = self.do_backward_chaining(self.goal)
                if not flag_2:
                    break
        
        return result

    def read_data(self, file_name):
        rules = []
        facts = []
        obj_var = []

        file = open(file_name, "r")
        read_state = 0

        for line in file:
            line = line.replace("\n", "")

            if line == "":
                read_state += 1
                continue
            if line[0] == '#':
                continue

            line = line.split(" ")

            if read_state == 0:
                right = line[0]
                left = line[1:]
                rules.append(Rule(left, right))
                obj_var.append(right)

            if read_state == 1:
                facts = line

            if read_state > 2:
                self.output += "Formatação incorreta do arquivo. Por favor, tente novamente."
                return [], [], []

        return rules, facts, obj_var

    def print_results(self, result, road, goal):

        if result:
            if len(road) == 0:
                self.output += "  1) Objetivo %s entre os fatos.\n" % goal
                self.output += "  2) Caminho vazio.\n"
            else:
                self.output += "  1) Objetivo %s derivado.\n" % goal
                self.output += "  2) Caminho: %s.\n" % ", ".join(road)
        else:
            self.output += "  1) Objetivo %s inalcançável.\n" % goal