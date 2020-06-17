#!/bin/bash
echo $0 

option=$1
lang=$2

echo $option
echo $lang


bot_root="bot/config/languages/$lang"
config="$bot_root/config.yml"
domain="$bot_root/domain.yml"
data="$bot_root/data" 
stories="bot/config/languages/stories.md"

train(){

    echo $bot_root
    echo $config
    echo $domain
    echo $data
    echo $stories

    rasa train --config $config --domain $domain --data $data $stories --out "bot/models" --fixed-model-name "model-$lang"

}

train_nlu(){

    # echo $bot_root
    # echo $config
    # echo $domain
    # echo $data
    # echo $stories

    rasa train nlu --nlu $data --config $config --out "bot/models" --fixed-model-name "nlu-model-$lang"

}

run(){

    model="bot/models/model-$lang.tar.gz"
    rasa shell --model $model
}

case $option
in
    "train") train "$lang";;
    "train_nlu") train_nlu "$lang";;
    "run") run "$lang" ;;
esac