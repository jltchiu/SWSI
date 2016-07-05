for topics in {2..10} #number of topics
do

FILES=/usr1/jchiu1/Thesis/FINAL_system/6.Result/video/$topics/doctopic/*
for f in $FILES
do
  file_name=$(basename $f)
  fb=$(basename $file_name .doctopic)
  echo "python 2.LDA_to_mat.py $f Step-2-matforCLUTO/$fb.LDA.$topics.mat Step-2-matforCLUTO/$fb.LDA.$topics.key"
  python 2.LDA_to_mat.py $f Step-2-matforCLUTO/$fb.LDA.$topics.mat Step-2-matforCLUTO/$fb.LDA.$topics.key
done

done

for topics in {2..10} #number of topics
do

FILES=/usr1/jchiu1/Thesis/CLUTO_systems/Step-2-matforCLUTO/*.LDA.$topics.mat
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


mkdir -p Step-3-doctopics/video-lda/$topics/doctopic/

FILES=/usr1/jchiu1/Thesis/CLUTO_systems/Step-2-matforCLUTO/*.sentence.mat
for f in $FILES
do
  file_name=$(basename $f)
  kw=$(basename $file_name .sentence.mat)
  #echo "/usr1/jchiu1/Thesis/doc2mat-1.0/doc2mat Step-1-TxtforCLUTO/$fb.txt Step-2-matforCLUTO/$fb.mat"
  echo "python 3.Cluster_to_doctopic.py Step-2-matforCLUTO/$kw.video.LDA.$topics.key Step-2-matforCLUTO/$kw.video.LDA.$topics.mat.clustering.$topics > Step-3-doctopics/video-lda/$topics/doctopic/$kw.video.doctopic"
  python 3.Cluster_to_doctopic.py Step-2-matforCLUTO/$kw.video.LDA.$topics.key Step-2-matforCLUTO/$kw.video.LDA.$topics.mat.clustering.$topics > Step-3-doctopics/video-lda/$topics/doctopic/$kw.video.doctopic

  #/usr1/jchiu1/Thesis/cluto-2.1.2/Linux-x86_64/vcluster Step-2-matforCLUTO/$fb.mat $topics
done

python 3.Video_doctopic_to_result.py Step-3-doctopics/video-lda/$topics/doctopic/ > Step-3-doctopics/video-lda/$topics/output.txt
python 6.FINAL_Get_Number.py FINAL_reference.txt Step-3-doctopics/video-lda/$topics/output.txt > Step-3-doctopics/video-lda/$topics/result.txt



done






