import os


# Get the path to the directory you want to make changes to. #
# path = input('Copy and paste the folder path and hit enter.')
path = r'YOUR PATH'
print('\n', "You are working on " +  path, '\n')


def build_changes():
    old_data = input(str('What text needs to be replaced? Place it here ---> :'))
    new_data = input(str('What text will be taking it\'s place? Place it here ---> :'))
    # print('\n', "The text we are finding is" + ' "' + old_data + '".' "")
    # print('\n', "The text we are replacing it with is" + ' "' + new_data + '".' "")
    cont = input("We will be replacing " + '"' + old_data + '"' + ' with ' + '"' + new_data + '". Would you like '
                'to continue? Enter "yes" or "no".').lower()
    replace_data = [(old_data, new_data)]
    if cont == 'yes':
        def selective_fr():
            for file in os.listdir(path):
                if file.endswith('.xml'):
                    with open(path + "\\" + file) as openfile:
                        orig_files = openfile.read()
                        for aPair in replace_data:
                            orig_files = orig_files.replace(aPair[0], aPair[1])
                            # output = orig_files
                        changed = open(path, 'w')
                        changed.write(orig_files)
                        changed.truncate()
            print(f'{file} successfully updated')
        selective_fr()
    else:
        exit()

        
build_changes()
