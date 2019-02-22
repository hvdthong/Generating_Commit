from pickle_data import loading_variable
from data_prepared import baseline_diffcode_word_dictionary
import matplotlib.pyplot as plt


if __name__ == '__main__':
    project = 'openstack'
    data = loading_variable(pname='baseline_diffcode_' + project)
    ids, title, diff_code = data
    print(len(ids), len(title), len(diff_code))
    length_title = [len(t.split()) for t in title]
    length_diff_code = list()
    for patch in diff_code:
        files = ''
        for file in patch:
            files += file
        split_files = files.split()
        length_diff_code.append(len(split_files))
    print('Max title: %i, max diff_code: %i' % (max(length_title), max(length_diff_code)))
    print(len([1 for t in length_title if t <= 25]))
    # num_bins = 10
    # plt.hist(length_title, bins='auto', facecolor='blue', alpha=0.5)
    # plt.show()

