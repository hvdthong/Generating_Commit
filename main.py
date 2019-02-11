from pickle_data import loading_variable


if __name__ == '__main__':
    project = 'openstack'
    data = loading_variable(pname=project)
    print(len(data))
