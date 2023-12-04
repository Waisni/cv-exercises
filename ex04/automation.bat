echo "Running ResNet-18 on CIFAR-10 with frost corruption severity 2"
echo "Number of BN updates: 1"
@python run_resnet.py --data_dir ..\data\ --corruption "frost" --severity 2 --apply_bn --num_bn_updates 1 | findstr "Loss Accuracy"

echo "Number of BN updates: 5"
@python run_resnet.py --data_dir ..\data\ --corruption "frost" --severity 2 --apply_bn --num_bn_updates 5 | findstr "Loss Accuracy

echo "Number of BN updates: 10"
@python run_resnet.py --data_dir ..\data\ --corruption "frost" --severity 2 --apply_bn --num_bn_updates 10 | findstr "Loss Accuracy"

echo "Number of BN updates: 20"
@python run_resnet.py --data_dir ..\data\ --corruption "frost" --severity 2 --apply_bn --num_bn_updates 20 | findstr "Loss Accuracy"

echo "Number of BN updates: 50"
@python run_resnet.py --data_dir ..\data\ --corruption "frost" --severity 2 --apply_bn --num_bn_updates 50 | findstr "Loss Accuracy"

echo "Number of BN updates: 100"
@python run_resnet.py --data_dir ..\data\ --corruption "frost" --severity 2 --apply_bn --num_bn_updates 100 | findstr "Loss Accuracy"