def compute(tp, fp, fn):
    '''
    This function computes the precision, recall, and f1 score 

    '''

    # Check inputs
    if not isinstance(tp, int):
        print('tp must be int')
        return

    if not isinstance(fp, int):
        print('fp must be int')
        return

    if not isinstance(fn, int):
        print('fn must be int')
        return

    for i in [tp, fp, fn]:
        if i <= 0:
            print('tp and fp and fn must be greater than zero')
            return

    # Compute
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print(f'precision is {precision}')
    print(f'recall is {recall}')
    print(f'f1-score is {f1_score}')


# Test
if __name__ == '__main__':
    tp = 2
    fp = 3
    fn = 4
    compute(tp, fp, fn)

    print('-------------------')

    tp = 'a'
    fp = 3
    fn = 4
    compute(tp, fp, fn)
