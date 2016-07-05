python 1-Extract_for_hdp.py

cp -rf ./Step1-txt_for_HDP/num_test_instances.all.txt /usr1/jchiu1/Thesis/hdp-wsi/wsi_input/thesis/sentence/
cp -rf ./Step1-txt_for_HDP/*.lemma /usr1/jchiu1/Thesis/hdp-wsi/wsi_input/thesis/sentence/all/

origin_folder=$PWD

cd /usr1/jchiu1/Thesis/hdp-wsi
bash run_wsi.sh

cd $origin_folder
cp /usr1/jchiu1/Thesis/hdp-wsi/wsi_output/thesis_output/sentence Step2-HDP-Output/HDP_output.txt

python 2-Get_HDP_doctopic.py Step2-HDP-Output/HDP_output.txt

python 3.Doctopic_to_result.py Step3-Result/doctopic/ > Step3-Result/output.txt
python 6.FINAL_Get_Number.py FINAL_reference.txt Step3-Result/output.txt > Step3-Result/result.txt

