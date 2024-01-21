import os
import pathlib
import pandas as pd

DIR = "Validation"
cols = ["Utterance", "Dialog_Act", "Dialog_Act_Label","ID", "Type"]

# TODO: Check consistency of number of levels
acts = [
    'gt', 'crq', 'cd', 'irq', 'id', 'orq', 'od', 'gc', 'yq', 'ack', 'op', 'on', 'ap', 
    'comp', 'cr', 'cv', 'yk', 'ci', 'ay', 'vc', 'na', 'cq', 'com', '', 'urq', 'in', 'cdd',
    'o', 'hp', 'acak', 'irrq'
]


for DIR in ["Test", "Train", "Validation"]:
    out = pd.DataFrame()
    for file in os.listdir(DIR):
        path = os.path.join(DIR, file)
        df = pd.read_csv(path)

        o = pd.DataFrame()
        o["ID"] = df["ID"]
        o["Utterance"] = df["Utterance"]
        try: o["Dialog_Act"] = df["Dialog_Act"]
        except:
            try: o["Dialog_Act"] = df["Dialog Act"]
            except:
                try: o["Dialog_Act"] = df["Dialogue Act"]
                except:
                    try: o["Dialog_Act"] = df["Dialogue_Act"]
                    except:
                        print(file)

        for d in o["Dialog_Act"]:
            if len(str(d).split(" ")) > 2:
                print(d)

        

        o["Dialog_Act"] = o["Dialog_Act"].apply(lambda x: str(x).split(" ")[0].split(".")[0].split(",")[0].strip())
        o["Dialog_Act"] = o["Dialog_Act"].apply(lambda x: "na" if str(x) == "nan" else x)
        # TODO
        o["Dialog_Act_Label"] = o["Dialog_Act"].apply(lambda x: acts.index(x) % 10 )

        # for i in o["ID"]:
        #     if "_" not in i:
        #         print(i)
        
        o["Type"] = df["Type"]
        # for d in o["Type"]:
        #     if (str(d) == "nan"):
        #         print(d)
            
        o = o.reindex(sorted(o.columns), axis=1)
        # print(o)
        out = pd.concat([out, o], axis=0)

    out.set_index("ID")
    out.to_csv("a2g_"+DIR.lower()+".csv")
    # print(out)
    # print(df[cols].head())
# print(out)
# print(len(out["Dialog_Act"].unique()))
# print((out["Dialog_Act"].unique()))

