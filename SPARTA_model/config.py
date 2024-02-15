import torch
config = {
    # data
    "data_dir":"../HOPE_data/hinglish/",
    "data_files":{
        "train":"a2g_train.csv",
        "valid":"a2g_validation.csv",
        "test":"a2g_test.csv",
    },
    # field to read from the dataset, its is limited to our dataset only
    "fields":{
        "text":"Utterance",
        "act":"Dialog_Act",
        "label":"Dialog_Act_Label",
        "id":"ID",
        "speaker":"Type"
    },
    
    "max_len":512,
    "batch_size": 16,
    "num_workers":8,
    
    "previous_sid":"start",
    
    # models
    "model_name":"l3cube-pune/hing-roberta",
    "hidden_size":768,
    "num_layers":1,
    "num_heads":12,
    "dropout":0.15,
    "need_weights":True,
    "start_sid":"start",
    "window_size":6,

    # "speaker_classifier_ckpt_path":"./drive/MyDrive/speaker-classifier/classifier.ckpt",
    
    "num_speakers":2,
    
    "hidden":[1024, 768, 512, 256, 128, 64],
    
    "num_dialogue_acts":12,
    
    "model_config": [{"dac_inputs": 6}], #model_config,
    "select_model_config":-1, # it will be from [0, 1, 2, 3, 4, 5, 6, 7]
   
    
    
    # training config
    # training
    "device":torch.device("cuda" if torch.cuda.is_available() else "cpu"),
    "save_dir":"./",
    "project":"dialogue-act-classification",
    
    "lr":1e-5,
    "monitor":"val_f1",
    "min_delta":0.0001,
    "patience":5,
    "filepath":"./models/{epoch}-{val_accuracy:4f}",
    "precision":32,
    "epochs": 25,
    "average":"macro"
    
}