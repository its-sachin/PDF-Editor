import os, shutil, pdb

initial_path = input('Please write the path of folder: ')

type_dict = {
    'Audio_list' : ('.mp3', '.m4a', '.wav', '.flac'),
    'Video_list' : ('.mp4', '.mkv', '.MKV', '.mpeg'),
    'Documents_list' : ('.xlsx', '.pptx', '.html', '.htm', '.doc', '.pdf', '.txt'),
    'Codes_list' : ('.py', 'sml'),
    'Images_list' : ('.jpg', '.jpeg', '.png', '.tif', '.gif', '.svg', '.webp', '.raw')
}

item_list = os.listdir(initial_path)

# pdb.set_trace()
for ext_type, ext_tuple in type_dict.items():
    folder_name = ext_type.split('_')[0] 
    folder_path = os.path.join(initial_path, folder_name)
    for item in item_list:
        for extension in ext_tuple:
            if item.endswith(extension):
                if os.path.exists(folder_path) == False: 
                    os.mkdir(folder_path)
                item_initial = os.path.join(initial_path, item)
                item_final = os.path.join(folder_path, item)
                shutil.move(item_initial,item_final)
