import random

words = [

  'hut', 'apostle', 'equipment', 'fop', 'refined', 'parapet', 'mog', 'amputate', 'covetous', 'somebody', 

  'all', 'lobbyist', 'remark', 'subscriber', 'quorum', 'steppe', 'clean', 'cu', 'commend', 'prosy',

  'supererogation', 'indignation', 'wolverine', 'emporium', 'intersect', 'constitution', 'miscast', 'rabbi', 'enmity', 'loft',

  'temporize', 'speedboat', 'agenda', 'delusion', 'addle', 'idolize', 'romance', 'overestimate', 'revive', 'smell', 

  'quite', 'seminar', 'bloomers', 'lives', 'innocuous', 'effluent', 'cross', 'recidivist', 'wet', 'synth', 

  'mantilla', 'tweak', 'lowbrow', 'aviation', 'quadruped', 'capable', 'graphic', 'barman', 'intemperate', 'mastermind', 

  'submit', 'considering', 'riddance', 'polyethene', 'jim', 'varicolored', 'medic', 'ferric', 'minaret', 'capacitor', 

  'pusher', 'gingerbread', 'grizzled', 'upsilon', 'km', 'glade', 'ribbon', 'parascending', 'shinty', 'breve', 

  'hotel', 'similitude', 'fuddle', 'secretariat', 'silicate', 'whinchat', 'abstention', 'untrue', 'toing', 'cnd', 

  'ramification', 'scorn', 'apricot', 'arnica', 'militate', 'muslim', 'homicide', 'overfeed', 'shooting', 'growth',

]

l_arr = len(words)

def partition(arr, beg, end):
    ri = random.randrange(beg, end)
    arr[beg], arr[ri] = arr[ri], arr[beg]
    pv = arr[beg]
    p, q = beg + 1, end - 1

    while True:
        while True:
            if p >= q: break
            if arr[p] < pv : break
            p += 1
        while True:
            if p > q: break
            if arr[q] >= pv : break
            q -= 1
        if p >= q: break
        
        arr[p], arr[q] = arr[q], arr[p]
        p += 1
        q -= 1

    arr[q], arr[beg] = arr[beg], arr[q]
    return q


def quickSort(arr, beg, end):
    if end - beg <= 1 : return

    pi = partition(arr, beg, end)
    quickSort(arr, beg, pi)
    quickSort(arr, pi + 1, end)


quickSort(words, 0, l_arr)
print(words)