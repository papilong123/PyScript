import os


my_train_path = 'dataset/Caltech256/dataset4u-trn.txt'
my_test_path = 'dataset/Caltech256/dataset4u-val.txt'

my_dataset_path = 'C:/path/to/dataset/Caltech256'


def generate_label(train_path, test_path, dataset_path):
    with open(train_path, 'w') as f1, open(test_path, 'w') as f2:
        for _, directory in enumerate(os.listdir(dataset_path)):
            each_dir_path = dataset_path + f'/{directory}'

            for i, file in enumerate(os.listdir(each_dir_path)):
                file_path = each_dir_path + f'/{file}'
                if i % 5 != 0:
                    f1.writelines([file_path, ' ', directory[:3].lstrip('0') + '\n'])
                else:
                    f2.writelines([file_path, ' ', directory[:3].lstrip('0') + '\n'])


generate_label(my_train_path, my_test_path, my_dataset_path)
