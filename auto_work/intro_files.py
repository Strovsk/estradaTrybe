import os

main_path = '/home/strovsk/Desktop/github/trybe-tarefas/Trybe/'

base_structure = '''---
tags: {}
---

# [[{}]]

{}

# Pastas filhas

{}

# Arquivos filhos

{}
'''

layer_1 = os.listdir(main_path) # Modules
layer_2 = [] # Blocks
layer_3 = [] # Subjects
layer_4 = [] # Subject_Childrens

folders_layer_1 = ['- [['+f+']]' for f in layer_1 if os.path.isdir(main_path+f)]
files_layer_1 = ['- [['+f+']]' for f in layer_1 if os.path.isfile(main_path+f)]

print('writing module '+main_path+'/'+'trybe_sumary.md')
file_module = open(main_path+'trybe_sumary.md', 'w')
file_module.writelines(base_structure.format('index', 'Índice', 'description', '\n'.join(folders_layer_1), '\n'.join(files_layer_1)))
file_module.close()

for module in layer_1:
    if os.path.isdir(main_path+module):
        layer_2 = os.listdir(main_path+module)
        folders_layer_2 = ['- [['+f+']]' for f in layer_2 if os.path.isdir(main_path+module+'/'+f)]
        files_layer_2 = ['- [['+f+']]' for f in layer_2 if os.path.isfile(main_path+module+'/'+f)]

        # colocar condição para escrever somente se o arquivo md não existir
        file_module = open(main_path+module+'/'+module+'.md', 'w')

        print('writing module '+main_path+module+'/'+module+'.md')
        file_module.writelines(base_structure.format('module, dir', module, 'description', '\n'.join(folders_layer_2), '\n'.join(files_layer_2)))
        file_module.close()

    for block in layer_2:
        if os.path.isdir(main_path+module+'/'+block):
            layer_3 = os.listdir(main_path+module+'/'+block)
            folders_layer_3 = ['- [['+f+']]' for f in layer_3 if os.path.isdir(main_path+module+'/'+block+'/'+f)]
            files_layer_3 = ['- [['+f+']]' for f in layer_3 if os.path.isfile(main_path+module+'/'+block+'/'+f)]

            # colocar condição para escrever somente se o arquivo md não existir
            file_module = open(main_path+module+'/'+block+'/'+block+'.md', 'w')

            print('\twriting block '+module+'/'+block+'/'+block+'.md')
            file_module.writelines(base_structure.format('block, dir', block, 'description', '\n'.join(folders_layer_3), '\n'.join(files_layer_3)))
            file_module.close()
        
        for subject in layer_3:
            if os.path.isdir(main_path+module+'/'+block+'/'+subject):
                layer_4 = os.listdir(main_path+module+'/'+block+'/'+subject)
                folders_layer_4 = ['- [['+f+']]' for f in layer_4 if os.path.isdir(main_path+module+'/'+block+'/'+subject+'/'+f)]
                files_layer_4 = ['- [['+f+']]' for f in layer_4 if os.path.isfile(main_path+module+'/'+block+'/'+subject+'/'+f)]

                # colocar condição para escrever somente se o arquivo md não existir
                file_module = open(main_path+module+'/'+block+'/'+subject+'/'+subject+'.md', 'w')

                print('\t\twriting block '+module+'/'+block+'/'+subject+'/'+subject+'.md')
                file_module.writelines(base_structure.format('subject, dir', subject, 'description', '\n'.join(folders_layer_4), '\n'.join(files_layer_4)))
                file_module.close()