#!/bin/bash
#for i in {1..5}

#echo "python 1.1-FINAL_Extract_for_mallet.py asr 0"
#python 1.1-FINAL_Extract_for_mallet.py asr 0
#for seg_size in 

arrayname=( 4 9 17 26 34 42 50 ) #segment size and asr for video and sentence

## get item count using ${arrayname[@]} ##
for m in "${arrayname[@]}"
do
#  echo "${m}"
  # do something on $m 
  echo "python 1.FINAL_Extract_for_mallet.py ${m}"
  python 1.FINAL_Extract_for_mallet.py ${m}

done

#2. convert from text to MALLET format
FILES=/usr1/jchiu1/Thesis/FINAL_system/1.Txt_For_Mallet/*
for f in $FILES
do
  file_name=$(basename $f)
  fb=$(basename $file_name .txt)
  echo "/usr1/jchiu1/MALLET/mallet-2.0.7/bin/mallet import-file --input ./1.Txt_For_Mallet/$file_name  --output ./2.Mallet_Input/$fb.mallet --keep-sequence --remove-stopwords"
  /usr1/jchiu1/MALLET/mallet-2.0.7/bin/mallet import-file --input ./1.Txt_For_Mallet/$file_name  --output ./2.Mallet_Input/$fb.mallet --keep-sequence --remove-stopwords
done

#3. MALLET LDA

#for j in {1..3}
for topics in {2..10} #number of topics
do

FILES=/usr1/jchiu1/Thesis/FINAL_system/2.Mallet_Input/*.mallet
for f in $FILES
do
  file_name=$(basename $f)
  fb=$(basename $file_name .mallet) #the fb here is like kw.video or kw.sentence
  echo "/usr1/jchiu1/MALLET/mallet-2.0.7/bin/mallet train-topics --input ./2.Mallet_Input/$file_name --num-topics $topics --output-doc-topics ./3-1.Mallet_dockey/$fb.doctopic --output-model ./3-2.Mallet_model/$fb.model"
  /usr1/jchiu1/MALLET/mallet-2.0.7/bin/mallet train-topics --input ./2.Mallet_Input/$file_name --num-topics $topics --output-doc-topics ./3-1.Mallet_doctopic/$fb.doctopic --output-model ./3-2.Mallet_model/$fb.model
done

mkdir -p 6.Result/video/$topics/doctopic/
mv ./3-1.Mallet_doctopic/*.video.doctopic 6.Result/video/$topics/doctopic/
python 6.FINAL_doctopic_to_result.py 6.Result/video/$topics/doctopic/ > 6.Result/video/$topics/output.txt
python 6.FINAL_Get_Number.py FINAL_reference.txt 6.Result/video/$topics/output.txt > 6.Result/video/$topics/result.txt

mkdir -p 6.Result/sentence/$topics/doctopic/
mv ./3-1.Mallet_doctopic/*.sentence.doctopic 6.Result/sentence/$topics/doctopic/
python 6.FINAL_doctopic_to_result.py 6.Result/sentence/$topics/doctopic/ > 6.Result/sentence/$topics/output.txt
python 6.FINAL_Get_Number.py FINAL_reference.txt 6.Result/sentence/$topics/output.txt > 6.Result/sentence/$topics/result.txt

for m in "${arrayname[@]}"
do

mkdir -p 6.Result/$m/$topics/doctopic/
mv ./3-1.Mallet_doctopic/*.$m.doctopic 6.Result/$m/$topics/doctopic/
python 6.FINAL_doctopic_to_result.py 6.Result/$m/$topics/doctopic/ > 6.Result/$m/$topics/output.txt
python 6.FINAL_Get_Number.py FINAL_reference.txt 6.Result/$m/$topics/output.txt > 6.Result/$m/$topics/result.txt

done

#first layer hybrid
FILES=/usr1/jchiu1/Thesis/FINAL_system/3-2.Mallet_model/*.sentence.model #hybrid on sentence
for f in $FILES
do
  file_name=$(basename $f)
  kw=$(basename $file_name .sentence.model)
   # take action on each file. $f store current file name
  echo "/usr1/jchiu1/MALLET/mallet-2.0.7/bin/mallet train-topics --input ./2.Mallet_Input/$kw.sentence.mallet --num-topics $topics --output-doc-topics ./3-1.Mallet_doctopic/$kw.video-sentence.doctopic --input-model ./3-2.Mallet_model/$kw.video.model --output-model ./3-2.Mallet_model/$kw.video-sentence.model"
  /usr1/jchiu1/MALLET/mallet-2.0.7/bin/mallet train-topics --input ./2.Mallet_Input/$kw.sentence.mallet --num-topics $topics --output-doc-topics ./3-1.Mallet_doctopic/$kw.video-sentence.doctopic --input-model ./3-2.Mallet_model/$kw.video.model --output-model ./3-2.Mallet_model/$kw.video-sentence.model
done

mkdir -p 6.Result/video-sentence/$topics/doctopic/
mv ./3-1.Mallet_doctopic/*.video-sentence.doctopic 6.Result/video-sentence/$topics/doctopic/
python 6.FINAL_doctopic_to_result.py 6.Result/video-sentence/$topics/doctopic/ > 6.Result/video-sentence/$topics/output.txt
python 6.FINAL_Get_Number.py FINAL_reference.txt 6.Result/video-sentence/$topics/output.txt > 6.Result/video-sentence/$topics/result.txt

for m in "${arrayname[@]}"
do

FILES=/usr1/jchiu1/Thesis/FINAL_system/3-2.Mallet_model/*.sentence.model #hybrid on middle size
for f in $FILES
do
  file_name=$(basename $f)
  kw=$(basename $file_name .sentence.model)
   # take action on each file. $f store current file name
  echo "/usr1/jchiu1/MALLET/mallet-2.0.7/bin/mallet train-topics --input ./2.Mallet_Input/$kw.$m.mallet --num-topics $topics --output-doc-topics ./3-1.Mallet_doctopic/$kw.video-$m.doctopic --input-model ./3-2.Mallet_model/$kw.video.model --output-model ./3-2.Mallet_model/$kw.video-$m.model"
  /usr1/jchiu1/MALLET/mallet-2.0.7/bin/mallet train-topics --input ./2.Mallet_Input/$kw.$m.mallet --num-topics $topics --output-doc-topics ./3-1.Mallet_doctopic/$kw.video-$m.doctopic --input-model ./3-2.Mallet_model/$kw.video.model --output-model ./3-2.Mallet_model/$kw.video-$m.model
done

mkdir -p 6.Result/video-$m/$topics/doctopic/
mv ./3-1.Mallet_doctopic/*.video-$m.doctopic 6.Result/video-$m/$topics/doctopic/
python 6.FINAL_doctopic_to_result.py 6.Result/video-$m/$topics/doctopic/ > 6.Result/video-$m/$topics/output.txt
python 6.FINAL_Get_Number.py FINAL_reference.txt 6.Result/video-$m/$topics/output.txt > 6.Result/video-$m/$topics/result.txt

done

#second layer hybrid

for m in "${arrayname[@]}"
do

FILES=/usr1/jchiu1/Thesis/FINAL_system/3-2.Mallet_model/*.sentence.model #hybrid on biggest size (This will get kw)
for f in $FILES
do
  file_name=$(basename $f)
  kw=$(basename $file_name .sentence.model)
   # take action on each file. $f store current file name
  echo "/usr1/jchiu1/MALLET/mallet-2.0.7/bin/mallet train-topics --input ./2.Mallet_Input/$kw.sentence.mallet --num-topics $topics --output-doc-topics ./3-1.Mallet_doctopic/$kw.video-$m-sentence.doctopic --input-model ./3-2.Mallet_model/$kw.video-$m.model --output-model ./3-2.Mallet_model/$kw.video-$m-sentence.model"
  /usr1/jchiu1/MALLET/mallet-2.0.7/bin/mallet train-topics --input ./2.Mallet_Input/$kw.sentence.mallet --num-topics $topics --output-doc-topics ./3-1.Mallet_doctopic/$kw.video-$m-sentence.doctopic --input-model ./3-2.Mallet_model/$kw.video-$m.model --output-model ./3-2.Mallet_model/$kw.video-$m-sentence.model
done

mkdir -p 6.Result/video-$m-sentence/$topics/doctopic/
mv ./3-1.Mallet_doctopic/*.video-$m-sentence.doctopic 6.Result/video-$m-sentence/$topics/doctopic/
python 6.FINAL_doctopic_to_result.py 6.Result/video-$m-sentence/$topics/doctopic/ > 6.Result/video-$m-sentence/$topics/output.txt
python 6.FINAL_Get_Number.py FINAL_reference.txt 6.Result/video-$m-sentence/$topics/output.txt > 6.Result/video-$m-sentence/$topics/result.txt

done













done #for topic loop







