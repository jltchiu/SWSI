gcc word2vec.c -o word2vec -lm -pthread -O3 -march=native -funroll-loops
time ./word2vec -train FINAL_decode_text -output vectors.txt -cbow 1 -size 100 -window 17 -negative 5 -hs 0 -sample 1e-4 -threads 30 -binary 0 -iter 20 -min-count 1 -sentence-vectors 1

rm sentence_vectors.txt
python getSentneceVector.py vectors.txt FINAL_decode_text > sentence_vectors.txt

python 1.Extract_vector_for_CLUTO.py


for topics in {2..10} #number of topics
do

FILES=/usr1/jchiu1/Thesis/Interspeech/VectorSpace-CBOW-NEGATIVE-SAMPLING_WER0/Step1-mat_for_CLUTO/*.mat
for f in $FILES
do
  file_name=$(basename $f)
  fb=$(basename $file_name .mat)
  /usr1/jchiu1/Thesis/cluto-2.1.2/Linux-x86_64/vcluster $f $topics
done

done

for topics in {2..10} #number of topics
do

mkdir -p Step2-Result/sentence/$topics/doctopic/

FILES=/usr1/jchiu1/Thesis/Interspeech/VectorSpace-CBOW-NEGATIVE-SAMPLING_WER0/Step1-mat_for_CLUTO/*.sentence.mat
for f in $FILES
do
  file_name=$(basename $f)
  kw=$(basename $file_name .sentence.mat)
  #echo "/usr1/jchiu1/Thesis/doc2mat-1.0/doc2mat Step-1-TxtforCLUTO/$fb.txt Step-2-matforCLUTO/$fb.mat"
  python 3.Cluster_to_doctopic.py Step1-mat_for_CLUTO/$kw.key Step1-mat_for_CLUTO/$kw.sentence.mat.clustering.$topics > Step2-Result/sentence/$topics/doctopic/$kw.sentence.doctopic

  #/usr1/jchiu1/Thesis/cluto-2.1.2/Linux-x86_64/vcluster Step-2-matforCLUTO/$fb.mat $topics
done

python 3.Doctopic_to_result.py Step2-Result/sentence/$topics/doctopic/ > Step2-Result/sentence/$topics/output.txt
python 6.FINAL_Get_Number.py FINAL_reference.txt Step2-Result/sentence/$topics/output.txt > Step2-Result/sentence/$topics/result.txt


done

