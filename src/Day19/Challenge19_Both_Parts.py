def parse_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read().split('\n\n')

    workflows_section = content[0].split('\n')
    workflows = {}

    for line in workflows_section:
        if '{' in line:
            name, rules_str = line.split('{', 1)
            rules = rules_str.strip().rstrip('}').split(',')
            workflows[name] = rules

    return workflows


def process_part(part, workflows, current_workflow):
    for rule in workflows[current_workflow]:
        if ':' in rule:
            condition, action = rule.split(':')
            if action == 'R':
                return 'R'
            if '>' in condition:
                key, value = condition.split('>')
                if key in part and part[key] > int(value):
                    return action
            elif '<' in condition:
                key, value = condition.split('<')
                if key in part and part[key] < int(value):
                    return action
        else:
            return rule
    return 'R'


def count_accepted_combinations(workflows, max_value):
    accepted_count = 0
    for x in range(1, max_value + 1):
        for m in range(1, max_value + 1):
            for a in range(1, max_value + 1):
                for s in range(1, max_value + 1):
                    part = {'x': x, 'm': m, 'a': a, 's': s}
                    if process_part(part, workflows, 'in') == 'A':
                        accepted_count += 1
    return accepted_count


file_path = '/example/file/path.txt'
workflows = parse_file(file_path)


max_value = 4000
accepted_combinations_count = count_accepted_combinations(workflows, max_value)
print(accepted_combinations_count)
