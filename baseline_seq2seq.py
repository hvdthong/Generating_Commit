from pickle_data import loading_variable


if __name__ == '__main__':
    project = 'openstack'
    data = loading_variable(pname='baseline_split_' + project)
    train, test = data
    print(len(train), len(test))