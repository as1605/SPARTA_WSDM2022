import os
import pandas as pd

directory ='train'
act_labels={'ack': 1, 'cd': 2, 'crq': 3, 'gc': 4, 'gt': 5, 'id': 6, 'irq': 7, 'od': 8, 'on': 9, 'op': 10, 'orq': 11, 'yq': 12}
super_dacts = {
                'crq': 0, 'yq': 0, 'orq': 0, 'irq': 0,
                'gt': 1, 'gc': 1, 'ack': 1,
                'id': 2, 'cd': 2, 'od': 2, 'op': 2, 'on': 2
            }
num_labels=13
num_super_labels=3
type_labels={'P': 'P', 'T': 'T'}

data = []
for f in os.listdir(directory):
    id = f.split(".")[0]

    if not os.path.isfile(os.path.join(directory, f)): continue
    if not f.endswith(".csv"): continue
    file_path = os.path.join(directory, f) 
    df = pd.read_csv(file_path)

    if not set(['Utterance', 'Type', 'Dialogue Act']).issubset(set(df.columns)): continue
    df['Dialog_Act'] = df['Dialogue Act'].map(lambda x: str(x).split(",")[0].split(" ")[0].split(".")[0])
    df['Dialog_Act_Label'] = df['Dialog_Act'].map(lambda x: act_labels[x] if x in act_labels else 0)
    df['Type'] = df['Type'].map(lambda x: type_labels[x] if x in type_labels else 'P')

    messages = df.to_dict('records')

    M = []
    for m, i in zip(messages, range(len(messages))):
        m["ID"] = f"{id}_{i}"
        # print(m)
        # break
        m.pop("Dialogue Act")
        M.append(m)

    data += M
df = pd.DataFrame(data)
df.to_csv(f"a2g_{directory}.csv")