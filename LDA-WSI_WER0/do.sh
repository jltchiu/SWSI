python 1.FINAL_Extract_for_mallet.py

#2. convert from text to MALLET format
FILES=/usr1/jchiu1/Thesis/Interspeech/LDA-WSI_WER0/1.Txt_For_Mallet/*
for f in $FILES
do
  file_name=$(basename $f)
  fb=$(basename $file_name .txt)
  echo "/usr1/jchiu1/MALLET/mallet-2.0.7/bin/mallet import-file --input ./1.Txt_For_Mallet/$file_name  --output ./2.Mallet_Input/$fb.mallet --keep-sequence --remove-stopwords"
  /usr1/jchiu1/MALLET/mallet-2.0.7/bin/mallet import-file --input ./1.Txt_For_Mallet/$file_name  --output ./2.Mallet_Input/$fb.mallet --keep-sequence --remove-stopwords
done

for topics in {2..10} #number of topics
do

FILES=/usr1/jchiu1/Thesis/Interspeech/LDA-WSI_WER0/2.Mallet_Input/*.mallet
for f in $FILES
do
  file_name=$(basename $f)
  fb=$(basename $file_name .mallet) #the fb here is like kw.video or kw.sentence
  echo "/usr1/jchiu1/MALLET/mallet-2.0.7/bin/mallet train-topics --input ./2.Mallet_Input/$file_name --num-topics $topics --output-doc-topics ./3.Mallet_doctopic/$fb.doctopic"
  /usr1/jchiu1/MALLET/mallet-2.0.7/bin/mallet train-topics --input ./2.Mallet_Input/$file_name --num-topics $topics --output-doc-topics ./3.Mallet_doctopic/$fb.doctopic
done

mkdir -p 6.Result/sentence/$topics/doctopic/
mv ./3.Mallet_doctopic/*.sentence.doctopic 6.Result/sentence/$topics/doctopic/
python 6.FINAL_doctopic_to_result.py 6.Result/sentence/$topics/doctopic/ > 6.Result/sentence/$topics/output.txt
python 6.FINAL_Get_Number.py FINAL_reference.txt 6.Result/sentence/$topics/output.txt > 6.Result/sentence/$topics/result.txt

done





