from pickle_data import loading_variable
import string
from nltk.tokenize import word_tokenize
from pickle_data import saving_variable


def title_word_dictionary(sentences):
    word_count = {}
    for sent in sentences:
        for word in sent.split():
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    word_count['</s>'] = len(sentences)
    return word_count


def title_word_index(word_count):
    word2idx = {k: v + 3 for v, k in enumerate(word_count.keys())}
    word2idx['<pad>'] = 0
    word2idx['<s>'] = 1
    word2idx['<unk>'] = 2
    return word2idx


#####################################################################################################
#####################################################################################################
# get code information
def get_id(data):
    ids, msgs, diff_code = data
    return ids


def get_title(data):
    ids, msgs, diff_code = data
    titles = list()
    for m in msgs:
        title = m['title'].lower()
        punctuation_table = title.maketrans({i: None for i in string.punctuation})
        title = title.translate(punctuation_table)
        titles.append(title)
    return titles


def check_first_comment_line(line, project):
    # check whether the code line is a comment
    flag = None
    if project == 'openstack':
        for i in range(1, len(line)):
            if line[i] == ' ' or line[i] == '\t':
                flag = False
                continue
            elif flag is False and line[i] == '#':
                flag = True
                return flag
            else:
                flag = False
                return flag
    else:
        print('You need to give correct project name')
        exit()


def check_second_comment_line(line, project):
    # if the code line is not a comment, check if there is a comment within a line
    # if True, get the first part. For example:
    # python code: if a == 3:  # checking variable a
    # we only get the "if a == 3:"
    if project == 'openstack':
        return line.split('#')[0].strip()
    else:
        print('You need to give correct project name')
        exit()


def remove_comment_project(file, project):
    file_name, diff_code = file['file'], file['diff']
    new_diff_file = list()
    for line in diff_code:
        if project == 'openstack':
            line_comment = check_first_comment_line(line=line, project=project)
            if line_comment is False:
                new_line = check_second_comment_line(line=line, project=project)
                if len(new_line) > 1:
                    new_diff_file.append(new_line)
    return file_name, new_diff_file


def get_diff_code(data, project):
    ids, msgs, diff_code = data
    if project == 'openstack':
        # openstack using python to write it
        new_diff_code = list()
        for d in diff_code:
            new_d = list()
            for f in d:
                new_f = dict()
                file_name, diff_file = remove_comment_project(file=f, project=project)
                new_f['file'], new_f['diff'] = file_name, diff_file
                new_d.append(new_f)
            new_diff_code.append(new_d)
        return new_diff_code


#####################################################################################################
#####################################################################################################
# clean code line: remove punctuation. we don't need to consider the added code or removed code
# clean code for running baselines
def baseline_clean_code_line(line):
    for p in string.punctuation:
        if line.startswith('+#') or line.startswith('-#'):
            line = line[2:].replace(p, ' ' + p + ' ')
        elif line.startswith('+') or line.startswith('-') or line.startswith('#'):
            line = line[1:].replace(p, ' ' + p + ' ')
        else:
            line = line.replace(p, ' ' + p + ' ')
    return line


def baseline_clean_code(data):
    new_diffs = list()
    for diff in data:
        new_diff = list()
        for file_ in diff:
            lines = [' '.join(word_tokenize(baseline_clean_code_line(line=line))) for line in file_['diff']]
            new_diff.append(' '.join(word_tokenize(' '.join(lines).strip())))
        new_diffs.append(new_diff)
    return new_diffs
#####################################################################################################
#####################################################################################################


if __name__ == '__main__':
    project = 'openstack'
    # project = 'qt'
    data = loading_variable(pname=project)
    ids, title, diff_code = get_id(data=data), get_title(data=data), baseline_clean_code(
        get_diff_code(data=data, project=project))
    data = (ids, title, diff_code)
    saving_variable(pname='baseline_diffcode_' + project, variable=data)
    print(len(ids), len(title), len(diff_code))
