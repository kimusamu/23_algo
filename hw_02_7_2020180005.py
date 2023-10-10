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

def downHeap(arr, root, size):
    lc = root * 2 + 1
    if lc >= size: return
    child = lc
    
    rc = lc + 1
    if rc < size:
        if arr[rc] > arr[lc]:
            child = rc

    if arr[root] >= arr[child]: return

    arr[root], arr[child] = arr[child], arr[root]
    downHeap(arr, child, size)

l_arr = len(words)

for i in range(l_arr // 2 - 1, -1, -1):
    downHeap(words, i, l_arr)

for i in range(l_arr - 1, 0, -1):
    words[0], words[i] = words[i], words[0]
    l_arr -= 1
    downHeap(words, 0, l_arr)

print(words)