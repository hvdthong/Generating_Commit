from pickle_data import loading_variable
from data_prepared import title_word_dictionary, baseline_diffcode_word_dictionary, word_index


def load_training_data_to_DataLoader(data):
    ids, title, diffcode = data

    title_word_count = title_word_dictionary(sentences=title)
    title_word2idx = word_index(word_count=title_word_count)

    diffcode_word_count = baseline_diffcode_word_dictionary(diffcode=diffcode)
    diffcode_word2idx = word_index(word_count=diffcode_word_count)

    print(len(title_word_count), len(diffcode_word_count))
    exit()

if __name__ == '__main__':
    project = 'openstack'
    data = loading_variable(pname='baseline_split_' + project)
    train, test = data
    load_training_data_to_DataLoader(data=train)
