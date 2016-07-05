python 1.Extract_for_CLUTO.py

#1. convert from text to  format
FILES=/usr1/jchiu1/Thesis/Interspeech/BOW-Cluster/Step-1-TxtforCLUTO/*.txt
for f in $FILES
do
  file_name=$(basename $f)
  fb=$(basename $file_name .txt)
  echo "/usr1/jchiu1/Thesis/doc2mat-1.0/doc2mat Step-1-TxtforCLUTO/$fb.txt Step-2-matforCLUTO/$fb.mat"
  /usr1/jchiu1/Thesis/doc2mat-1.0/doc2mat Step-1-TxtforCLUTO/$fb.txt Step-2-matforCLUTO/$fb.mat
done


for topics in {2..10} #number of topics
do

FILES=/usr1/jchiu1/Thesis/Interspeech/BOW-Cluster/Step-2-matforCLUTO/*.mat
for f in $FILES
do
  file_name=$(basename $f)
  fb=$(basename $file_name .mat)
  echo "/usr1/jchiu1/Thesis/cluto-2.1.2/Linux-x86_64/vcluster Step-2-matforCLUTO/$fb.mat $topics"
  /usr1/jchiu1/Thesis/cluto-2.1.2/Linux-x86_64/vcluster Step-2-matforCLUTO/$fb.mat $topics
done

done

for topics in {2..10} #number of topics
do

mkdir -p Step-3-Result/sentence/$topics/doctopic/

FILES=/usr1/jchiu1/Thesis/Interspeech/BOW-Cluster/Step-2-matforCLUTO/*.sentence.mat
for f in $FILES
do
  file_name=$(basename $f)
  kw=$(basename $file_name .sentence.mat)
  #echo "/usr1/jchiu1/Thesis/doc2mat-1.0/doc2mat Step-1-TxtforCLUTO/$fb.txt Step-2-matforCLUTO/$fb.mat"
  echo "python 3.Cluster_to_doctopic.py Step-1-TxtforCLUTO/$kw.key Step-2-matforCLUTO/$kw.sentence.mat.clustering.$topics > Step-3-Result/sentence/$topics/doctopic/$kw.sentence.doctopic"
  python 3.Cluster_to_doctopic.py Step-1-TxtforCLUTO/$kw.key Step-2-matforCLUTO/$kw.sentence.mat.clustering.$topics > Step-3-Result/sentence/$topics/doctopic/$kw.sentence.doctopic

  #/usr1/jchiu1/Thesis/cluto-2.1.2/Linux-x86_64/vcluster Step-2-matforCLUTO/$fb.mat $topics
done

python 3.Doctopic_to_result.py Step-3-Result/sentence/$topics/doctopic/ > Step-3-Result/sentence/$topics/output.txt
python 6.FINAL_Get_Number.py FINAL_reference.txt Step-3-Result/sentence/$topics/output.txt > Step-3-Result/sentence/$topics/result.txt

done

