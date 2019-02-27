import torch
from torch.utils.data import Dataset


class DiffCode2Title(Dataset):
    '''
            Diff Code and associated Title sentences.
        '''

    def __init__(self, diffcode, title, diffcode_word_count, title_word_count, diffcode_word2idx, title_word2idx,
                 diffcode_seq_length, title_seq_length):
        self.diffcode = diffcode
        self.title = title
        self.diffcode_word_count = diffcode_word_count
        self.title_word_count = title_word_count
        self.diffcode_word2idx = diffcode_word2idx
        self.title_word2idx = title_word2idx
        self.diffcode_seq_length = diffcode_seq_length
        self.title_seq_length = title_seq_length
        self.unk_diffcode = set()
        self.unk_title = set()

    def __len__(self):
        return len(self.fr_sentences)

    def __getitem__(self, idx):
        '''
            Returns a pair of tensors containing word indices
            for the specified sentence pair in the dataset.
        '''

        # init torch tensors, note that 0 is the padding index
        diffcode_tensor = torch.zeros(self.diffcode_seq_length, dtype=torch.long)
        title_tensor = torch.zeros(self.title_seq_length, dtype=torch.long)

        # Get sentence pair
        diffcode_sentence = self.diff_code[idx].split()
        title_sentence = self.title[idx].split()

        # Add <EOS> tags
        french_sentence.append('</s>')
        english_sentence.append('</s>')

        # Load word indices
        for i, word in enumerate(french_sentence):
            if word in self.fr_word2idx and self.fr_word_count[word] > 5:
                french_tensor[i] = self.fr_word2idx[word]
            else:
                french_tensor[i] = self.fr_word2idx['<unk>']
                self.unk_fr.add(word)

        for i, word in enumerate(english_sentence):
            if word in self.en_word2idx and self.en_word_count[word] > 5:
                english_tensor[i] = self.en_word2idx[word]
            else:
                english_tensor[i] = self.en_word2idx['<unk>']
                self.unk_en.add(word)

        sample = {'french_tensor': french_tensor, 'french_sentence': self.fr_sentences[idx],
                  'english_tensor': english_tensor, 'english_sentence': self.en_sentences[idx]}
        return sample
