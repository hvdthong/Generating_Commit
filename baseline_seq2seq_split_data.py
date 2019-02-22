from pickle_data import loading_variable, saving_variable
from sklearn.model_selection import KFold


def get_index(data, indexes):
    return [data[i] for i in indexes]


def kfold_split(data, nfolds, random_state=10, shuffle=True):
    kf = KFold(n_splits=nfolds, random_state=random_state, shuffle=shuffle)
    ids, title, diff_code = data
    for train_index, test_index in kf.split(ids):
        train_ids, train_title, train_diffcode = get_index(ids, indexes=train_index), \
                                                 get_index(title, indexes=train_index), \
                                                 get_index(diff_code, indexes=train_index)
        test_ids, test_title, test_diffcode = get_index(ids, indexes=test_index), \
                                              get_index(title, indexes=test_index), \
                                              get_index(diff_code, indexes=test_index)
        train_data, test_data = (train_ids, train_title, train_diffcode), (test_ids, test_title, test_diffcode)
        return train_data, test_data


if __name__ == '__main__':
    project = 'openstack'
    data = loading_variable(pname='baseline_diffcode_' + project)
    ids, title, diff_code = data
    nfolds, random_state, shuffle = 10, 10, True
    train, test = kfold_split(data=data, nfolds=nfolds, random_state=random_state, shuffle=shuffle)
    split_data = (train, test)
    saving_variable(pname='baseline_split_' + project, variable=split_data)