z = ['junior', 'filho', 'filha', 'sobrinho', 'sobrinha', 'neto', 'neta']


def org(name):
    name_list = name.split()
    if any(i in z for i in name_list):
        org_name = name_list[-2].upper() + ' ', name_list[-1].upper() + ', ', name_list[0].capitalize()
        final_org_name = ''.join(org_name)
        return final_org_name
    elif len(name_list) == 1:
        org_name = name_list[1].capitalize()
        final_org_name = ''.join(org_name)
        return final_org_name
    else:
        org_name = name_list[-1].upper() + ', ', name_list[0].capitalize()
        final_org_name = ''.join(org_name)
        return final_org_name


name = input(str())
print('Autor: {}'.format(org(name)))
